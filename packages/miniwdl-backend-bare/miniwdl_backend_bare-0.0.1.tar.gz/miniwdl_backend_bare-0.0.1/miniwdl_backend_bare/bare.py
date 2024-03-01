import os
import psutil
import subprocess
import multiprocessing
from contextlib import ExitStack
import WDL
from WDL._util import StructuredLogMessage as _


class BareContainer(WDL.runtime.task_container.TaskContainer):
    """
    Subclasses miniwdl TaskContainer; each task runner thread instantiates this class to set up &
    execute a container.

    Refer to the base class:
      https://github.com/chanzuckerberg/miniwdl/blob/main/WDL/runtime/task_container.py
    """

    # Set by copy_input_files() below
    _copied_input_files: bool = False

    @classmethod
    def global_init(cls, cfg, logger):
        """
        Perform any necessary process-wide initialization of the container backend
        """
        cls._resource_limits = {
            "cpu": multiprocessing.cpu_count(),
            "mem_bytes": psutil.virtual_memory().total,
        }
        logger.info(
            _(
                "initialized BareContainer plugin",
                resource_limits=cls._resource_limits,
            )
        )

    @classmethod
    def detect_resource_limits(cls, cfg, logger):
        """
        Detect the maximum cpu and mem_bytes the backend can provision -for any one container-
        """
        return cls._resource_limits

    def __init__(self, cfg, run_id, host_dir):
        super().__init__(cfg, run_id, host_dir)
        self.container_dir = self.host_dir  # Annotate Me

    def copy_input_files(self, logger):
        """
        link input files into the task working directory
        """
        if not self._copied_input_files:
            for src, dst in self.input_path_map.items():
                logger.debug(_("link input file", input=src, link=dst))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                os.symlink(os.path.relpath(src, os.path.dirname(dst)), dst)
            self._copied_input_files = True

    def process_runtime(self, logger, runtime_eval):
        super().process_runtime(logger, runtime_eval)

    def _run(self, logger, terminating, command):
        """
        Run task

        Note: retry logic may cause _run() to be invoked multiple times on the same object
        """
        try:
            # contextlib.ExitStack() is useful for numerous "finally" actions
            with ExitStack() as cleanup:
                self.copy_input_files(logger)

                # Formulate `BareContainer` invocation
                invocation = self.bare_run_invocation(command)

                # The task running context updates miniwdl's status bar for running tasks; we
                # should enter it when our container actually starts (not while it's still in a
                # resource scheduling queue).
                cleanup.enter_context(self.task_running_context())

                # Store the stdout/stderr of `BareContainer` itself (not the task command running
                # inside the container, which we handle separately below) in the run directory.
                run_log_filename = os.path.join(self.host_dir, "run.log")
                run_log = cleanup.enter_context(open(run_log_filename, "wb"))

                # Start `BareContainer` subprocess
                logger.debug(_("BareContainer", invocation=invocation))
                proc = subprocess.Popen(
                    invocation,
                    cwd=self.host_work_dir(),
                    stdout=run_log,
                    stderr=subprocess.STDOUT,
                    shell=True,
                )
                logger.notice(_("BareContainer", pid=proc.pid, log=run_log_filename))

                # The poll_stderr context yields a helper function that we should invoke frequently
                # while the task runs, to forward its standard error to miniwdl's verbose log.
                poll_stderr = cleanup.enter_context(self.poll_stderr_context(logger))

                # Long-poll for completion
                exit_code = None
                while exit_code is None:
                    # The terminating() flag turns true when miniwdl has received SIGTERM/SIGINT.
                    # In this event we should gracefully abort our container.
                    if terminating():
                        proc.terminate()
                    try:
                        exit_code = proc.wait(1)
                    except subprocess.TimeoutExpired:
                        pass
                    # Frequently invoke poll_stderr()
                    poll_stderr()

                # Invoke poll_stderr() once more after container exit, to get any final logs.
                poll_stderr()

                # If we aborted due to terminating(), then raise WDL.runtime.Terminated().
                # In a production implementation that submits to some external queue, we should
                # also check for terminating() flag while sitting in the queue and cancel the job
                # promptly if triggered. In that case we can raise Terminated(quiet=true) to emit
                # less log noise during the abort sequence (for tasks that never really started).
                if terminating():
                    raise WDL.runtime.Terminated()

                # Return container exit status (which might or might not be zero)
                assert isinstance(exit_code, int)
                return exit_code
        except WDL.runtime.Terminated:
            raise
        except Exception as exn:
            # In the event of an error (other than Terminated or non-zero container exit status),
            # emit an informative log message and raise a WDL.Error.RuntimeError (or some subclass
            # thereof)
            logger.error(_("unexpected BareContainer error", exception=str(exn)))
            raise WDL.Error.RuntimeError(str(exn))

    def bare_run_invocation(self, command):
        """
        Stage the command to a file and formulate the invocation
        """
        cmd_path = os.path.join(self.host_dir, "command")
        with open(cmd_path, "w") as outfile:
            outfile.write(command)
        ans = [
            self.cfg.get("task_runtime", "command_shell")
            + " "
            + cmd_path
            + " >> "
            + self.host_stdout_txt()
            + " 2>> "
            + self.host_stderr_txt()
        ]
        return ans

# miniwdl-backend-bare

This bare [container backend](https://miniwdl.readthedocs.io/en/latest/runner_backends.html) plugin for [miniwdl](https://github.com/chanzuckerberg/miniwdl) runs WDL task natively within the host enviroment. This plugin proves particularly advantageous for containerizing WDL workflows using Docker.

To install and apply this plugin:

```bash
pip3 install miniwdl-backend-bare
## Or 
# pip3 install git+https://github.com/ghbore/miniwdl-backend-bare
export MINIWDL__SCHEDULER__CONTAINER_BACKEND=bare
```

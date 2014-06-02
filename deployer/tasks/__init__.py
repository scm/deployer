from fabric.api import task, env
from fabric.utils import _AttributeDict
from deployer.utils.config import load
from deployer.utils.decorators import targeted, cache_config

__author__ = 'adam.jorgensen.za@gmail.com'


@task(alias='config')
@cache_config
def config(*configs):
    """
    Applies the contents of one or more YAML files to the Fabric env

    :param *configs: Comma-separated names of YAML config files located in config
    """
    configs = dict(configs)
    if 'all' in configs:
        env.update(configs['all'])
        del configs['all']
    for config, config_data in configs.items():
        env.update(config_data)


@task(alias='target')
@cache_config('config/targets')
def target(*targets):
    """
    Set the deployment target system(s)

    :param *targets: Comma-separated names of YAML config files located in config/targets
    """
    env.targets = _AttributeDict(targets)


@task(alias='project')
@cache_config('config/projects')
def project(*projects):
    """
    Specify the project(s) to deploy to the target system.

    :param *projects: Comma-separated names of YAML config files located in config/projects
    """
    env.projects = _AttributeDict(projects)


@task
def branch(branch):
    """
    Specify the branch to deploy to the target system. This branch is used for all projects that will be deployed

    :param branch: Name of the branch to deploy
    """
    env.branch = branch


@task(alias='setup')
@targeted
def setup():
    """
    Checks out Projects on the target system
    """
    pass


@task(alias='build')
@targeted
def build():
    """
    Builds Docker images for Projects on the target system
    """
    pass


@task(alias='deploy')
@targeted
def deploy():
    """
    Deploys Docker containers for Projects on the target system
    """
    pass

from fabric.api import task, env
from deployer.utils.config import load
from deployer.utils.decorators import targeted

__author__ = 'adam.jorgensen.za@gmail.com'


@task
def config(config):
    """
    Applies the contents of a YAML file to the Fabric env

    :param config: Name of the YAML config located in config to load and apply to the Fabric env
    """
    configs = env.setdefault('configs', {})
    if config not in configs:
        config_data = load('config/%s.yml' % config)
        configs[config] = config_data
    env.update(configs[config])


@task
def target(target):
    """
    Set the deployment target system

    :param target: Name of the YAML config file located in config/targets associated with the target system
    """
    targets = env.setdefault('targets', {})
    if target not in targets:
        target_config = load('config/targets/%s.yml' % target)
        targets[target] = target_config
    env.target = targets[target]


@task
def project(project):
    """
    Specify the project to deploy to the target system.

    :param project: Name of the YAML config file located in config/projects associated with the project
    """
    projects = env.setdefault('projects', {})
    if project not in projects:
        project_config = load('config/projects/%s.yml' % project)
        projects[project] = project_config
    env.project = projects[project]


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

from fabric.api import task, env
from deployer.utils.config import load
from deployer.utils.decorators import targeted

__author__ = 'adam.jorgensen.za@gmail.com'


@task
def config(path):
    """
    Applies the contents of a JSON file to the Fabric env

    :param path:
    """
    env.update(load(path))


@task
def target(target):
    """
    Set the deployment target system

    :param target: Name of the JSON config file located in config/targets associated with the target system
    """
    env.update({'target': load('config/targets/%s.yml' % target)})


@task
def project(project):
    """
    Specify the project to deploy to the target system.

    :param project: Name of the JSON config file located in config/projects associated with the project
    """
    env.update({'project': load('config/projects/%s.yml' % project)})


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

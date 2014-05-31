from fabric.api import task, env
from deployer.utils.json import load

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
    env.update({'target': load('config/targets/%s.json' % target)})


@task
def project(project):
    """
    Specify the project to deploy to the target system.

    :param project: Name of the JSON config file located in config/projects associated with the project
    """
    env.update({'project': load('config/projects/%s.json' % project)})


@task
def branch(branch):
    """
    Specify the branch to deploy to the target system. This branch is used for all projects that will be deployed

    :param branch: Name of the branch to deploy
    """
    env.branch = branch


@task
def setup():
    """
    Sets up the deployment system on the target system:
     1. Installs necessary system-wide software
     2. Checks out deployer
     3. Checks out projects specified in config/projects.json
    """
    pass


@task
def build():
    pass


@task
def deploy():
    pass

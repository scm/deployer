from fabric.api import task, env
from json import load

__author__ = 'adam.jorgensen.za@gmail.com'


@task
def config(path):
    """
    Applies the contents of a JSON file to the Fabric env

    :param path:
    """
    env.update(load(open(path, 'r')))


@task
def target(target):
    """
    Set the deployment target system

    :param target: Name of the JSON config file located in config/targets associated with the target system
    """
    env.update({'target': load(open('config/targets/%s.json' % target, 'r'))})


@task
def project(project):
    """
    Specify the project to deploy to the target system.

    :param project: Name of the JSON config file located in config/projects associated with the project
    """
    env.update({'project': load(open('config/projects/%s.json' % project, 'r'))})


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

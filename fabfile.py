from fabric.api import *

__author__ = 'adam.jorgensen.za@gmail.com'


@task
def target(target):
    """
    Set the deployment target system

    :param target: Name of the config file located in config/targets associated with the target system
    """
    pass


@task
def branch(branch):
    """
    Specify the branch to deploy to the target system. This branch is used for all projects that will be deployed

    :param branch: Name of the branch to deploy
    """
    pass


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

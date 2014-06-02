========
Deployer
========

A web-application deployment tool built on Fabric, Git and Docker


Requirements
============

Client
------

 * Python 2.7.x
 * PyYAML 3.11
 * Fabric 1.8.x
 * Git 1.9.x

The client system is generally your own machine, although it may also be some kind of centralised system that
is allocated to manage deployments (Probably with the aid of a CI system).

Target(s)
---------

 * Apache 2.2.x
 * Git 1.9.x
 * Docker 0.9.1

Configuring the target system(s) for Git and Docker usage is currently beyond the scope of this tool (Although this
may change in the future). As such, it is the responsibility of the user to provision and configure his/her systems
correctly.


Installation
============

Installing Deployer on the Client system is as simple as checking the project out from Git. Once this has been done
Deployer simply needs to be configured and can then be used in the same fashion as any other Fabric script.

The .gitignore file included with Deployer marks the contents of the config folder as ignored and hence you can easily
place your own configs within it and not worry about accidentally commiting them to a public repository.

If you do want to version control your own config files or make other changes to Deployer then the recommended method
of doing so is to fork the project on Github. Doing this will allow you to freely commit your own changes while also
enabling you to pull any upstream changes to the core Deployer project. Contributing fixes or other changes back to the
upstream project is also possible and encouraged.


Configuration
=============

Projects
--------
Each YAML file within the *config/projects* directory defines a Project that consists of one or more Components to be
deployed.

A Component defines an associated source Git repository and, optionally, a list of Dockerfile paths to be built for
the Component. Each path is considered relative to the checked-out Component source. Deployer handles the process of
temporarily relocating each Dockerfile such that the Component source can be treated as the Context by Docker during
the Build process.

Consult the *config/projects/example.yml* file for further details.

Targets
-------
Each YAML file within the *config/targets* directory defines a Deployment Target.

A Deployment Target associates a set of standard Fabric environment variable values with a given name (The basename
of the Deployment Target config file).

In addition to the standard Fabric environment variables, the Deployment Target must also define an additional Fabric
environment variable named **deployment_root**. This variable determines the path on the Deployment Target systems
that will be used as a base for Deployer operations.

The Deployment Target can also define an environment variable named **branch**, the value of which indicates the
default Project branch to deploy to the Target.

Consult the *config/targets/example.yml* file for further details.

Additional Configuration
------------------------
Beyond Projects and Targets, it is possible to defined Additional Configuration in the form of YAML files placed
within the *config/* directory directly.

The values defined in an Additional Configuration can be applied during usage through the **config** Fabric task.


Usage
=====

Deployer behaves like a standard Fabric script. The following tasks are provided:

config
------
TBD

target
------
TBD

project
-------
TBD

setup
-----
TBD

build
-----
TBD

deploy
------
TBD


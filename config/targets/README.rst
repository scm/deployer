Each YAML file in this directory represents a Deployment Target.

Each Deployment Target can define standard Fabric environment variable values that are associated with that
Deployment Target.

The *all.yml* file, if it exists, is treated in a special fashion. In terms of contents, you can use it list
environment variable definitions that should be standard to all Deployment Targets. This allows you to avoid
copy-and-pasting common variable definitions into each YAML file.

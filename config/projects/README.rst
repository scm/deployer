Each YAML file in this directory represents a distinct project that consists of one or more components to be deployed.

Each component will generally consist of a git repository that includes a Dockerfile describing the container used
to run the code hosted within that git repository. Some components may include multiple Dockerfiles in which case
they will share the same codebase but possibly run different aspects of that code.

The *all.yml* file, if it exists, is treated in a special fashion. In terms of contents, you can use it to list
components that are shared between multiple projects. Components defined in *all.yml* will be available to every
project defined in addition to the components in defines for itself.

Each JSON file in this directory represents a distinct project that consists of one or more components to be deployed.

Each component will generally consist of a git repository that includes a Dockerfile describing the container used
to run the code hosted within that git repository. Some components may include multiple Dockerfiles in which case
they will share the same codebase but possibly run different aspects of that code.

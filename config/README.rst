Each YAML file in this directory can define Fabric environment variables that can be applied by calling the **config**
Fabric task.

The *all.yml* file, if it exists, will be loaded and applied automatically when the **config** Fabric task is called.
Furthermore, it is applied before any other YAML file and hence its definitions can always be overridden.

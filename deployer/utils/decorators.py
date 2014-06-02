from fabric.api import env, settings
from fabric.colors import green
from decorator import decorator
from deployer.utils.config import load

__author__ = 'adam.jorgensen.za@gmail.com'


@decorator
def targeted(f, *args, **kwargs):
    """
    Decorated function is called once for each item in env.targets. For each item
    Apply target settings to env for the duration of the call to the decorated function

    :param f:
    :param args:
    :param kwargs:
    """
    all_targets = env.targets.get('all', {})
    for target, target_data in env.targets.items():
        if target == 'all':
            continue
        if 'branch' in env:
            target_data.branch = env.branch
        with settings(**all_targets):
            with settings(**target_data):
                print(green('Targeted: %s' % target))
                f(*args, **kwargs)


def cache_config(f, config_root='config'):
    """
    Decorated Fabric task must expect an input of 1..n configs.

    The decorator takes care of processing input config names and transforming them into config data such that the
    decorated function receives 1..n tuples of (config name, config data), rather than 1..n config names.

    Additionally, the decorator will attempt to load all.yml as if it had been specified as one of the configs.
    Failure to load all.yml does not hinder the application.

    The decorator function accepts a parameter indicating the root direct to be used for locating YAML files
    associated with config names.

    :param f:
    :param config_root:
    :return:
    """
    def decorated(f, *configs):
        """

        :param f:
        :param configs:
        :return:
        """
        for config in configs:
            if config not in f.config_cache:
                f.config_cache[config] = load('%s/%s.yml' % (config_root, config))
        if 'all' not in f.config_cache:
            try:
                f.config_cache['all'] = load('%s/all.yml' % config_root)
                configs = list(configs)
                configs.append('all')
            except:
                pass
        return f(*[(config, f.config_cache[config]) for config in configs])
    f.config_cache = {}
    return decorator(decorated, f)

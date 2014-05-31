from fabric.api import env, settings
from decorator import decorator

__author__ = 'adam.jorgensen.za@gmail.com'


@decorator
def targeted(f, *args, **kwargs):
    """
    Apply target settings to env for the duration of the call to the decorated function

    :param f:
    :param args:
    :param kwargs:
    """
    with settings(**env.target):
        f(*args, **kwargs)

from fabric.utils import _AttributeDict
try:
    from simplejson import load
except ImportError:
    from json import load

__author__ = 'adam.jorgensen.za@gmail.com'


def load(path_or_file_object):
    if not callable(getattr(path_or_file_object, 'read')):
        path_or_file_object = open(path_or_file_object, 'r')
    return load(path_or_file_object, object_hook=lambda d: _AttributeDict(d))

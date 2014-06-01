import yaml
from fabric.utils import _AttributeDict

__author__ = 'adam.jorgensen.za@gmail.com'


class DeployerLoader(yaml.SafeLoader):
    """
    A custom YAML Loader class that extends SafeLoader and provides the additional feature of transforming output
    dicts into Fabric _AttributeDicts
    """

    def construct_mapping(self, node, deep=False):
        """
        Constructs a mapping from a node, returning a Fabric _AttributeDict
        """
        return _AttributeDict(super(DeployerLoader, self).construct_mapping(node, deep))


def load(path_or_file_object):
    """
    Load a YAML config file and return it as a Fabric _AttributeDict. Any nested mappings within the YAML will also be
    returned as _AttributeDicts.

    :param path_or_file_object:
    :return: _AttributeDict
    """
    if not callable(getattr(path_or_file_object, 'read')):
        path_or_file_object = open(path_or_file_object, 'r')
    return yaml.load(path_or_file_object, DeployerLoader)

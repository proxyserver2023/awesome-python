import os
import sys
import threading
from examples.monitor_file_system_events.watchdog.utils import platform
from examples.monitor_file_system_events.watchdog.utils.compat import Event


if sys.version_info[0] == 2 and platform.is_windows():
    # st_ino is not implemented in os.stat on this platform
    import win32stat
    stat = win32stat.stat
else:
    stat = os.stat


def has_attribute(ob, attribute):
    return getattr(ob, attribute, None) is not None


class UnsupportedLibc(Exception):
    pass


def load_module(module_name):
    """Imports a module given its name and returns a handle to it."""
    try:
        __import__(module_name)
    except ImportError:
        raise ImportError('No module named %s' % module_name)
    return sys.modules[module_name]


def load_class(dotted_path):
    dotted_path_split = dotted_path.split('.')

    if len(dotted_path_split) > 1:
        klass_name = dotted_path_split[-1]
        module_name = '.'.join(dotted_path_split[:-1])

        module = load_module(module_name)
        if has_attribute(module, klass_name):
            klass = getattr(module, klass_name)
            return klass
        else:
            raise AttributeError(f'Module {module_name} does not have class attribute {klass_name}')
    else:
        raise ValueError(
            f'Dotted module path {dotted_path} must contain a module_name and a classname'
        )
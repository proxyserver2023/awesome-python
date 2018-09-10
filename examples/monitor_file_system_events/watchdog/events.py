import os.path
import logging
import re

from pathtools.patterns import match_any_paths
from examples.monitor_file_system_events.watchdog.utils import has_attribute
from examples.monitor_file_system_events.watchdog.utils import unicode_paths


EVENT_TYPE_MOVED = 'moved'
EVENT_TYPE_DELETED = 'deleted'
EVENT_TYPE_CREATED = 'created'
EVENT_TYPE_MODIFIED = 'modified'


class FileSystemEvent(object):

    event_type = None
    """The type of the event as a string."""

    is_directory = False
    """True if event was emitted for a directory; False otherwise."""

    def __init__(self, src_path):
        self._src_path = src_path

    @property
    def src_path(self):
        return self._src_path


class FileSystemMovedEvent(FileSystemEvent):
    pass


# region [Imports]
import os
import configparser
import re
import subprocess
import shutil
import src.utility.gidlogger.logger_functions as glog
from glob import iglob, glob
import re
from pprint import pprint
# endregion[Imports]


# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))


# endregion [Logging]


# region [Configs]


# endregion[Configs]


# region [Global_Functions]


def commentcleaner(content):
    _string = content
    _string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", _string)  # remove all occurrences streamed comments (/*COMMENT */) from string
    _string = re.sub(re.compile("//.*?/n"), "", _string)  # remove all occurrence single-line comments (//COMMENT\n ) from string
    return _string

# endregion[Global_Functions]


class ASFile:
    def __init__(self, full_path):
        self.full_path = full_path
        self.file_name = os.path.basename(self.full_path)
        self.folder = os.path.dirname(self.full_path)
        self.as_function = None
        self.calls = []

    @property
    def content(self):
        with open(self.full_path, 'r') as _file:
            _content = _file.read()
        return _content

    def find_calls(self, function_list):
        _content = commentcleaner(self.content)
        for func in function_list:
            if func.regex.search(_content):
                self.calls.append(func)
                func.called_from.append(self)


class ASFunction:
    def __init__(self, function_name, prefix, category):
        self.function_name = function_name
        self.prefix = prefix
        self.category = category
        self.full_function_name = self.prefix + '_fnc_' + self.function_name
        self.regex = re.compile(self.full_function_name + '\W')
        self.called_from = []


if __name__ == '__main__':
    pass

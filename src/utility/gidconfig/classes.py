
# | TODO: create and 'APPDATA' handler singleton class, that creates, selects, read, and so on to all data taht is saved in appdata, with a dev_option, that redirects the env variable to cwd
# region [Imports]


# *NORMAL Imports -->

# from collections import namedtuple
# from contextlib import contextmanager
# from natsort import natsorted
# from pprint import *
# import argparse
from datetime import datetime
# import jinja2
# import lzma
import os
# import pyperclip
# import re
# import shutil
# import sys
# import time
import enum
import configparser

# *GID Imports -->
import src.utility.gidlogger.logger_functions as glog

# *QT Imports -->

# *Local Imports -->

# endregion [Imports]

__updated__ = '2020-10-03 09:41:02'

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]

# region [Constants]


# endregion [Constants]


# region [Global_Functions]


# endregion [Global_Functions]


# region [Configs]


# endregion [Configs]


# region [Extension_Registration]


# endregion [Extension_Registration]


# region [Factories]


# endregion [Factories]


# region [Main_Function]


# endregion [Main_Function]


# region [Main_Window_Widget]


# endregion [Main_Window_Widget]


# region [Paths]


# endregion [Paths]


# region [Setting_Window_Widget]


# endregion [Setting_Window_Widget]


# region [Singleton_Objects]


# endregion [Singleton_Objects]


# region [Support_Objects]
class Get(enum.Enum):
    basic = enum.auto()
    boolean = enum.auto()
    int = enum.auto()
    list = enum.auto()
    path = enum.auto()
    datetime = enum.auto()


# endregion [Support_Objects]


# region [Class_1]

class ConfigHandler(configparser.ConfigParser):
    def __init__(self, config_file=None, auto_read=True, **kwargs):
        super().__init__(**kwargs)
        self.config_file = '' if config_file is None else config_file
        self.auto_read = auto_read
        self._method_select = {Get.basic: self.get, Get.boolean: self.getboolean, Get.int: self.getint, Get.list: self.getlist, Get.path: self.get_path, Get.datetime: self.get_datetime}

        if self.auto_read is True:
            self.read(self.config_file)

    def getlist(self, section, key, delimiter=',', as_set=False):
        _raw = self.get(section, key).strip()
        if _raw.endswith(delimiter):
            _raw = _raw.rstrip(delimiter)
        if _raw.startswith(delimiter):
            _raw = _raw.lstrip(delimiter).strip()
        _out = _raw.replace(delimiter + ' ', delimiter).split(delimiter)
        if as_set is True:
            _out = set(_out)
        return _out

    def list_from_keys_only(self, section, as_set=True):
        _result = self.options(section)
        _out = []
        for line in _result:
            if line != '':
                _out.append(line)
        if as_set is True:
            _out = set(_out)
        return _out

    def get_path(self, section, key, cwd_symbol='+cwd+'):
        _raw_path = self.get(section, key)
        if cwd_symbol in _raw_path:
            _out = _raw_path.replace(cwd_symbol, os.getcwd()).replace('\\', '/')
        elif '+userdata+' in _raw_path:
            _out = _raw_path.replace('+userdata+', os.getenv('APPDATA')).replace('\\', '/')
        else:
            _out = os.path.join(_raw_path).replace('\\', '/')
        return _out

    def get_datetime(self, section, key, dtformat=None):
        _dtformat = '%Y-%m-%d %H:%M:%S' if dtformat is None else format
        _date_time_string = self.get(section, key)
        return datetime.strptime(_date_time_string, _dtformat).astimezone()

    def set_datetime(self, section, key, datetime_object, dtformat=None):
        _dtformat = '%Y-%m-%d %H:%M:%S' if dtformat is None else format
        self.set(section, key, datetime_object.strftime(_dtformat))

    def enum_get(self, section: str, option: str, typus: Get = Get.basic):
        return self._method_select.get(typus, self.get)(section, option)

    def save(self):
        with open(self.config_file, 'w') as confile:
            self.write(confile)
        self.read()

    def read(self, filenames=None):
        _configfile = self.config_file if filenames is None else filenames

        super().read(_configfile)

# endregion [Class_1]


# region [Class_2]


# endregion [Class_2]


# region [Class_3]


# endregion [Class_3]


# region [Class_4]


# endregion [Class_4]


# region [Class_5]


# endregion [Class_5]


# region [Class_6]


# endregion [Class_6]


# region [Class_7]


# endregion [Class_7]


# region [Class_8]


# endregion [Class_8]


# region [Class_9]


# endregion [Class_9]


# region [Converted_Widget_Base_1]


# endregion [Converted_Widget_Base_1]


# region [Converted_Widget_Base_2]


# endregion [Converted_Widget_Base_2]


# region [Converted_Widget_Base_3]


# endregion [Converted_Widget_Base_3]


# region [Converted_Widget_Base_4]


# endregion [Converted_Widget_Base_4]


# region [Converted_Widget_Base_5]


# endregion [Converted_Widget_Base_5]


# region [Converted_Widget_Base_6]


# endregion [Converted_Widget_Base_6]


# region [Converted_Widget_Base_7]


# endregion [Converted_Widget_Base_7]


# region [Converted_Widget_Base_8]


# endregion [Converted_Widget_Base_8]


# region [Converted_Widget_Base_9]


# endregion [Converted_Widget_Base_9]


# region [Data_1]


# endregion [Data_1]


# region [Data_2]


# endregion [Data_2]


# region [Data_3]


# endregion [Data_3]


# region [Data_4]


# endregion [Data_4]


# region [Data_5]


# endregion [Data_5]


# region [Data_6]


# endregion [Data_6]


# region [Data_7]


# endregion [Data_7]


# region [Data_8]


# endregion [Data_8]


# region [Data_9]


# endregion [Data_9]


# region [Dialog_1]


# endregion [Dialog_1]


# region [Dialog_2]


# endregion [Dialog_2]


# region [Dialog_3]


# endregion [Dialog_3]


# region [Dialog_4]


# endregion [Dialog_4]


# region [Dialog_5]


# endregion [Dialog_5]


# region [Dialog_6]


# endregion [Dialog_6]


# region [Dialog_7]


# endregion [Dialog_7]


# region [Dialog_8]


# endregion [Dialog_8]


# region [Dialog_9]


# endregion [Dialog_9]


# region [Functions_1]


# endregion [Functions_1]


# region [Functions_2]


# endregion [Functions_2]


# region [Functions_3]


# endregion [Functions_3]


# region [Functions_4]


# endregion [Functions_4]


# region [Functions_5]


# endregion [Functions_5]


# region [Functions_6]


# endregion [Functions_6]


# region [Functions_7]


# endregion [Functions_7]


# region [Functions_8]


# endregion [Functions_8]


# region [Functions_9]


# endregion [Functions_9]


# region [Model_1]


# endregion [Model_1]


# region [Model_2]


# endregion [Model_2]


# region [Model_3]


# endregion [Model_3]


# region [Model_4]


# endregion [Model_4]


# region [Model_5]


# endregion [Model_5]


# region [Model_6]


# endregion [Model_6]


# region [Model_7]


# endregion [Model_7]


# region [Model_8]


# endregion [Model_8]


# region [Model_9]


# endregion [Model_9]


# region [Widget_1]


# endregion [Widget_1]


# region [Widget_2]


# endregion [Widget_2]


# region [Widget_3]


# endregion [Widget_3]


# region [Widget_4]


# endregion [Widget_4]


# region [Widget_5]


# endregion [Widget_5]


# region [Widget_6]


# endregion [Widget_6]


# region [Widget_7]


# endregion [Widget_7]


# region [Widget_8]


# endregion [Widget_8]


# region [Widget_9]


# endregion [Widget_9]


# region [Main_Exec]
if __name__ == '__main__':
    pass


# endregion [Main_Exec]

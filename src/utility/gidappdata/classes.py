# region [Imports]


# *NORMAL Imports -->
# from collections import namedtuple
# from contextlib import contextmanager
# from jinja2 import Environment, BaseLoader
# from natsort import natsorted
from pprint import pformat
# import argparse
# import datetime
# import lzma
import os
# import pyperclip
# import re
import shutil
# import sqlite3 as sqlite
import sys
# import time

# *GID Imports -->

# from gidtools.gidstuff import RandomRGB, not_nempty, time_log


# from gidtools.gidtriumvirate import GiUserConfig, GiSolidConfig, GiDataBase, give_std_repr
import src.utility.gidlogger.logger_functions as glog

# *QT Imports -->
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtGui import QIcon, QPixmap, QColor, QBrush, QCursor
# from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QTreeWidgetItem, QListWidgetItem, QHeaderView, QButtonGroup, QTreeWidgetItemIterator, QMenu

# * Local Imports -->
from src.utility.gidconfig import Cfg, ConfigRental

# endregion [Imports]

__updated__ = '2020-10-03 09:45:37'


# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]


# region [Constants]


# endregion [Constants]


# region [Misc]


# endregion [Misc]


# region [Global_Functions]
# -------------------------------------------------------------- pathmaker -------------------------------------------------------------- #
def pathmaker(first_segment, *in_path_segments, rev=False):
    # -------------------------------------------------------------- pathmaker -------------------------------------------------------------- #
    """
    Normalizes input path or path fragments, replaces '\\\\' with '/' and combines fragments.

    Parameters
    ----------
    first_segment : str
        first path segment, if it is 'cwd' gets replaced by 'os.getcwd()'
    rev : bool, optional
        If 'True' reverts path back to Windows default, by default None

    Returns
    -------
    str
        New path from segments and normalized.
    """
    _first = os.getcwd() if first_segment == 'cwd' else first_segment
    _path = os.path.join(_first, *in_path_segments)
    _path = _path.replace('\\\\', '/')
    _path = _path.replace('\\', '/')
    if rev is True:
        _path = _path.replace('/', '\\')

    return _path.strip()

# endregion [Global_Functions]


# region [Class_1]

# endregion [Class_1]


# region [Class_2]

class AppDataStorageUtility:
    def __init__(self, author_name: str, app_name: str, dev: str = None, redirect=None):
        # sourcery skip: simplify-boolean-comparison
        self.dev = dev
        self.author_name = author_name
        self.app_name = app_name
        self.redirect = redirect
        self._manipulate_enviroment(redirect)
        self.operating_system = sys.platform
        self.general_data_folder = None if self.dev is None else os.path.split(self.dev)[0]
        self.appstorage_folder = None if self.dev is None else self.dev
        if self.dev is None:
            self.setup_app_storage_base()
            self.find_general_data_folder()

    def _manipulate_enviroment(self, redirect):
        if redirect is not None:
            os.environ['APPDATA'] = redirect

    def setup_app_storage_base(self):
        self.find_general_data_folder()
        self.appstorage_folder = pathmaker(self.general_data_folder, self.author_name, self.app_name)
        if os.path.isdir(self.appstorage_folder) is False:
            os.makedirs(self.appstorage_folder)

    def find_general_data_folder(self):
        if self.redirect is not None:
            self.general_data_folder = pathmaker(self.redirect)
        elif self.operating_system.startswith('win32'):
            self.general_data_folder = os.getenv('APPDATA')
        elif self.operating_system.startswith('linux'):
            self.general_data_folder = os.getenv('XDG_CONFIG_HOME')
        elif self.operating_system.startswith('darwin'):
            raise FileNotFoundError('currently not available for MacOS')

    def add_folder(self, folder_name, parent_folder=None):
        if parent_folder is None:
            _folder = pathmaker(self.appstorage_folder, folder_name)
        else:
            _folder = pathmaker(self.appstorage_folder, parent_folder, folder_name)
        if os.path.isdir(_folder) is False:
            os.makedirs(_folder)

    def copy_file(self, source, target_filename, folder=None, overwrite=False):
        _path = self._get_filepath(target_filename, folder)
        if os.path.isfile(_path) is False or overwrite is True:
            shutil.copyfile(source, _path)

    def _get_filepath(self, filename, folder):
        if folder is not None:
            _path = pathmaker(self.folder[folder], filename)
        else:
            _path = pathmaker(self.appstorage_folder, filename)
        return _path

    def __getitem__(self, key):
        _out = None
        if key in self.files:
            _out = self.files[key]
        elif key in self.folder:
            _out = self.folder[key]
        return _out

    @property
    def folder(self):
        _out = {}
        for dirname, dirlist, _ in os.walk(self.appstorage_folder):
            for _dir in dirlist:
                _out[_dir] = pathmaker(dirname, _dir)
        return _out

    @property
    def files(self):
        _out = {}
        for dirname, _, filelist in os.walk(self.appstorage_folder):
            for _file in filelist:
                _out[_file] = pathmaker(dirname, _file)
        return _out

    def generate_configs(self, **kwargs):
        self.add_folder('config')
        for key, value in kwargs.items():
            self.write(f'{key}.ini', value, 'config')

        ConfigRental.set_appdata(self)

    def __str__(self):
        return self.appstorage_folder

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


# region [Main_Exec]
if __name__ == '__main__':
    pass

# endregion [Main_Exec]

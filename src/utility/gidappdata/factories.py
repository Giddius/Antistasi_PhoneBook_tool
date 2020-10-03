# region [Imports]


# *NORMAL Imports -->

# from collections import namedtuple
# from contextlib import contextmanager
# from natsort import natsorted
# from pprint import *
# import argparse
# import datetime
# import jinja2
import lzma
import os
# import pyperclip
# import re
import shutil
import sys
# import time
import zipfile

# *GID Imports -->
import src.utility.gidlogger.logger_functions as glog

# *QT Imports -->

# *Local Imports -->
from src.utility.gidconfig import ConfigHandler, Cfg, ConfigRental

from src.utility.gidappdata.classes import AppDataStorageUtility
# endregion [Imports]

__updated__ = '2020-09-25 20:12:15'

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]

# region [Constants]


# endregion [Constants]


# region [Global_Functions]

def pathmaker(first_segment, *in_path_segments, rev=False):
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


# region [Configs]

def unzip(root_dir, zip_file, overwrite: bool = False):
    # sourcery skip: simplify-boolean-comparison
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        for item in zipf.namelist():
            _info = zipf.getinfo(item)
            if _info.is_dir() is True:
                if os.path.isdir(pathmaker(root_dir, item)) is False:
                    os.makedirs(pathmaker(root_dir, item))
                    log.debug("created folder '%s' because it did not exist", pathmaker(root_dir, item))
                else:
                    log.debug("folder '%s' already exists", pathmaker(root_dir, item))
            else:
                if os.path.isfile(pathmaker(root_dir, item)) is False:
                    zipf.extract(item, pathmaker(root_dir))
                    log.debug("extracted file '%s' because it didn't exist", pathmaker(root_dir, item))
                elif overwrite is True:
                    log.debug("file '%s' already exist and is overwriten because overwrite is 'True'", pathmaker(root_dir, item))
                    zipf.extract(item, pathmaker(root_dir))
                else:
                    log.debug("file '%s' is already existing and overwrite is 'False' so file was not extracted", pathmaker(root_dir, item))


# endregion [Configs]


# region [Factories]

class AppdataFactory:
    handler = None

    @classmethod
    def setup_appdata(cls, author_name: str, app_name: str, folderlist: list = None, filelist: list = None, configs: dict = None, dev=None, redirect=None):
        if cls.handler is None:
            cls.handler = AppDataStorageUtility(author_name, app_name, dev, redirect)
        if folderlist is not None:
            for _item in folderlist:
                if isinstance(_item, str):
                    cls.handler.add_folder(_item)
                elif isinstance(_item, tuple):
                    cls.handler.add_folder(_item[0], _item[1])
        if filelist is not None:
            for _item in filelist:
                if _item[0].endswith('.json'):
                    cls.handler.write_json(*_item)
                else:
                    cls.handler.write(*_item)

        if configs is not None:

            cls.handler.generate_configs(**configs)
        ConfigRental.set_appdata(cls.handler)
        return cls.handler

    @classmethod
    def archive_from_bin(cls, bin_data: str, name: str = 'user_data_archive', ext: str = 'zip'):
        _file = pathmaker(str(cls.handler), name + '.' + ext)
        with open(_file, 'wb') as archfile:
            archfile.write(bin_data)
        return _file

    @classmethod
    def unpack_archive(cls, in_archive_file, clean: bool):
        unzip(str(cls.handler), in_archive_file, False)
        if clean:
            os.remove(in_archive_file)

    @classmethod
    def setup_from_binarchive(cls, author_name: str, app_name: str, in_archive: str, dev=None, redirect=None, clean=True):

        if cls.handler is None:
            log.info("appdata, does not exist, creating from scratch")
            cls.handler = AppDataStorageUtility(author_name, app_name, dev, redirect)
            _archive = cls.archive_from_bin(in_archive)
            cls.unpack_archive(_archive, clean=clean)
            ConfigRental.set_appdata(cls.handler)
        else:
            log.info("appdata, already existing so returning existing object")

        return cls.handler

    @classmethod
    def get_handler(cls):
        if cls.handler is not None:
            return cls.handler
        else:
            raise LookupError('AppDataStorage object has to be created first via "get_handler" of this factory')

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


# endregion [Support_Objects]


# region [Class_1]


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

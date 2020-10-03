# region [Imports]


# *NORMAL Imports -->

# from collections import namedtuple
# from contextlib import contextmanager
# from natsort import natsorted
# from pprint import *
# import argparse
# import datetime
# import jinja2
# import lzma
import os
# import pyperclip
# import re
# import shutil
# import sys
# import time


# *GID Imports -->
import src.utility.gidlogger.logger_functions as glog

# *QT Imports -->

# *Local Imports -->
from src.utility.gidconfig.classes import ConfigHandler
from src.utility.gidconfig.data import Cfg

# endregion [Imports]

__updated__ = '2020-09-23 20:13:55'

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


# region [Factories]

class ConfigRental:
    UCFG = None
    SCFG = None
    DCFG = None
    appdata = None

    @classmethod
    def set_appdata(cls, appdata_object):
        cls.appdata = appdata_object

    @classmethod
    def get_config(cls, variant: Cfg, cfg_folder=None):
        if cls.appdata is None and cfg_folder is None:
            raise FileExistsError('appdata has not been set')
        _folder = cls.appdata['config'] if cfg_folder is None else cfg_folder

        if variant == Cfg.User:
            if cls.UCFG is None:
                cls.UCFG = ConfigHandler(os.path.join(_folder, 'user_config.ini').replace('\\', '/'), inline_comment_prefixes='#')
            return cls.UCFG
        elif variant == Cfg.Solid:
            if cls.SCFG is None:
                cls.SCFG = ConfigHandler(os.path.join(_folder, 'solid_config.ini').replace('\\', '/'), inline_comment_prefixes='#')
            return cls.SCFG
        elif variant == Cfg.Database:
            if cls.DCFG is None:
                cls.DCFG = ConfigHandler(os.path.join(_folder, 'db_config.ini').replace('\\', '/'), inline_comment_prefixes='#')
            return cls.DCFG
        else:
            raise KeyError('unable to rent out Config of type ' + str(variant) + ' and location ' + str(_folder))


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

# region [Imports]


# *NORMAL Imports -->

# from collections import namedtuple
# from contextlib import contextmanager

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

# endregion [Imports]

__updated__ = '2020-10-03 09:41:54'

# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion [Logging]

# region [Constants]


# endregion [Constants]


# region [Paths]

def appdata_folder():
    return os.path.join(os.getenv('APPDATA')).replace('\\', '/')

# endregion [Paths]


# region [Functions_1]

def make_user_app_folder(in_app_name):
    _path = os.path.join(appdata_folder(), in_app_name).replace('\\', '/')
    if os.path.exists(_path) is False:
        os.makedirs(_path)
    return _path
# endregion [Functions_1]


# region [Functions_2]

def create_configs(app_name, solid='default', user='default', database='default'):
    _path = make_user_app_folder(app_name)
    _solidcfg = solid_config_string_std if solid == 'default' else solid
    _usercfg = user_config_string_std if user == 'default' else user
    _databasecfg = database_config_string_std if database == 'default' else database


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

#!../venv/scripts/python
# region [Imports]

import sys
import os
import logging
from logging import handlers

# endregion [Imports]

# region [TOC]


# endregion [TOC]


# region [Constants]

__updated__ = '2020-09-22 20:50:37'


# endregion [Constants]


# region [Logging_Messages]

def imported(in_name):
    return (f"succesfully imported [-{in_name}-]")

# -------------------------------------------------------------- DEPRECATED -------------------------------------------------------------- #


def DEPRECATED(in_alternative=None):
    if in_alternative is None:
        _msg = "!!!!!!!!!DEPRECATED FUNCTION!!!!!!!!!, stop using it!"
    else:
        _msg = f"!!!!!!!!!DEPRECATED FUNCTION!!!!!!!!!, use [{in_alternative}] instead!"
    return _msg
# -------------------------------------------------------------- DEPRECATED -------------------------------------------------------------- #


# ---------------------------------------------------------------- NEWRUN ---------------------------------------------------------------- #
def NEWRUN():
    return "# " + "*-$-" * 6 + "* --> NEW_RUN <-- " + "*-?-" * 6 + "* #"

# ---------------------------------------------------------------- NEWRUN ---------------------------------------------------------------- #


def class_initiated(in_class):
    _string = repr(in_class)
    return f"finished initiating {_string} class"


def called(function_name):
    return f"{function_name} was called"


def completed(function_name):
    return f"{function_name} completed"

# endregion [Logging_Messages]


# region [Logging_Settings]

# -------------------------------------------------------------- aux_logger -------------------------------------------------------------- #
def aux_logger(in_name):
    return logging.getLogger('main').getChild(in_name)
# -------------------------------------------------------------- aux_logger -------------------------------------------------------------- #


def main_logger(in_file_name, in_level, in_back_up=2):

    _out = logging.getLogger('main')
    _out.setLevel(getattr(logging, in_level.upper()))
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(lineno)s : %(funcName)s : %(message)s')
    should_roll_over = os.path.isfile(in_file_name)
    handler = handlers.RotatingFileHandler(in_file_name, mode='a', backupCount=in_back_up)
    handler.namer = std_namer
    if should_roll_over:
        handler.doRollover()
    handler.setFormatter(formatter)
    _out.addHandler(handler)

    return _out


def main_logger_stdout(in_level, message_sep: int = 10):

    _out = logging.getLogger('main')
    _out.setLevel(getattr(logging, in_level.upper()))
    formatter = logging.Formatter(fmt='[{levelname}][{funcName}] --> ' + ' ' * message_sep + '{message}', style='{')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    _out.addHandler(handler)

    return _out

# endregion [Logging_Settings]


# region [Logging_Functions]

# --------------------------------------------------------------- std_namer -------------------------------------------------------------- #
def std_namer(name):
    _nameparts = name.split('.')
    _path, _basename = _nameparts[0].rsplit('\\', 1)
    return f'{_path}/old_logs/{_basename}_{_nameparts[2]}.{_nameparts[1]}'
# --------------------------------------------------------------- std_namer -------------------------------------------------------------- #


# ------------------------------------------------------------- log_folderer ------------------------------------------------------------- #
def log_folderer(in_log_file_name, in_main_log_folder='logs', in_old_log_subfolder='old_logs'):
    _cwd = os.getcwd()
    _path_to_old_folder = f"{_cwd}/{in_main_log_folder}/{in_old_log_subfolder}"
    if os.path.exists(_path_to_old_folder) is False:
        os.makedirs(_path_to_old_folder)
    return f"{_cwd}/{in_main_log_folder}/{in_log_file_name}.log"
# ------------------------------------------------------------- log_folderer ------------------------------------------------------------- #


# endregion [Logging_Functions]


# region [Logging_Class_1]


# endregion [Logging_Class_1]


if __name__ == "__main__":
    pass

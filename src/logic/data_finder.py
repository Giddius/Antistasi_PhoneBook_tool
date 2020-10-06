
# region [Imports]
import os
import configparser
import re
from pprint import pprint
import subprocess
import shutil
import armaclass
import src.utility.gidlogger.logger_functions as glog
from src.logic.function_classes import ASFunction, ASFile

from multiprocessing import Pool, cpu_count, Process
import json
from src.utility.misc_helpers.misc_functions import pathmaker, writejson, writeit
# endregion[Imports]


# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))


# endregion [Logging]


# region [Configs]


# endregion[Configs]


# region [Global_Functions]


# endregion[Global_Functions]


class DataFinderHolder:
    def __init__(self, as_folder):
        self.as_folder = as_folder
        self.function_hpps = []
        self.funtion_hpp_dicts = {}
        self.functions = []
        self.sqf_files = []

    def find_files(self):
        self.sqf_files = []
        self.function_hpps = []
        for dirname, _, filelist in os.walk(self.as_folder):
            for _file in filelist:
                if '.github' not in dirname:
                    if _file == "functions.hpp":
                        self.function_hpps.append(pathmaker(dirname, _file))
                    elif _file.endswith('.sqf'):
                        self.sqf_files.append(ASFile(pathmaker(dirname, _file)))

    def parse_functions_hpp(self):
        self.functions = []
        for _file in self.function_hpps:
            with open(_file, 'r') as hppfile:
                _content = hppfile.read()
            _parsed_content = armaclass.parse(_content)
            for prefix, value in _parsed_content.items():
                for category, bvalue in value.items():
                    for function_name in bvalue:
                        if function_name != 'file':
                            self.functions.append(ASFunction(function_name, prefix, category))

    def match_function_files(self):
        for _file in self.sqf_files:
            _naked_file_name = _file.file_name.replace('.sqf', '').replace('fn_', '')
            for _function in self.functions:
                if _function.full_function_name.endswith(_naked_file_name):
                    _file.as_function = _function

    def find_all_calls(self):
        for _file in self.sqf_files:
            _file.find_calls(self.functions)

    def write_dot

    def make_data(self):
        self.find_files()
        self.parse_functions_hpp()
        self.match_function_files()
        self.find_all_calls()


if __name__ == '__main__':
    a = DataFinderHolder(r"D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi")
    a.make_data()
    _out = {}
    for _file in a.sqf_files:
        _out[_file.file_name] = [f.full_function_name for f in _file.calls]
    writejson(_out, 'results.json')

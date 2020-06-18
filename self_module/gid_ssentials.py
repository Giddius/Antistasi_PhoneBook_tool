# region [Imports]

import configparser
import datetime
import functools
import logging
import lzma
import os
import pprint
import shutil
import sqlite3
import sys
from contextlib import contextmanager
from sqlite3 import Error

# endregion [Imports]


# region [Logging]




# endregion [Logging]


# region [Global_Functions]

def underscore_maker(*in_args):
    _out_string = ''
    for items in list(in_args):
        _out_string += '_' + items
    _out_string = _out_string.lstrip('_')
    return _out_string

def sepVar(in_str):
    _num = len(in_str)/2
    _amount = 20 - int(_num)
    if _amount < 0:
        _amount = _amount*-1
    _liner = '-'*_amount
    _sep = '\n#' + _liner + ' ' + in_str + ' ' + _liner + '#'
    print(_sep)

def sepI():
    _sep = '\n' + '-'*10 + '\n'
    print(_sep)


def file_name_time(var_sep='_', date_time_sep='-', box=('[', ']')):
    whole_time = str(datetime.datetime.today()).split(' ')
    today_date_temp = whole_time[0].split('-')
    today_date = var_sep.join(today_date_temp)
    today_time_temp = whole_time[1].split('.')[0].split(':')
    today_time = '' + today_time_temp[0] + var_sep + today_time_temp[1]
    if box is not None:
        _output = box[0] + today_date + date_time_sep + today_time + box[1]
    else:
        _output = today_date + date_time_sep + today_time
    return _output

def number_rename(in_path, in_round):
    _temp_path = in_path
    _temp_path = _temp_path.split('.')
    _output = _temp_path[0] + str(in_round) + '.' + _temp_path[1]
    _new_round = int(in_round) + 1
    return exist_handle(_output, _new_round, _temp_path[0] + '.' + _temp_path[1])


def exist_handle(in_path, in_round, original_path):
    if os.path.exists(in_path) is True:
        _new_path = number_rename(original_path, in_round)
    else:
        _new_path = in_path
    return _new_path


def pathmaker_decorator(func):
    def pathmaker_inner(in_file, *args, **kwargs):
        _file = pathmaker(in_file)
        return func(_file, *args, **kwargs)
    return pathmaker_inner



def readit(in_file, bindata=False, per_lines=False):

    _read_type = 'r' if bindata is False else 'rb'
    with open(in_file, _read_type) as _rfile:
        if per_lines is True:
            _output = _rfile.readlines()
        elif per_lines is False:
            _output = _rfile.read()

    return _output


def writeit(in_file, in_data, bindata=False, append=False):
    _write_type = 'w' if append is False else 'a'
    if bindata is True:
        _write_type += 'b'
    else:
        _in_data = in_data
    with open(pathmaker(in_file), _write_type) as _wfile:
        _wfile.write(_in_data)


def pathmaker(in_fr_cwd, *in_paths, rev=None):
    """makes sure all paths have '\' replaced with '/'. Takes multiple arguments and joins those while ensuring escape.

    Arguments:
        in_fr_cwd {str} -- [if this is cwd, uses os.getwd as actual first argument]
        rev {str} -- if True, reverses the escape, '/' -> '\'
    """
    _first = os.getcwd() if in_fr_cwd == 'cwd' else in_fr_cwd
    _path = os.path.join(_first, *in_paths)
    _path = _path.replace('\\', '/')
    if rev is True:
        _path = _path.replace('/', '\\')
    return _path

def utf8len(s):
    return len(s.encode('utf-8'))


def splitter(in_file, out_part='file'):
    if out_part == 'file':
        _output = os.path.basename(in_file)
    elif out_part == 'path':
        _output = os.path.dirname(in_file)
    return _output


def dir_change(*args, in_adress_home=False, ):
    """changes directory to script location or provided path.
    {*args} --> optional path pieces input
    {in_adress_home}= 'in_home_adress' if True defaults everything to location of current file and *args are ignored"""

    if in_adress_home is True:
        _path_to_home = os.path.abspath(os.path.dirname(__file__))
    else:
        _path_to_home = pathmaker(args)
    os.chdir(_path_to_home)
    print('We are now in ' + _path_to_home)


def timenamemaker(in_full_path):
    _time = str(datetime.datetime.now()).rsplit('.', maxsplit=1)[0]
    _file = splitter(in_full_path, out_part='file')
    _file_tup = os.path.splitext(_file)
    _new_file_name = _file_tup[0] + _time + _file_tup[1]
    _path = splitter(in_full_path, out_part='path')
    return pathmaker(_path, _new_file_name)

def ext_splitter(in_file, _out='file'):
    if '.' in in_file:
        _file = in_file.rsplit('.', maxsplit=1)[0]
        _ext = in_file.rsplit('.', maxsplit=1)[1]
    else:
        _file = in_file
        _ext = 'folder'
    if _out == 'file':
        _output = _file
    elif _out == 'ext':
        _output = _ext

    return _output


# endregion [Global_Functions]


# region [Class_1]



# endregion [Class_1]


class GidConfigMaster:
# region [Class_2]
    def __init__(self, config_name, config_loc):
        self.cfg_handle = configparser.ConfigParser()
        self.config_name = config_name
        self.config_location = pathmaker('cwd', 'config') if config_loc == 'default' else pathmaker(config_loc)
        self.config = pathmaker(self.config_location, self.config_name)
        self.cfg_sections = self.read_config()


    def read_config(self, in_section=None, in_key=None):
        self.cfg_handle.read(self.config)
        if in_section is None and in_key is None:
            _output = self.cfg_handle.sections()
        elif in_section is not None and in_key is None:
            _output = self.cfg_handle.options(in_section)
        elif in_section is not None and in_key is not None:
            _output = self.cfg_handle[in_section][in_key]
        return _output


    def sections_as_attributes(self):
        for section in self.cfg_sections:
            _temp_dict = {}
            for key in self.read_config(section):
                _temp_dict[key] = self.read_config(section, key)
            setattr(self, section, _temp_dict)


    @classmethod
    def from_fullpath(cls, full_path):
        cfile = pathmaker(full_path, st_revsplit='split_getfile')
        cpath = pathmaker(full_path, st_revsplit='split_getpath')
        return cls(cfile, cpath)

# -------------------------------------- modify ini Section -------------------------------------- #
    def add_or_update_option(self, in_section, option_key, in_option_value):
        self.cfg_handle.read(self.config)
        self.cfg_handle.set(in_section, option_key, in_option_value)
        self.write_to_file(self.config)
        self.sections_as_attributes()


    def config_object_clear(self):
        self.cfg_handle = ''
        self.cfg_handle = configparser.ConfigParser()


    def create_config_section(self, in_section, in_option_dict: dict):
        self.cfg_handle[in_section] = in_option_dict


    def write_to_file(self, in_config):
        with open(in_config, 'w') as new_config:
            self.cfg_handle.write(new_config)
# ------------------------------------ end modify ini Section ------------------------------------ #


    def __repr__(self):
        return f"{self.__class__.__name__} '{self.config_name}' '{self.config_location}/' '{self.cfg_sections}'"

    def __str__(self):
        return f"Class {self.__class__.__name__} using {self.config_name} located at {self.config_location}/ containing:\nsections:\n\t\t\t\t{self.cfg_sections}\n\n"

# endregion [Class_2]


class GiDataBaseMaster:
# region [Class_3]
# --------------------------------------------- init --------------------------------------------- #
    def __init__(self, in_db_name, in_db_loc, in_sql_script_loc, in_pragma=None):
        self.db_name = in_db_name
        self.db_loc = pathmaker(in_db_loc)
        self.db = pathmaker(self.db_loc, self.db_name)
        self.pragma = () if in_pragma is None else in_pragma
        self.tables = []
        self.sql_script_loc = in_sql_script_loc
        self.db_status = ''

# ------------------------------------------- end init ------------------------------------------- #

# ------------------------------------ database contextmanager ----------------------------------- #
    @contextmanager
    def opendb(self, row_factory=None):
        conn = sqlite3.connect(self.db)
        if row_factory is not None:
            conn.row_factory = row_factory
        yield conn.cursor()
        conn.commit()
        conn.close()
# ---------------------------------- end database contextmanager --------------------------------- #

# ---------------------------------------- phrase_executer --------------------------------------- #
    def phrase_executer(self, in_phrase, in_variables=None):
        with self.opendb() as conn:
            try:
                if in_variables is None:
                    conn.execute(in_phrase)
                    print(f'SQL [{in_phrase}] executed succesfully')
                else:
                    conn.execute(in_phrase, in_variables)
                    print(f'SQL [{in_phrase}]--[{in_variables}] executed succesfully')
            except Error as error:
                print(str(error) + f' - with SQL [{in_phrase}]' + '\n\n') # TODO logging needed here in the future!
# -------------------------------------- end phrase_executer ------------------------------------- #

# ---------------------------------------- query_executer ---------------------------------------- #
    def query_executer(self, in_phrase, in_variables=None, row_factory=None, mode='all'):
        # query Section
        with self.opendb(row_factory) as conn:
            try:
                if in_variables is None:
                    conn.execute(in_phrase)
                    print(f'SQL [{in_phrase}] executed succesfully')
                else:
                    conn.execute(in_phrase, in_variables)
                    print(f'SQL [{in_phrase}][{in_variables}] executed succesfully')
            except Error as error:
                print(str(error) + f' - with SQL [{in_phrase}]' + '\n\n') # TODO logging needed here in the future!

            # assign to variable Section
            if mode == 'all':
                _results = conn.fetchall()
            elif mode == 'one':
                _results = conn.fetchone()

            # output Section
            return _results
# -------------------------------------- end query_executer -------------------------------------- #

# ------------------------------------------- start_db ------------------------------------------- #
    def start_db(self, overwrite=False, backup=True):
        self.db_exist()
        if self.db_status == 'EXISTING':
            _toc = self.fetch_toc()
            _out = True

        elif self.db_status == 'NOT_EXISTING' or overwrite is True:
            self.delete_db_if_exist(backup)
            if self.pragma != ():
                self.add_pragma()
            self.create_std_init_tables()
            self.create_extra_init_tables()
            print('DB is ready') # TODO logging needed here in the future!
            self.db_exist()
            _toc = self.fetch_toc()
            _out = False
        return _out
# ----------------------------------------- end start_db ----------------------------------------- #

# ------------------------------------------- fetch_toc ------------------------------------------ #
    def fetch_toc(self):
        return self.query_executer(self.sql_init['que_toc'])
# ----------------------------------------- end fetch_toc ---------------------------------------- #

# -------------------------------------- delete_db_if_exist -------------------------------------- #
    def delete_db_if_exist(self, backup=False):
        self.db_exist()
        if self.db_status == 'EXISTING':
            if backup is True:
                _archive_path = pathmaker(self.db_parameter['main_dir'], self.db_parameter['archive_loc'])
                _db_archive_loc = pathmaker(_archive_path, self.db_name)
                if os.path.exists(_db_archive_loc) is True:
                    _round = 1
                    _db_archive_loc = number_rename(pathmaker(_db_archive_loc, self.db_name), _round)

                shutil.copy(self.db, _db_archive_loc)
                print('DB backed up')
                # TODO logging needed here in the future!

            os.remove(self.db)
            print('DB removed')
            # TODO logging needed here in the future!
# ------------------------------------ end delete_db_if_exist ------------------------------------ #

# ------------------------------------ create_std_init_tables ------------------------------------ #
    def create_std_init_tables(self):
        # create toc_tbl
        self.phrase_executer(self.sql_init['cre_toc'])
        # create tablegroup_tbl
        self.phrase_executer(self.sql_init['cre_tablegroup_tbl'])
        print('standard init tables created') # TODO logging needed here in the future!
# ---------------------------------- end create_std_init_tables ---------------------------------- #

# ----------------------------------- create_extra_init_tables ----------------------------------- #
    def create_extra_init_tables(self):
        for entries in self.read_config('sql_init_create'):
            if entries != 'main_dir' and entries != 'project_name':
                _sql = self.sql_init_create[entries]
                self.phrase_executer(_sql)
                self.insert_to_toc(entries, 'initial')
# --------------------------------- end create_extra_init_tables --------------------------------- #

# ----------------------------------------- insert_to_toc ---------------------------------------- #
    def insert_to_toc(self, tbl_name, in_tablegroup):
        _sql = self.sql_init['ins_toc']
        self.create_tablegroup(in_tablegroup)
        self.phrase_executer(_sql, (f'{tbl_name}', in_tablegroup))
# --------------------------------------- end insert_to_toc -------------------------------------- #

# --------------------------------------- create_tablegroup -------------------------------------- #
    def create_tablegroup(self, in_tablegroup):
        _sql = self.sql_init['ins_tablegroup_tbl']
        self.phrase_executer(_sql, (in_tablegroup, '-'))
# ------------------------------------- end create_tablegroup ------------------------------------ #

    def drop_table(self, in_table_name):
        _sql = 'DROP TABLE IF EXISTS "' + in_table_name + '"'
        self.phrase_executer(_sql)


    def delete_from_toc(self, in_table_name):
        _sql = 'DELETE FROM toc_tbl WHERE tbl_name='
        _sql += '"' + in_table_name + '"'
        self.phrase_executer(_sql)

# ------------------------------------------- db_exist ------------------------------------------- #
    def db_exist(self):
        self.db_status = 'EXISTING' if os.path.exists(self.db) is True else 'NOT_EXISTING'
        print(self.db_status) # TODO logging needed here in the future!
# ----------------------------------------- end db_exist ----------------------------------------- #

# -------------------------------------------- vacuum -------------------------------------------- #
    def vacuum(self):
        self.phrase_executer("VACUUM")
# ------------------------------------------ end vacuum ------------------------------------------ #

# -------------------------------------------- pragma -------------------------------------------- #
    def add_pragma(self):
        for pragma in self.pragma:
            self.phrase_executer(pragma)

# -------------------------------------------- dunder -------------------------------------------- #
    def __bool__(self):
        return os.path.exists(self.db)

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.db_name}' '{self.db_loc}'"

    def __str__(self):
        _sql_phrase = "SELECT tbl_name FROM toc_tbl"
        _output = self.querista(_sql_phrase)
        _tbl_list = '\n'.join(_output)
        return f"Class {self.__class__.__name__} with tables: {_tbl_list}"
# ------------------------------------------ end dunder ------------------------------------------ #

# endregion [Class_3]


class GidFile():
# region [Class_4]
# --------------------------------------------- init --------------------------------------------- #
    def __init__(self, in_file, bindata=False, append=False, compress=False):
        self.read_type = 'r' if bindata is False else 'rb'
        self.write_type = 'w' if append is False else 'a'
        self.compress = compress
        if bindata is True:
            self.write_type += 'b'
        self.file = pathmaker(in_file)
        self.file_name = ''
        self.file_path = ''
        self.content = b''
        self.ssplitter()
# ------------------------------------------- end init ------------------------------------------- #

# ---------------------------------- classmethod from_fileandloc --------------------------------- #
    @classmethod
    def from_fileandloc(cls, in_file_loc, in_file_name):
        _file = pathmaker(in_file_loc, in_file_name)
        return cls(_file)
# -------------------------------------- end from_fileandloc ------------------------------------- #

# -------------------------------------------- sreadit ------------------------------------------- #
    def sreadit(self, per_lines=False):
        with open(self.file, self.read_type) as _rfile:
            _temp_output = _rfile.readlines() if per_lines is True else _rfile.read()
            if self.compress is True and self.read_type == 'rb':
                _output = lzma.compress(_temp_output, check=1, preset=9)
            else:
                _output = _temp_output

            self.content = _output
# ------------------------------------------ end sreadit ----------------------------------------- #

# ------------------------------------------- swriteit ------------------------------------------- #
    def swriteit(self):
        _in_data = lzma.decompress(self.content) if self.compress is True else self.content

        with open(pathmaker(self.file), self.write_type) as _wfile:
            _wfile.write(_in_data)
# ----------------------------------------- end swriteit ----------------------------------------- #

# ------------------------------------------- ssplitter ------------------------------------------ #
    def ssplitter(self):
        self.file_name = splitter(self.file, out_part='file')
        self.file_path = splitter(self.file, out_part='path')
# ----------------------------------------- end ssplitter ---------------------------------------- #

# ---------------------------------------- stimenamemaker ---------------------------------------- #
    def stimenamemaker(self):
        return timenamemaker(self.file)
# -------------------------------------- end stimenamemaker -------------------------------------- #

# endregion [Class_4]

# region [SEPERATOR_2]
# endregion [SEPERATOR_2]
# region [SEPERATOR_1]
# endregion [SEPERATOR_1]


class GiDataBase(GidConfigMaster, GiDataBaseMaster):
# region [Class_5]
    def __init__(self, in_config_loc='default', in_pragma=None):
        GidConfigMaster.__init__(self, config_name='db_config.ini', config_loc=in_config_loc)
        self.sections_as_attributes()
        GiDataBaseMaster.__init__(self, self.db_parameter['db_name'], self.db_parameter['db_loc'], pathmaker(self.db_parameter['main_dir'], self.db_parameter['sql_script_folder']), in_pragma=in_pragma)



# endregion [Class_5]


class GiUserConfig(GidConfigMaster):
# region [Class_6]
    def __init__(self, in_config_loc='default'):
        super().__init__(config_name='user_config.ini', config_loc=in_config_loc)
        self.sections_as_attributes()

# endregion [Class_6]


class GiSolidConfig(GidConfigMaster):
# region [Class_7]
    def __init__(self, in_config_loc='default'):
        super().__init__(config_name='solid_config.ini', config_loc=in_config_loc)
        self.sections_as_attributes()

# endregion [Class_7]


# region [Class_8]






# endregion [Class_8]


class NewTable:
# region[Helper_Class]
    def __init__(self, in_table_name, in_table_group='misc'):
        self.table_group = in_table_group
        self.table_name = in_table_name
        self.collumns = []
        self.unique = []
        self.foreign_keys = []
        self.primary_key = []


    def addcol(self, in_value, in_type, pk=False, unique=False):
        if pk is True:
            self.collumns.append(in_value + ' ' + in_type + ' PRIMARY KEY')
            self.primary_key.append(in_value + ' ' + in_type)
        else:
            self.collumns.append(in_value + ' ' + in_type)

        if unique is True:
            getattr(self, 'unique').append(in_value)

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.table_name}'"

    def __radd__(self, other):
        self.foreign_keys.extend(getattr(other, 'primary_keys', default=''))
        self.collumns.extend(getattr(other, 'primary_keys', default=''))

    def __str__(self):
        _output = f'"CREATE TABLE IF NOT EXISTS {self.table_name} ('
        _output += ', '.join(self.collumns)
        _output += ', UNIQUE(' + ', '.join(self.unique) + ')'
        _output = _output.rstrip(', ') + ')"'
        return _output

# endregion[Helper_Class]

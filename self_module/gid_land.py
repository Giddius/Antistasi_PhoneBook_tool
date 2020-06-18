
# region [ModuleDocString]
""" [summary]

[extended_summary]

Returns:
    [type] -- [description]"""
# endregion [ModuleDocString]

# region [Imports]
import configparser
import datetime
import os
import shutil
import sqlite3
from contextlib import contextmanager
from sqlite3 import Error


# endregion Classes


# endregion [Imports]
# region [Constants]
DEBUG = 1
# endregion [Constants]
# region [Global_Functions]


def underscore_maker(*in_args):
    _out_string = ''
    for items in list(in_args):
        _out_string += '_' + items
    _out_string = _out_string.lstrip('_')
    return _out_string




def database_create_connect(overwrite=False, real_overwrite=False):
    _database = GiDatabasebNoble()
    _database.startup_db(backup=True)
    if overwrite is True and real_overwrite is True:
        _database.startup_db(backup=True, overwrite=True)
    return _database


def dirhomemaker(in_home_adress=None):
    """changes directory to script location or provided path.

    KEYWORD= 'in_home_adress' if not provided defaults to location of current file"""

    if in_home_adress is None:
        _path_to_home = os.path.abspath(os.path.dirname(__file__))
    else:
        _path_to_home = pathmaker(in_home_adress)
    os.chdir(_path_to_home)
    print('We are now in ' + _path_to_home)


def pathmaker(in_fr_cwd: str, *in_paths: str, st_revsplit=None):
    """makes sure all paths have '/' replaced with '/'. Takes multiple arguments and joins those while ensuring escape.
    Is also able to rev the escape and splitting file and path to the file via the 'st_revsplit' Keyword.

    Arguments:
        in_fr_cwd {str} -- [if this is cwd, uses os.getwd as actual first argument]

    st_revsplit='rev': [reverses escape]

    st_revsplit='split_getfile': [returns the file from the filepath]

    st_revsplit='split_getpath': [returns the path without the file]

    """
    _first = os.getcwd() if in_fr_cwd == 'cwd' else in_fr_cwd
    _path = os.path.join(_first, *in_paths)
    if st_revsplit == 'rev':
        _path = in_fr_cwd
        _path = _path.replace('/', '\\')
    elif st_revsplit == 'split_getname':
        _path = os.path.basename(_path)
    elif st_revsplit == 'split_getpath':
        _path = os.path.dirname(_path)
    elif st_revsplit == 'split_getpath_norm':
        _path = os.path.dirname(_path)
        _path = pathmaker(_path, st_revsplit='rev')
    else:
        _path = _path.replace('\\', '/')

    return _path


def newlinemaker(in_amount: int):
    """returns '\n' multiplied by the input"""
    return '\n'*int(in_amount)


def is_file_there(in_file, debug=1):

    _file = pathmaker(in_file, st_revsplit='split_getname')
    if debug == 2:
        _path = pathmaker(in_file, st_revsplit='split_getpath_norm')
        _fullpath = pathmaker(in_file, st_revsplit='rev')
    else:
        _path = pathmaker(in_file, st_revsplit='split_getpath')
        _fullpath = in_file
    if os.path.exists(in_file):
        print('The file [{}], located at [{}] ----> EXISTS'.format(_file, _path))
    else:
        print('The file [{}], located at [{}] ----> XXX!!!!____DOES NOT EXISTS____!!!!!XXXX'.format(_file, _path))

    print('Full Path entered----> [{}]'.format(_fullpath))


def qumaker(in_string: str, qu_type=1):
    if qu_type == 1:
        _output = "'" + in_string + "'"
    elif qu_type == 2:
        _output = '"' + in_string + '"'
    return _output


def timenamemaker(in_full_path):
    _time = str(datetime.datetime.now())
    _time = _time[0:-10]
    _time = _time.replace(' ', '_')
    _time = _time.replace(':', '-')
    _file = pathmaker(in_full_path, st_revsplit='split_getfile')
    _file_tup = os.path.splitext(_file)
    _new_file_name = _file_tup[0] + _time + _file_tup[1]
    _path = pathmaker(in_full_path, st_revsplit='split_getpath')
    return pathmaker(_path, _new_file_name)


def create_object_triumvirate():
    db_worker = GiDatabasebNoble()
    solid_worker = GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    user_worker = GiConfigRex(cfg_file='user_config.ini', cfg_sections='all')

    return [db_worker, solid_worker, user_worker]

# endregion [Global_Functions]

# region seperatorfold
# region [SEPERATOR_1]
# endregion [SEPERATOR_1]
# region [SEPERATOR_2]
# endregion [SEPERATOR_2]
# region [SEPERATOR_1]
# endregion [SEPERATOR_1]
# endregion seperatorfold


# region [Class_Name]

class GiConfigRex:

    # endregion [Class_Name]
    # region [ClassDocString]
    """ [Masterclass for handling config.ini files.]

    [is not intented to be directly used, use one of its Peasants]

    Returns:

    """
# endregion [ClassDocString]
    # region [Class_Init]

    def __init__(self, cfg_folder='default', cfg_file=None, cfg_sections=None):
        self.cfg_handle = configparser.ConfigParser()
        if cfg_folder == 'default':
            self.cfg_folder = pathmaker('cwd', 'config')
        else:
            self.cfg_folder = pathmaker(cfg_folder)

        self.cfg_file = '' if cfg_file is None else cfg_file
        self.cfg_full_loc = pathmaker(self.cfg_folder, self.cfg_file)

        if cfg_sections is None:
            self.cfg_sections = []
        elif cfg_sections == 'all':
            self.cfg_sections = self.read_config()
        else:
            self.cfg_sections = cfg_sections


        self.get_key_value_as_param()

    # endregion [Class_Init]
    # region [Class_Methods]

    @classmethod
    def from_fullpath(cls, full_path):
        cfile = pathmaker(full_path, st_revsplit='split_getfile')
        cpath = pathmaker(full_path, st_revsplit='split_getpath')
        return cls(cfile, cpath)

    def read_config(self, in_section=None, in_key=None):
        self.cfg_handle.read(self.cfg_full_loc)
        if in_section is None and in_key is None:
            _output = self.cfg_handle.sections()
        elif in_section is not None and in_key is None:
            _output = self.cfg_handle.options(in_section)
        elif in_section is not None and in_key is not None:
            _output = self.cfg_handle[in_section][in_key]
        return _output

    def get_key_value_as_param(self):
        for section in self.cfg_sections:
            _temp_dict = {}
            for key in self.read_config(section):
                _temp_dict[key] = self.read_config(section, key)
            setattr(self, section, _temp_dict)

    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return "GiMasterConfiger '{}'".format(self.cfg_folder)

    def __str__(self):
        return "Congfig processing Class 'GiMasterConfiger' '{}' '{}'".format(self.cfg_file, self.cfg_sections)

    # endregion [Class_Dunder]


# region seperatorfolder
# region [SEPERATOR_1]
# endregion [SEPERATOR_1]
# region [SEPERATOR_2]
# endregion [SEPERATOR_2]
# region [SEPERATOR_1]
# endregion [SEPERATOR_1]
# endregion seperatorfolder


# region [Class_Name]

class GiDatabasebNoble(GiConfigRex):

    # endregion [Class_Name]
    # region [ClassDocString]
    """GiDatabasebNoble [Handles SQLite DB from a solid_config.ini]

    [everything to handle DB should be contained in here, needs the solid_config.ini for most, but no other inputs needed.
    Default looks for the config in the same folder as the script and looks for the 'solid_config.ini.]

    Arguments:
        GiMasterConfiger {[type]} -- [description]

    Returns:
        [type] -- [description]

    Yields:
        [type] -- [description]"""

    # endregion [ClassDocString]
    # region [Class_Init]
    def __init__(self, cfg_folder='default', cfg_file='solid_config.ini', cfg_sections='default'):
        super().__init__(cfg_folder, cfg_file, 'all')

        self.db_name = self.db_parameter['db_name']
        self.db_full_loc = pathmaker(self.db_parameter['main_dir'], self.db_parameter['db_loc'], self.db_name)
        self.db_existance = str('ERROR:' 'not checked')
        self.db_archive_loc = pathmaker(self.db_parameter['main_dir'], self.db_parameter['archive_loc'])
        self.tables_dict = {}


    # endregion [Class_Init]
    # region [Class_Methods]

    def inspect_db_status(self):
        _output = 'EXISTING' if os.path.exists(self.db_full_loc) else 'NOT_EXISTING'
        self.db_existance = _output
        return _output


    @contextmanager
    def open_db(self, row_factory=None):
        conn = sqlite3.connect(self.db_full_loc)
        if row_factory is not None:
            conn.row_factory = row_factory
        yield conn.cursor()
        conn.commit()
        conn.close()

    def execute_phrase(self, phrase, replacement=None):
        with self.open_db() as dab:
            try:
                if replacement is None:
                    dab.execute(phrase)
                else:
                    dab.execute(phrase, replacement)
                _output = 'executed'

            except Error as error:
                print(str(error))
                _output = error
        return _output

    def startup_db(self, toc=True, table_groups=True, overwrite=False, backup=False, misc_init_tbl=None):
        self.inspect_db_status()
        if self.db_existance == 'NOT_EXISTING':
            self.con_create_db(toc, table_groups, misc_init_tbl)
        elif self.db_existance == 'EXISTING' and overwrite is True:
            if backup is True:
                print('archiving DB to: ')
                _archive_loc = timenamemaker(pathmaker(self.db_archive_loc, self.db_name))
                print(_archive_loc)
                shutil.copy(self.db_full_loc, _archive_loc)
            os.remove(self.db_full_loc)
            self.con_create_db(toc, table_groups, misc_init_tbl)
        elif self.db_existance == 'EXISTING' and overwrite is False:
            return 'DB_loaded'

    def con_create_db(self, toc=True, table_groups=True, misc_init_tbl=None):
        self.inspect_db_status()
        if self.db_existance == 'NOT_EXISTING':
            _sql_init_tbls = {}
            if toc is True:
                _sql_init_tbls['toc_tbl'] = self.sql_init['cre_toc']
            if table_groups is True:
                _sql_init_tbls['tablegroup_tbl'] = self.sql_init['cre_tablegroup_tbl']
            if misc_init_tbl is not None:
                for key, value in misc_init_tbl.items():
                    _sql_init_tbls['key'] = value
            with self.open_db() as conn:
                for key, value_ in _sql_init_tbls.items():
                    try:
                        conn.execute(value_)
                        print('executed creating: ' + key)
                        self.tables_dict[key] = ''
                    except Error as error:
                        print(str(error) + ' - with ' + key)
            self.createtable_group('misc')
            self.insert_to_toc('tablegroup_tbl', 'misc')

    def createtable_group(self, tbl_group_name):
        _sql = self.sql_init['ins_tablegroup_tbl']
        with self.open_db() as conn:
            try:
                conn.execute(_sql, (tbl_group_name, '-'))
                print('executed creating tablegroup: ' + tbl_group_name)
                self.tables_dict['tablegroup_tbl'] = tbl_group_name

            except Error as error:
                print(str(error) + ' -with create tablegroup')

    def insert_to_toc(self, tbl_name, tbl_group):
        _sql = self.sql_init['ins_toc']
        self.createtable_group(tbl_group)
        with self.open_db() as conn:
            try:
                conn.execute(_sql, (tbl_name, tbl_group))
                print('executed insert to toc:' + tbl_name)
                self.tables_dict['toc_tbl'] = (tbl_name, tbl_group)

            except Error as error:
                print(str(error) + ' - with toc insert')

    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return "GiDatabasebNoble '{}','{}','{}'".format(self.cfg_folder, self.cfg_file, self.cfg_sections)

    def __str__(self):
        return """
        DB Lord '{}' Database: ['{}'],
        Toc: '{}'
        table groups: '{}'
        """.format('GiDatabasebNoble', self.db_full_loc, self.tables_dict['toc_tbl'], self.tables_dict['tablegroup_tbl'])

    # endregion [Class_Dunder]

# region [Class_Name]


class GiDbInputKnight(GiDatabasebNoble):

    # endregion [Class_Name]
    # region [ClassDocString]
    """ [TODO]

    [TODO]

    Arguments:
         {[type]} -- [description]

    Returns:
        [type] -- [description]

    Yields:
        [type] -- [description]"""

    # endregion [ClassDocString]
    # region [Class_Init]
    def __init__(self, cfg_sections='default', table_name=None, table_collumns=None, table_group=None, fixed=None):
        if cfg_sections == 'default':
            self.cfg_sections = ['db_parameter', 'sql_input', 'sql_init']
        else:
            self.cfg_sections = []
        super().__init__(cfg_sections=self.cfg_sections)
        self.fixed = '' if fixed is None else fixed
        self.table_name = '' if table_name is None else table_name
        self.table_collumns = [] if table_collumns is None else table_collumns
        self.table_group = 'Misc' if table_group is None else table_group
        if self.fixed == '':
            self.tbl_creator()
        else:
            self.create_fixed(self.fixed)

    # endregion [Class_Init]
    # region [Class_Methods]

    @classmethod
    def from_std_tbl(cls, tablename, tablegroup, blob=False):
        _collumns = [str(tablename + '_id integer PRIMARY KEY'), str(tablename + '_name text'), str(tablename + '_content text')]
        if blob is True:
            _collumns.append(str(tablename + '_data blob'))
        _collumns.append(str('UNIQUE(' + tablename + '_name)'))
        return cls(table_name=tablename, table_collumns=_collumns, table_group=tablegroup)

    def create_fixed(self, in_put):
        _sql = in_put
        print(self.execute_phrase(_sql) + ' from :[' + in_put + ']')

    def tbl_creator(self):
        _sql = 'CREATE TABLE IF NOT EXISTS {0}({1})'.format(self.table_name, str(self.table_collumns))
        print(_sql)
        with self.open_db() as conn:
            try:
                conn.execute(_sql)
                print('executed create table: {}'.format(self.table_name))
                self.insert_to_toc(self.table_name, self.table_group)
                self.tables_dict[self.table_name] = ''

            except Error as error:
                print(str(error) + ' - with create table: {}'.format(self.table_name))

    @staticmethod
    def read_to_binary(file_full_loc):
        with open(file_full_loc, 'rb') as bif:
            return bif.read()

    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return "GiDbInputKnight '{}','{}','{}','{}'".format(self.cfg_sections, self.table_name, self.table_collumns, self.table_group)

    def __str__(self):
        return self.table_name

    # endregion [Class_Dunder]


class TocGetter(GiDatabasebNoble):

    def __init__(self):
        super().__init__()
        self.toc_dict = self.fill_toc_dict()
        print(self.toc_dict)

    def fill_toc_dict(self):
        _temp_dict = {}
        with self.open_db() as conn:
            conn.execute(self.sql_query['sel_whole_toc'])
            _raw_output = conn.fetchall()
        for rows in _raw_output:
            setattr(self, rows[0], rows[1])
            _temp_dict[rows[1]] = rows[0]
        return _temp_dict

    def update(self):
        self.toc_dict = self.fill_toc_dict()

    def list_tbl_groups(self):
        return [key for key in self.toc_dict]


    def __repr__(self):
        return "TocGetter"

    def __str__(self):
        return str(self.toc_dict)

    def __getitem__(self, key):
        try:
            return self.toc_dict[key]
        except KeyError:
            print('{} -> no such tablegroup'.format(key))

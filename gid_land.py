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
        _file = pathmaker(full_path, st_revsplit='split_getfile')
        _path = pathmaker(full_path, st_revsplit='split_getpath')
        return cls(_path, _file)

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
        if cfg_sections == 'default':
            self.cfg_sections = ['db_parameter', 'sql_init', 'sql_input', 'sql_query']
        else:
            self.cfg_sections = cfg_sections
        super().__init__(cfg_folder, cfg_file, self.cfg_sections)

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
    def open_db(self):
        conn = sqlite3.connect(self.db_full_loc)
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
        print(self.inspect_db_status())
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
            print('DB_loaded')

    def con_create_db(self, toc=True, table_groups=True, misc_init_tbl=None):
        print(self.inspect_db_status())
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
    def __init__(self, cfg_sections='default', auto_create_table=False, table_name=None, table_collumns=None, fixed=None, tbl_group=None):
        if cfg_sections == 'default':
            self.cfg_sections = ['db_parameter', 'sql_input', 'sql_init']
        else:
            self.cfg_sections = []
        super().__init__(cfg_sections=self.cfg_sections)

        self.table_name = '' if table_name is None else table_name
        self.table_collumns = [] if table_collumns is None else table_collumns
        self.table_group = '' if tbl_group is None else tbl_group
        if auto_create_table is True:
            self.general_input(self.table_name, self.table_collumns, action='create', table_group=self.table_group)

        if fixed is not None and auto_create_table is True:
            self.create_fixed(fixed)
            _temp_holder = str(self.sql_input_tnames[fixed]).split('-')
            self.table_name = _temp_holder[0]
            self.table_collumns = _temp_holder[1]
            self.table_group = _temp_holder[2]
            self.insert_to_toc(self.table_name, self.table_group)

    # endregion [Class_Init]
    # region [Class_Methods]

    @classmethod
    def from_input_create(cls, table_name, table_collumns, table_group, cfg_sections='default'):
        return cls(table_name=table_name, table_collumns=table_collumns, tbl_group=table_group, cfg_sections=cfg_sections, auto_create_table=True)

    @classmethod
    def from_fixed_create(cls, fixed_phrase):
        return cls(fixed=fixed_phrase, auto_create_table=True, cfg_sections='default')

    def create_fixed(self, in_put):
        _sql = in_put
        print(self.execute_phrase(_sql) + ' from :[' + in_put + ']')


    def input_fixed(self, fixed, *args, tablename=None):
        if tablename is None:
            _sql = self.sql_input[fixed]

        else:
            _sql = self.sql_input[fixed].format(tablename)

        _param_tuple = tuple(*args)
        self.execute_phrase(_sql, _param_tuple)

    def general_input(self, tablename: str, in_data: list, action='create', table_group='misc'):
        _table_name = str(tablename)
        _param_tuple = tuple(in_data)
        if action == 'create':
            self.tbl_creator(_table_name, _param_tuple, table_group=table_group)
        elif action == 'insert':
            _param_num = len(in_data) - 1
            self.data_inserter(_table_name, _param_num, _param_tuple)





    def tbl_creator(self, tablename, collumns, table_group='misc'):
        _sql = 'CREATE TABLE IF NOT EXISTS "{}"'.format(tablename) + str(collumns)
        print(_sql)
        with self.open_db() as conn:
            try:
                conn.execute(_sql)
                print('executed create table: {}'.format(tablename))
                self.insert_to_toc(tablename, table_group)
                self.tables_dict[tablename] = ''

            except Error as error:
                print(str(error) + ' - with create table: {}'.format(tablename))


    def data_inserter(self, tablename, coll_nums, collumns):
        _sql = 'INSERT INTO "{}" VALUES ('.format(tablename) + '?, '*coll_nums + ' ?)'

        with self.open_db() as conn:
            try:
                conn.execute(_sql, collumns)
                print('executed insert into: {}'.format(tablename))
                self.tables_dict[tablename] = collumns

            except Error as error:
                print(str(error) + ' - with insert into: {}'.format(tablename))

    @staticmethod
    def read_to_binary(file_full_loc):
        with open(file_full_loc, 'rb') as bif:
            return bif.read()

    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return "GiDbInputKnight '{}'".format(self.cfg_sections)

    def __str__(self):
        return """
        DB Input Knight '{}' Database: ['{}'],
        tables: '{}'
        """.format('GiDbInputKnight', self.db_full_loc, self.tables_dict)

    # endregion [Class_Dunder]



# region [Class_Name]

class SQLSelect(GiDatabasebNoble):

    # endregion [Class_Name]
    # region [ClassDocString]
    """$TM_CURRENT_LINE [TODO]

    [TODO]

    Arguments:
        $TM_CURRENT_LINE {[type]} -- [description]

    Returns:
        [type] -- [description]

    Yields:
        [type] -- [description]"""

    # endregion [ClassDocString]
    # region [Class_Init]
    def __init__(self, tablename: str, *collumns, allcol=False):
        super().__init__()
        self.table = tablename
        self.query_action = 'SELECT'
        self.query_collumns = '*' if allcol is True else collumns
        self.query_secarg = 'FROM'
        self.extra_clause = ''


    # endregion [Class_Init]
    # region [Class_Methods]

    def to_string(self):
        _string = str(self.query_action)
        for collumn in self.query_collumns:
            _string = _string + ' ' +  str(collumn)
        _string = _string + ' ' + self.query_secarg + ' ' + self.table + self.extra_clause
        return str(_string)

    def execute_from_string(self):
        print(self.to_string())
        print(self.extra_clause)
        with self.open_db() as conn:
            conn.execute(self.to_string())
            return conn.fetchall()





    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return 'placeholder'  #TODO

    def __str__(self):
        return 'placeholder' #TODO

    # endregion [Class_Dunder]


class SQLWhere(GiDatabasebNoble):

    # endregion [Class_Name]
    # region [ClassDocString]
    """$TM_CURRENT_LINE [TODO]

    [TODO]

    Arguments:
        $TM_CURRENT_LINE {[type]} -- [description]

    Returns:
        [type] -- [description]

    Yields:
        [type] -- [description]"""

    # endregion [ClassDocString]
    # region [Class_Init]
    def __init__(self, argument_dict: dict):
        super().__init__()
        self.query_action = 'WHERE'
        self.arguments = argument_dict




    # endregion [Class_Init]
    # region [Class_Methods]

    def to_string(self):
        _string = ' ' + str(self.query_action)
        for key, value in self.arguments.items():
            _string = _string + ' ' +  key + '=' + '"' + value + '"'

        return _string







    # endregion [Class_Methods]
    # region [Class_Dunder]

    def __repr__(self):
        return 'placeholder'  #TODO

    def __str__(self):
        return 'placeholder' #TODO

    # endregion [Class_Dunder]



if __name__ == "__main__":
    pass

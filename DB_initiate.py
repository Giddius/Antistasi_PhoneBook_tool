
# region [Imports]

import armaclass
import os
import re
import gid_land as gil

# endregion [Imports]




# region baseclass
class PhoneBookInitializer:
    """File handling for searching mission folders for sqf and hpp files"""

    def __init__(self, outfile, outputFolderName, path_to_source, function_folder):
        self.source_folder = gil.pathmaker(path_to_source)
        self.function_folder = gil.pathmaker(function_folder)
        self.outputfolder = outputFolderName
        self.outfile = outfile
        self.pybasefolder = os.path.abspath(os.path.dirname(__file__))
        self.pyoutfile = gil.pathmaker(self.outputfolder, self.outfile)
        self.fnchpp_dict = {}
        self.fnc_dict = {}
        self.sqf_dict = {}
        self.call_list = []

        self.collect_data()



    def collect_data(self):
        self.walkthefile('functions.hpp')
        self.walkthefile('sqf')
        self.getfunctions()
        self.find_calls()


    @staticmethod
    def commentcleaner(content):
        _string = content
        _string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,_string) # remove all occurrences streamed comments (/*COMMENT */) from string
        _string = re.sub(re.compile("//.*?\n" ) ,"" ,_string) # remove all occurrence single-line comments (//COMMENT\n ) from string
        return _string


    def appendoutput(self, OUTPUT):
        with open(self.pyoutfile, 'a') as f:
            f.write(OUTPUT)

    def initOutputfile(self):
        with open(self.pyoutfile, 'w') as f:
            f.write('')

    def walkthefile(self, file_type):
        if file_type == 'sqf':
            _named_dict = self.sqf_dict
        elif file_type == 'functions.hpp':
            _named_dict = self.fnchpp_dict
        _id = 0
        for roots, _directories, files in os.walk(self.source_folder):
            for file in files:
                if file_type in file:
                    _named_dict[_id] = [gil.pathmaker(roots, file), file]
                    _id += 1

    def getfunctions(self):
        fnc_id = 0
        source_functions_folder = self.function_folder
        for _key, _value in self.fnchpp_dict.items():
            parsed_cfg = armaclass.parse(self.getcontent(_value[0]))
            for prefix, rest in parsed_cfg.items():
                for folder, classlist in rest.items():
                    for function in classlist:
                        funct = prefix + '_fnc_' + function
                        functfile = 'fn_' + function + '.sqf'
                        pathfull = gil.pathmaker(source_functions_folder, folder, functfile)
                        self.fnc_dict[fnc_id] = [pathfull, functfile, funct]
                        fnc_id += 1


    def find_calls(self):
        for _sqf_key, _sqf_value in self.sqf_dict.items():
            _file_path = _sqf_value[0]
            _content = self.getcontent(_sqf_value[0])
            for _fnc_key, _fnc_value in self.fnc_dict.items():
                _fncregex = re.compile(rf'(?<=\W){_fnc_value[2]}(?=\W)', flags=re.IGNORECASE)
                if _fncregex.search(_content):
                    self.call_list.append([_sqf_key, _fnc_key])



    def getcontent(self, file):
        with open(file, 'r') as _file:
            _content = _file.read()
            return self.commentcleaner(_content)

# endregion

# region class for functions.hpp files




# endregion

# region class for sqf files








def fncintosqf(fncfunction):

    fassqf = fncfunction.replace('A3A_fnc', 'fn')
    fassqf = fassqf.replace('JN_fnc', 'fn')
    fassqf = fassqf + '.sqf'
    return fassqf





def PhoneBook_create_search_db():



    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()
    if os.path.exists(gil.pathmaker('cwd', s_config.db_parameter['db_loc'])) is False:
        os.makedirs(gil.pathmaker('cwd', s_config.db_parameter['db_loc']))
    database.startup_db(overwrite=True)

    fnchpp_knight = gil.GiDbInputKnight(table_name='fnchpp_tbl', tbl_group='Antistasi_PhoneBook_tool_tbls')
    fnchpp_knight.create_fixed(s_config.sql_input['cre_fnchpp_tbl'])
    fnchpp_knight.insert_to_toc(fnchpp_knight.table_name, fnchpp_knight.table_group)

    sqf_knight = gil.GiDbInputKnight(table_name='sqf_tbl', tbl_group='Antistasi_PhoneBook_tool_tbls')
    sqf_knight.create_fixed(s_config.sql_input['cre_sqf_tbl'])
    sqf_knight.insert_to_toc(sqf_knight.table_name, sqf_knight.table_group)

    fnc_knight = gil.GiDbInputKnight(table_name='fnc_tbl', tbl_group='Antistasi_PhoneBook_tool_tbls')
    fnc_knight.create_fixed(s_config.sql_input['cre_fnc_tbl'])
    fnc_knight.insert_to_toc(fnc_knight.table_name, fnc_knight.table_group)

    call_list_knight = gil.GiDbInputKnight(table_name='call_list_tbl', tbl_group='Antistasi_PhoneBook_tool_tbls')
    call_list_knight.create_fixed(s_config.sql_input['cre_call_list_tbl'])
    call_list_knight.insert_to_toc(call_list_knight.table_name, call_list_knight.table_group)

    WORKER = PhoneBookInitializer(u_config.from_user['output_file'], u_config.from_user['output_folder'], u_config.from_user['path_to_antistasi'], u_config.from_user['antistasi_functions_folder'])

    for _data_key, _data_value in WORKER.fnchpp_dict.items():
        _tuple_params = tuple(_data_value)
        database.execute_phrase(database.sql_input['ins_fnchpp_tbl'], _tuple_params)

    for _data_key, _data_value in WORKER.sqf_dict.items():
        _tuple_params = tuple(_data_value)

        database.execute_phrase(database.sql_input['ins_sqf_tbl'], _tuple_params)

    for _data_key, _data_value in WORKER.fnc_dict.items():
        _tuple_params = tuple(_data_value)

        database.execute_phrase(database.sql_input['ins_fnc_tbl'], _tuple_params)

    for _data_value in WORKER.call_list:
        _tuple_params = tuple(_data_value)

        database.execute_phrase(database.sql_input['ins_call_list_tbl'], _tuple_params)

    print('Antistasi_Phone_book Database initialization done')





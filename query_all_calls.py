import self_created.gid_land as gil



def get_all_calls(to_md=False, html_all=False, to_csv=False, outputfolder=None, combined=False):


    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()
    if outputfolder is None:
        _output_loc = u_config.from_user['output_folder']
    else:
        _output_loc = outputfolder
    _output_file = u_config.from_user['output_file']
    _output_full_path = gil.pathmaker(_output_loc, _output_file)

    with database.open_db() as conn:
        conn.execute(s_config.sql_query['sel_whole_call_list'])
        _results = conn.fetchall()

    if to_md is True:
        with open(_output_full_path + '.md', 'w') as md_file:
            md_file.write('# Antistasi function call list\n\n## Results\n\n')
            md_file.write('**"[-->]" stands for "calls"**\n\n')
            for rows in _results:
                md_file.write('"{}" --> "{}"\n\n'.format(rows[0], rows[1]))
            print('md file created!')

    if to_csv is True:
        with open(_output_full_path + '.csv', 'w') as csv_file:
            csv_file.write('sqf_file,function_name\n')
            for rows in _results:
                csv_file.write('"{}","{}"\n'.format(rows[0], rows[1]))

    if combined is True:
        _output = {}
        for rows in _results:
            _output[rows[0]] = ''
        for rows in _results:
            _output[rows[0]] = str(_output[rows[0]]) + ' --> ' + rows[1] + '\n'
    else:
        _output = _results


    return _output


def get_all_functions():
    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()

    with database.open_db() as conn:
        conn.execute(s_config.sql_query['sel_all_fnc'])
        _results = conn.fetchall()

    return _results

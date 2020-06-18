import self_module.gid_land as gil



def get_all_calls(as_filepath=False):


    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()
    _output = {}
    if as_filepath is True:
        _sql_phrase = s_config.sql_query['sel_whole_call_list_full']
    elif as_filepath is False:
        _sql_phrase = s_config.sql_query['sel_whole_call_list']
    with database.open_db() as conn:
        conn.execute(_sql_phrase)
        _results = conn.fetchall()

    for k, v in _results:
        _output.setdefault(v, []).append(k)

    return _output


def get_all_functions():
    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()

    with database.open_db() as conn:
        conn.execute(s_config.sql_query['sel_all_fnc'])
        _results = conn.fetchall()

    return _results

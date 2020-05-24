import gid_land as gil






def query_from_file(search_term, make_graph=False):
    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()


    with database.open_db() as conn:
        conn.execute(database.sql_query['sel_fnc_name_from_sqf'], (str(search_term), ))
        results = conn.fetchall()

    _output = results

    return _output





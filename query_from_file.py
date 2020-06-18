import self_module.gid_land as gil






def query_from_file(search_term, full_path=False):
    u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
    s_config = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    database = gil.GiDatabasebNoble()

    with database.open_db() as conn:
        if full_path is True:
            conn.execute(database.sql_query['sel_fnc_name_from_sqf_full'], (str(search_term), ))
        else:
            conn.execute(database.sql_query['sel_fnc_name_from_sqf'], (str(search_term), ))
        results = conn.fetchall()

    return results





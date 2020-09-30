# modified to new Gid module on 01.07.2020

import Gid_Generic_helpers.gid_ssentials as gis






def query_from_file(search_term, full_path=False):

    database = gis.GiDataBase()

    with database.opendb() as conn:
        if full_path is True:
            conn.execute(database.sql_query['sel_fnc_name_from_sqf_full'], (str(search_term), ))
        else:
            conn.execute(database.sql_query['sel_fnc_name_from_sqf'], (str(search_term), ))
        results = conn.fetchall()

    return results





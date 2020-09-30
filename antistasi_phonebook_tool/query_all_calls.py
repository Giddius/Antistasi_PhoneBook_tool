# modified to new Gid module on 01.07.2020

import Gid_Generic_helpers.gid_ssentials as gis



def get_all_calls(as_filepath=False):



    database = gis.GiDataBase()
    _output = {}
    if as_filepath is True:
        _sql_phrase = database.sql_query['sel_whole_call_list_full']
    elif as_filepath is False:
        _sql_phrase = database.sql_query['sel_whole_call_list']
    with database.opendb() as conn:
        conn.execute(_sql_phrase)
        _results = conn.fetchall()

    for k, v in _results:
        _output.setdefault(v, []).append(k)

    return _output


def get_all_functions():

    database = gis.GiDataBase()

    with database.opendb() as conn:
        conn.execute(database.sql_query['sel_all_fnc'])
        _results = conn.fetchall()

    return _results

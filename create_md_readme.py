import pprint
import self_module.gid_land as gil
import sqlite3

# Todo reverse it so calls to the header get shown and not what the header calls
# Todo figure out stupid relative paths

def get_callers(in_sqf_id):
    item = in_sqf_id
    with database.open_db(row_factory= sqlite3.Row) as conn:
        conn.execute(f"SELECT a.fnc_path, a.fnc_file, a.fnc_callname FROM fnc_tbl a INNER JOIN call_list_tbl b ON a.fnc_id=b.fnc_id WHERE b.sqf_id='{item}'")
        _file_list = conn.fetchall()
    fnc_dict = {}
    for row in _file_list:
        _name = row['fnc_file']
        _cname = row['fnc_callname']
        _temp_path = row['fnc_path'].split('/')
        _path = _temp_path[-2] + '/' + _temp_path[-1]
        fnc_dict[_name] = {'fnc_callname': _cname, 'fnc_path': _path}
    return fnc_dict


with open(gil.pathmaker('cwd', 'readme_test.md'), 'w') as readf:
    readf.write('')

database = gil.GiDatabasebNoble()
u_config = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
_sql_1 = "SELECT * FROM sqf_tbl"



with database.open_db(row_factory= sqlite3.Row) as conn:
    conn.execute(_sql_1)
    file_list = conn.fetchall()
sqf_dict = {}
for row in file_list:

    _name = row['sqf_file']
    _id = row['sqf_id']
    _temp_path = row['sqf_path'].split('/')
    _path = _temp_path[-2] + '/' + _temp_path[-1]
    sqf_dict[_name] = {'sqf_id': _id, 'sqf_path': _path}

with open(gil.pathmaker('cwd', 'readme_test.md'), 'a') as readf:
    for key in sqf_dict:
        readf.write(f"## [{key}]({sqf_dict[key]['sqf_path']})\n\n")
        callerdict = get_callers(sqf_dict[key]['sqf_id'])
        if callerdict != {}:
            readf.write("### calls:\n\n")
            readf.write("<details>\n  <summary>Click to expand!</summary>\n\n")
            for callers in callerdict:
                readf.write(f"- [{callers}]({callerdict[callers]['fnc_path']})\n\n")
        readf.write("</details>\n\n---\n\n---\n\n")




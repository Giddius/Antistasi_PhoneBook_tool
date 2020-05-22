import gid_land as gil





U_CONFIG = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
S_CONFIG = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
DATABASE = gil.GiDatabasebNoble()






def main():

    print('please enter the function you want to query: ', end='')
    fnc_seeked = input()
    with DATABASE.open_db() as conn:
        conn.execute(DATABASE.sql_query['sel_sqf_file_from_fnc'], (str(fnc_seeked), ))
        results = conn.fetchall()

    print('the function ["{}"] is called by the following files: \n'.format(str(fnc_seeked)))
    print('full file Path                            file name\n')
    print('------------------------------------------------------\n')
    for result in results:
        print(result)


main()

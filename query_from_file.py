import gid_land as gil





U_CONFIG = gil.GiConfigRex(cfg_folder=gil.pathmaker('cwd', 'config'), cfg_file='user_config.ini', cfg_sections='all')
S_CONFIG = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
DATABASE = gil.GiDatabasebNoble()






def main():

    print('please enter the file you want to query: ', end='')
    file_seeked = input()
    with DATABASE.open_db() as conn:
        conn.execute(DATABASE.sql_query['sel_fnc_name_from_sqf'], (str(file_seeked), ))
        results = conn.fetchall()

    print('\n\nthe file ["{}"] is called by the following files: \n'.format(str(file_seeked)))
    print('full file Path                            file name\n')
    print('------------------------------------------------------\n')
    for result in results:
        print(result)


main()

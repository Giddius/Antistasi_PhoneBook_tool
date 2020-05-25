
# Author: Giddi    https://github.com/Giddius
# configurator.py (c) 2020
# Desc: description
# Created:  2020-05-25T11:42:40.224Z
# Modified: !date!
import gid_land as gil


def read_and_new_config():
    print('please enter the full path to your Antistasi folder: ', end='')
    new_AS_folder = input()
    print('please enter the full path to the folder you want to save the output to: ', end='')
    new_output_folder = input()
    print('please enter the base name you want to use for output files [no extensions]: ', end='')
    new_output_name = input()
    with open(gil.pathmaker('cwd', 'config', 'user_config.ini'), 'w') as new_conf_f:
        new_conf_f.write("""[DEFAULT]
output_folder: %(path_to_antistasi)s
output_file: Antistasi_PhoneBook""")
        new_conf_f.write("""\n\n[from_user]
path_to_antistasi: {0}
antistasi_functions_folder: %(path_to_antistasi)s\\functions
output_folder: {1}
output_file: {2}""".format(new_AS_folder, new_output_folder, new_output_name))

if __name__ == "__main__":
    read_and_new_config()

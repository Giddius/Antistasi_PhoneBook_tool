# region [Imports]

import os
import sys

import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QTreeWidgetItem

import DB_initiate
import query_all_calls
import query_from_file
import query_from_fnc
import ui_Antistasi_PhoneBook_tool as mgui
from Antistasi_PhoneBook_tool_configuration import Configurator as cfgurator
from Antistasi_PhoneBook_tool_snippet import SnippetWindow as snippet
import PhoneBook_tool_ressources_rc
import self_created.gid_qt as giq
import self_created.gid_land as gil
import pprint

# endregion [Imports]
def conspire_the_triumvirate():
    dbi = gil.GiDatabasebNoble()
    scfg = gil.GiConfigRex(cfg_file='solid_config.ini', cfg_sections='all')
    ucfg = gil.GiConfigRex(cfg_file='user_config.ini', cfg_sections='all')
    print('The triumvirate has been created!')
    return (dbi, scfg, ucfg)




class PhoneBookMainGui(mgui.Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.triumvirate = conspire_the_triumvirate()
        self.db_tv = self.triumvirate[0]
        self.sc_tv = self.triumvirate[1]
        self.uc_tv = self.triumvirate[2]
        self.dialog_creator = giq.LittlePopuper()
        self.current_view = ''
        self.search_singlefile_radiobutton.toggle()
        self.snippets_forvsc_radiobutton.toggle()
        if self.db_tv.inspect_db_status() is 'EXISTING':
            self.fncnumber_lcdnumber.display(self.get_fnc_number())
        self.db_status_lineedit.setText(self.check_db())
        self.fontsize_spinbox.setValue(12)
        self.font_2 = QFont()
        self.font_2.setFamily("Fira Mono Medium")
        self.font_2.setPointSize(self.fontsize_spinbox.value())
        self.font_2.setBold(False)
        self.font_2.setWeight(50)
        self.font_3 = QFont()
        self.font_3.setFamily("Fira Mono Medium")
        self.font_3.setPointSize(self.fontsize_spinbox.value()-3)
        self.font_3.setBold(False)
        self.font_3.setWeight(50)
        self.actions()
        self.set_disabled()
        if self.uc_tv.from_user['changed_by_user'] == 'no':
            self.first_start()
        self.print_fileinput_lineedit.setText(self.uc_tv.from_user['output_folder'] + '/' + self.uc_tv.from_user['output_file'])
        self.db_status_lineedit.setText(self.check_db())
        if self.db_tv.inspect_db_status() == 'NOT_EXISTING':
            self.show_ask_popup()

        if self.db_tv.inspect_db_status() is 'EXISTING':
            self.fncnumber_lcdnumber.display(self.get_fnc_number())
        self.db_status_lineedit.setText(self.check_db())
    def set_disabled(self):
# region [Line_disable]

        self.line_empty_check()

    def line_empty_check(self):

        self.search_completelist_radiobutton.pressed.connect(self.search_radiobutton_check_for_button)
        self.search_singlefile_radiobutton.pressed.connect(self.search_radiobutton_check_for_button)
        self.search_completelist_radiobutton.pressed.connect(self.search_radiobutton_check_for_line)
        self.search_singlefile_radiobutton.pressed.connect(self.search_radiobutton_check_for_line)

    def search_radiobutton_check_for_button(self):
        revchecktext = '' if self.search_completelist_radiobutton.isDown() else 'Yes'
        giq.enable_button(self.search_openfiledialog_button, revchecktext)

    def search_radiobutton_check_for_line(self):
        checktext = 'Yes' if self.search_singlefile_radiobutton.isDown() else ''
        giq.enable_button(self.search_fileinput_lineedit, checktext)

# endregion [Line_disable]


    def actions(self):
# region [Actions]

        self.actionrebuild_DB.triggered.connect(self.show_ask_popup)

        self.fontsize_spinbox.valueChanged.connect(self.change_font_size)

        self.search_openfiledialog_button.pressed.connect(lambda: giq.as_filedialog(in_title='Open as Boiler File', in_dir=self.uc_tv.from_user['path_to_antistasi'], in_filter_name='sqf', in_ext='*.sqf', in_output_object=self.search_fileinput_lineedit.setText))
        self.print_openfiledialog_button.pressed.connect(lambda: giq.as_filedialog(in_type='save', in_title='Open folder', in_dir=None, in_filter_name=None, in_ext=None, in_output_object=self.print_fileinput_lineedit.setText))

        self.search_startsearch_button.pressed.connect(self.start_search)

        self.print_startprint_button.pressed.connect(self.tree_to_file_pretest)

        self.snippets_createsnippets_button.pressed.connect(self.open_snippet_window)

        self.task_createtask_button.pressed.connect(self.create_task_json)

        self.actionopen_Settings.triggered.connect(self.open_config_window)

# endregion [Actions]



    def create_task_json(self):
        _json = r"""        {
            "label": "Antistasi_PhoneBook",
            "type": "shell",
            "command": "%REPLACE_EXELOC%",
            "args": ["${fileDirname}\\${fileBasename}"],
            "group": {
                "kind": "none",
                "isDefault": true
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": true,
                "panel": "shared",
                "showReuseMessage": true,
                "clear": true
            },
            "problemMatcher": []
        },"""

        _output = _json.replace('%REPLACE_EXELOC%', gil.pathmaker('cwd', 'PhoneBook_vsc_helper.exe'))
        with open(gil.pathmaker('cwd', 'task_json.txt'), 'w') as jfile:
            jfile.write(_output)
        self.dialog_creator.information_dialog('the Json text was created as a .txt file\nplease open VS code -> F1 -> configure task, and paste the text', in_detail_message='', in_title='Json Blueprint created')


    def first_start(self):
        self.dialog_creator.information_dialog('As this is the first launch, you will have to configurate the paths.\n\n The configuration window will now open up\n afterward the Database will be created', in_detail_message='', in_title='need to set paths')
        dialog = QtWidgets.QDialog()
        dialog.ui = cfgurator(dialog, self.triumvirate)
        dialog.exec_()
        self.dialog_creator.information_dialog('Database construction will now beginn\nThis will take about 90 seconds and the programm will not react in that time', in_detail_message='', in_title='initializing Database')
        DB_initiate.PhoneBook_create_search_db()

    def open_config_window(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = cfgurator(dialog, self.triumvirate)
        dialog.exec_()

    def open_snippet_window(self):
        self.atom_snippet_text = self.atom_snippet()
        self.vsc_snippet_text = self.vsc_snippet()
        if self.snippets_forvsc_radiobutton.isChecked() is True:
            _text = self.vsc_snippet_text
        elif self.snippets_foratom_radiobutton.isChecked() is True:
            _text = self.atom_snippet_text
        dialog = QtWidgets.QDialog()
        dialog.ui = snippet(dialog, _text)
        dialog.exec_()


    def atom_snippet(self):
        _raw_output = query_all_calls.get_all_functions()
        _output = '\n'
        _output += "\n'.source.sqf':\n"
        for rows in _raw_output:
            _shorter_name = rows[0].replace('JN_fnc_', '')
            _shorter_name = _shorter_name.replace('A3A_fnc_', '')
            _withprefix = self.snippets_prefix_lineedit.text() + _shorter_name
            _output += "\n\t'{}':\n\t\t".format(rows[0])
            _output += "'prefix': '{}'\n\t\t".format(_withprefix)
            _output += "'body': '{}'\n".format(rows[0])
        return _output

    def vsc_snippet(self):
        _raw_output = query_all_calls.get_all_functions()
        _output = '\n'
        for rows in _raw_output:
            _shorter_name = rows[0].replace('JN_fnc_', '')
            _shorter_name = _shorter_name.replace('A3A_fnc_', '')
            _withprefix = self.snippets_prefix_lineedit.text() + _shorter_name
            _output += '\n{\n\t'
            _output += '"{0}": '.format('AS_function' + _shorter_name)
            _output += '\n\t{\n\t\t"prefix": '
            _output += '["{0}"],\n\t\t"body": ["{1}"],'.format(_withprefix, rows[0])
            _output += '\n\t\t"description": ""\n\t'
            _output += '}\n'
            _output += '}'
        return _output

    def tree_to_file_pretest(self):
        if self.print_csv_checkbox.isChecked() is True:
            _output_type = '.csv'
            self.tree_to_file(_output_type)
        elif self.print_md_checkbox.isChecked() is True:
            _output_type = '.md'
            self.tree_to_file(_output_type)
        else:
            self.dialog_creator.information_dialog('please select an output filetype', in_detail_message='', in_title='select output file type')

    def tree_to_file(self, output_type):

        if self.current_view == '':
            self.dialog_creator.information_dialog('Nothing to print', in_detail_message='start a search to have something to print', in_title='nothing to print')
        else:
            _method = self.current_view[0]
            _name = self.current_view[1]
            _aspath = self.current_view[2]

            if _method == 'all':
                _output = query_all_calls.get_all_calls(_aspath)
                if output_type == '.csv':
                    _text = 'called,caller\n'
                    for key, value in _output.items():
                        for a_value in value:
                            _text += f'{key},{a_value}\n'


                elif output_type == '.md':
                    _text = '# All calls\n\n'
                    for key, value in _output.items():
                        _text += f'\n## {key} is called by\n\n'
                        for a_value in value:
                            _text += f'- {a_value}\n'

                with open(self.print_fileinput_lineedit.text() + output_type, 'w') as file:
                    file.write(_text)

            elif _method == 'file':
                _raw_output = query_from_file.query_from_file(_name, _aspath)
                if output_type == '.csv':
                    _text = 'called,caller\n'
                    for rows in _raw_output:
                        _text += f'{_name},{rows[0]}\n'

                elif output_type == '.md':
                    _text = f'## {_name} is called by\n\n'
                    for rows in _raw_output:
                        _text += f'- {rows}\n'

            elif _method == 'fnc':
                _raw_output = query_from_fnc.query_from_fnc(_name, _aspath)
                if output_type == '.csv':
                    _text = 'called,caller\n'
                    for rows in _raw_output:
                        _text += f'{_name},{rows[0]}\n'

                elif output_type == '.md':
                    _text = f'## {_name} is called by\n\n'
                    for rows in _raw_output:
                        _text += f'- {rows}\n'
            self.dialog_creator.information_dialog('File created in' + self.uc_tv.from_user['output_folder'], in_detail_message='', in_title='file, created')


            with open(self.print_fileinput_lineedit.text() + '_' + _name + '_' + output_type, 'w') as file:
                file.write(_text)

    def change_font_size(self):
        self.font_2.setPointSize(self.fontsize_spinbox.value())
        self.font_3.setPointSize(self.fontsize_spinbox.value()-3)

    def check_db(self):
        _status = self.db_tv.inspect_db_status()
        return f'DB is {_status}'

    def get_fnc_number(self):
        with self.db_tv.open_db() as conn:
            conn.execute("SELECT fnc_callname FROM fnc_tbl")
            _number = conn.fetchall()
        return len(_number)

    def show_ask_popup(self):
        _message = 'Do you really want to rebuild the Database?\n this can take up to 2 minutes!\n programm will not react in that time!'
        self.dialog_creator.information_dialog(_message, in_detail_message='', in_title='rebuild the Database?', in_fnc=DB_initiate.PhoneBook_create_search_db)

    def start_search(self):

        if self.search_completelist_radiobutton.isChecked() is True:

            self.output_treewidget.clear()
            _output = query_all_calls.get_all_calls(self.options_asfilepath_checkbox.isChecked())

            for key, value in _output.items():
                _namel = str(key)

                _namel = QTreeWidgetItem(self.output_treewidget)
                _namel.setText(0, key)
                _namel.setExpanded(True)
                _namel.setFont(0, self.font_2)
                for values in value:
                    _namev = str(values)

                    _namev = QTreeWidgetItem(_namel)
                    _namev.setText(0, values)
                    _namev.setFont(0, self.font_3)

                _empty =QTreeWidgetItem(self.output_treewidget)
                _empty.setText(0, '')
                _empty =QTreeWidgetItem(self.output_treewidget)
                _empty.setText(0, '')
            self.current_view = ('all', 'all', self.options_asfilepath_checkbox.isChecked())

        elif self.search_singlefile_radiobutton.isChecked() is True:
            if self.search_fileinput_lineedit.text() == '':
                self.dialog_creator.error_dialog('you need to input an function name or the name of an .sqf file!', '')
            else:
                self.output_treewidget.clear()
                _name = gil.pathmaker(self.search_fileinput_lineedit.text())

                _cleaned_name = gil.pathmaker(_name, st_revsplit='split_getname')


                print(_cleaned_name)
                if '.sqf' in str(self.search_fileinput_lineedit.text()):
                    _raw_output = query_from_file.query_from_file(_cleaned_name, full_path=self.options_asfilepath_checkbox.isChecked())
                    _mainitem = _cleaned_name
                    _mainitem = QTreeWidgetItem(self.output_treewidget)
                    _mainitem.setText(0, _cleaned_name)
                    _mainitem.setExpanded(True)
                    _mainitem.setFont(0, self.font_2)
                    for rows in _raw_output:
                        _sec_item = str(rows[0])
                        _sec_item = QTreeWidgetItem(_mainitem)
                        _sec_item.setText(0, rows[0])
                        _sec_item.setExpanded(True)
                    self.current_view = ('file', _cleaned_name, self.options_asfilepath_checkbox.isChecked())

                elif 'A3A' in str(self.search_fileinput_lineedit.text()):
                    _raw_output = query_from_fnc.query_from_fnc(_cleaned_name, full_path=self.options_asfilepath_checkbox.isChecked())
                    _mainitem = _cleaned_name
                    _mainitem = QTreeWidgetItem(self.output_treewidget)
                    _mainitem.setText(0, _cleaned_name)
                    _mainitem.setExpanded(True)
                    _mainitem.setFont(0, self.font_2)
                    for rows in _raw_output:
                        _sec_item = str(rows[0])
                        _sec_item = QTreeWidgetItem(_mainitem)
                        _sec_item.setText(0, rows[0])
                        _sec_item.setExpanded(True)
                    self.current_view = ('fnc', _cleaned_name, self.options_asfilepath_checkbox.isChecked())
                else:
                    self.dialog_creator.error_dialog('what?', '')
                    self.current_view = ''




# region [Main]

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PhoneBookMainGui(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

# endregion [Main]

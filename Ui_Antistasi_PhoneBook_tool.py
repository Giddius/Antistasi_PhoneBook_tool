"""
this program finds all Antistasi functions and .sqf files and lists calls from those files to the functions;
it can search the result by file name and function name, also provided is a dump all, dump all to file and snippet creator from all functions;
it is wrapped in an UI and uses an sqlite DB as storage.
"""
# Author: Giddi    https://github.com/Giddius
# Ui_Antistasi_PhoneBook_tool.py 2020
# Desc: description
# Created:  2020-05-26T08:39:04.567Z
# Modified: 2020-05-26T10:55:02.398Z


import pprint
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import DB_initiate
import self_created.gid_land as gil
import query_all_calls
import query_from_file
import query_from_fnc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 180, 731, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Output_window = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Semibold")
        font.setKerning(False)
        self.Output_window.setFont(font)
        self.Output_window.setReadOnly(True)
        self.Output_window.setObjectName("Output_window")
        self.horizontalLayout.addWidget(self.Output_window)
        self.Snippett_window = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Semibold")
        font.setKerning(False)
        font.setPointSize(7)
        self.Snippett_window.setFont(font)
        self.Snippett_window.setReadOnly(True)
        self.Snippett_window.setObjectName("Snippett_window")
        self.horizontalLayout.addWidget(self.Snippett_window)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 731, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.input_search_term = QtWidgets.QLineEdit(self.tab)
        self.input_search_term.setGeometry(QtCore.QRect(130, 20, 341, 23))
        self.input_search_term.setObjectName("input_search_term")
        self.start_query = QtWidgets.QPushButton(self.tab)
        self.start_query.setGeometry(QtCore.QRect(280, 60, 121, 27))
        self.start_query.setObjectName("start_query")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 20))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(480, 10, 235, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.output_full_path_check = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_full_path_check.setFont(font)
        self.output_full_path_check.setObjectName("output_full_path_check")
        self.verticalLayout_3.addWidget(self.output_full_path_check)
        self.create_header_check = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.create_header_check.setObjectName("create_header_check")
        self.create_header_check.setEnabled(False)
        self.verticalLayout_3.addWidget(self.create_header_check)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.create_vscsnippet_check = QtWidgets.QCheckBox(self.tab_2)
        self.create_vscsnippet_check.setGeometry(QtCore.QRect(470, 10, 181, 23))
        self.create_vscsnippet_check.setObjectName("create_vscsnippet_check")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 162, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_md_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.create_md_check.setObjectName("create_md_check")
        self.verticalLayout.addWidget(self.create_md_check)
        self.create_csv_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.create_csv_check.setObjectName("create_csv_check")
        self.verticalLayout.addWidget(self.create_csv_check)
        self.create_html_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.create_html_check.setEnabled(False)
        self.create_html_check.setObjectName("create_html_check")
        self.verticalLayout.addWidget(self.create_html_check)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(470, 40, 251, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_snippet_prefix = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.input_snippet_prefix.setObjectName("input_snippet_prefix")
        self.input_snippet_prefix.setText('asf_')
        self.horizontalLayout_2.addWidget(self.input_snippet_prefix)
        self.clipboard_button = QtWidgets.QPushButton(self.tab_2)
        self.clipboard_button.setGeometry(QtCore.QRect(580, 110, 144, 25))
        self.clipboard_button.setObjectName("clipboard_button")
        self.start_query_all = QtWidgets.QPushButton(self.tab_2)
        self.start_query_all.setGeometry(QtCore.QRect(260, 10, 160, 25))
        self.start_query_all.setObjectName("start_query_all")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 79, 241, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")


        self.output_combined_check = QtWidgets.QCheckBox(self.tab_2)
        self.output_combined_check.setGeometry(QtCore.QRect(260, 40, 181, 23))
        self.output_combined_check.setObjectName("output_combined_check")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menurebuild = QtWidgets.QMenu(self.menubar)
        self.menurebuild.setObjectName("menurebuild")
        MainWindow.setMenuBar(self.menubar)
        self.actionrebuild_Database = QtWidgets.QAction(MainWindow)
        self.actionrebuild_Database.setObjectName("actionrebuild_Database")
        self.menurebuild.addAction(self.actionrebuild_Database)
        self.menubar.addAction(self.menurebuild.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.start_query.pressed.connect(self.pressed_search)
        self.start_query_all.pressed.connect(self.pressed_search_all)
        self.menurebuild.triggered[QtWidgets.QAction].connect(self.show_ask_popup)
        self.clipboard_button.pressed.connect(self.copy_snippets)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antistasi PhoneBook Tool"))
        self.start_query.setText(_translate("MainWindow", "find callers"))
        self.label.setText(_translate("MainWindow", "Search term:"))
        self.output_full_path_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.output_full_path_check.setText(_translate("MainWindow", "Results as full file path?"))
        self.create_header_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.create_header_check.setText(_translate("MainWindow", "create header for file?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.create_vscsnippet_check.setText(_translate("MainWindow", "create VSC snippets"))
        self.create_md_check.setText(_translate("MainWindow", "create .md"))
        self.create_csv_check.setText(_translate("MainWindow", "create .csv"))
        self.create_html_check.setText(_translate("MainWindow", "create .html"))
        self.label_2.setText(_translate("MainWindow", "snippet prefix:"))
        self.clipboard_button.setText(_translate("MainWindow", "copy to clipboard"))
        self.start_query_all.setText(_translate("MainWindow", "show every function"))

        self.output_combined_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.output_combined_check.setText(_translate("MainWindow", "combine caller?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menurebuild.setTitle(_translate("MainWindow", "rebuild"))
        self.actionrebuild_Database.setText(_translate("MainWindow", "rebuild Database"))

    def show_config_popup(self):
        self.sub = Ui_Dialog()
        self.sub.setupUi(MainWindow)

    def copy_snippets(self):
        self.Snippett_window.selectAll()
        self.Snippett_window.copy()

    def show_ask_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('rebuild the Database?')
        msg.setText('Do you really want to rebuild the Database?\n this can take up to 2 minutes!\n programm will not react in that time!')
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.process_ask_popup)
        x = msg.exec()


    def process_ask_popup(self, i):

        if i.text() == 'OK':
            DB_initiate.PhoneBook_create_search_db()

    def show_error_popup(self, IN_content):
        msg = QMessageBox()
        msg.setWindowTitle('ERROR!')
        msg.setText(IN_content)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)

    def pressed_search_all(self):
        _raw_output = query_all_calls.get_all_calls(to_md=self.create_md_check.isChecked(), to_csv=self.create_csv_check.isChecked(), combined=self.output_combined_check.isChecked())
        _output = '\n'
        if self.output_combined_check.isChecked() is False:
            for rows in _raw_output:
                _output += '{}  -->  {}\n\n'.format(rows[0], rows[1])
        elif self.output_combined_check.isChecked() is True:
            for key, value in _raw_output.items():
                _output += '{2}\n{0}:\n{2}\n{1}\n\n'.format(key, value, '-'*(len(key)+int((len(key)/3))))
        self.Output_window.setText(_output)
        if self.create_vscsnippet_check.isChecked() is True:
            self.create_vsc_snippets()


    def create_vsc_snippets(self):
        _raw_output = query_all_calls.get_all_functions()
        _output = '\n'
        for rows in _raw_output:
            _shorter_name = rows[0].replace('JN_fnc_', '')
            _shorter_name = _shorter_name.replace('A3A_fnc_', '')
            _output += '\n{\n\t'
            _output += '"{0}": '.format('AS_function' + _shorter_name)
            _output += '\n\t{\n\t\t"prefix": '
            _output += '["{0}"],\n\t\t"body": ["{1}"],'.format(self.input_snippet_prefix.text() + _shorter_name, rows[0])
            _output += '\n\t\t"description": ""\n\t'
            _output += '}\n'
            _output += '}'
        self.Snippett_window.setText(_output)


    def pressed_search(self):
        if str(self.input_search_term.text()) == '':
            self.show_error_popup('you need to input an function name or the name of an .sqf file!')

        if '.sqf' in str(self.input_search_term.text()):
            _raw_output = query_from_file.query_from_file(str(self.input_search_term.text()), full_path=self.output_full_path_check.isChecked())
            _output = '[{}] is called as a function, by the following files:\n\n'.format(str(self.input_search_term.text()))
            for rows in _raw_output:
                _output += '<-- {}\n'.format(rows[0])
            self.Output_window.setText(_output)

        elif 'A3A' in str(self.input_search_term.text()):
            _raw_output = query_from_fnc.query_from_fnc(str(self.input_search_term.text()), full_path=self.output_full_path_check.isChecked())
            _output = '[{}] is called by the following files:\n\n'.format(str(self.input_search_term.text()))
            for rows in _raw_output:
                _output += '<-- {}\n'.format(rows[0])
            self.Output_window.setText(_output)
        else:
            self.Output_window.setText('what?')







if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

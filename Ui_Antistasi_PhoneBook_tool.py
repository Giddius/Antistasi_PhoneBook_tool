# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\ui\Antistasi_PhoneBook_tool.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import query_all_calls
import query_from_fnc
import query_from_file
import DB_initiate
import gid_land as gil



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 931, 571))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Output_window = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.Output_window.setReadOnly(True)
        self.Output_window.setObjectName("Output_window")
        self.horizontalLayout.addWidget(self.Output_window)
        self.graphicsView = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 931, 171))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.input_search_term = QtWidgets.QLineEdit(self.tab)
        self.input_search_term.setGeometry(QtCore.QRect(130, 20, 341, 23))
        self.input_search_term.setObjectName("input_search_term")
        self.start_query = QtWidgets.QPushButton(self.tab)
        self.start_query.setGeometry(QtCore.QRect(280, 60, 121, 27))
        self.start_query.setObjectName("start_query")
        self.output_diagram_check = QtWidgets.QCheckBox(self.tab)
        self.output_diagram_check.setEnabled(False)
        self.output_diagram_check.setGeometry(QtCore.QRect(420, 60, 191, 22))
        self.output_diagram_check.setObjectName("output_diagram_check")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 20))
        self.label.setObjectName("label")
        self.output_full_path_check = QtWidgets.QCheckBox(self.tab)
        self.output_full_path_check.setGeometry(QtCore.QRect(480, 20, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_full_path_check.setFont(font)
        self.output_full_path_check.setObjectName("output_full_path_check")
        self.create_header_check = QtWidgets.QCheckBox(self.tab)
        self.create_header_check.setGeometry(QtCore.QRect(420, 90, 231, 22))
        self.create_header_check.setObjectName("create_header_check")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.start_query_all = QtWidgets.QPushButton(self.tab_2)
        self.start_query_all.setGeometry(QtCore.QRect(210, 20, 161, 27))
        self.start_query_all.setObjectName("start_query_all")
        self.create_md_check = QtWidgets.QCheckBox(self.tab_2)
        self.create_md_check.setGeometry(QtCore.QRect(410, 20, 131, 23))
        self.create_md_check.setObjectName("create_md_check")
        self.create_csv_check = QtWidgets.QCheckBox(self.tab_2)
        self.create_csv_check.setGeometry(QtCore.QRect(410, 60, 111, 23))
        self.create_csv_check.setObjectName("create_csv_check")
        self.create_html_check = QtWidgets.QCheckBox(self.tab_2)
        self.create_html_check.setEnabled(False)
        self.create_html_check.setGeometry(QtCore.QRect(410, 100, 121, 23))
        self.create_html_check.setObjectName("create_html_check")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        self.menurebuild = QtWidgets.QMenu(self.menubar)
        self.menurebuild.setObjectName("menurebuild")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_user_config = QtWidgets.QAction(MainWindow)
        self.actionopen_user_config.setObjectName("actionopen_user_config")
        self.actionrebuild_Database = QtWidgets.QAction(MainWindow)
        self.actionrebuild_Database.setObjectName("actionrebuild_Database")
        self.menusettings.addAction(self.actionopen_user_config)
        self.menurebuild.addAction(self.actionrebuild_Database)
        self.menubar.addAction(self.menusettings.menuAction())
        self.menubar.addAction(self.menurebuild.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.start_query.pressed.connect(self.pressed_search)
        self.start_query_all.pressed.connect(self.pressed_search_all)
        self.menurebuild.triggered[QtWidgets.QAction].connect(self.show_ask_popup)
        self.actionopen_user_config.triggered.connect(self.show_config_popup)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antistasi PhoneBook Tool"))
        self.start_query.setText(_translate("MainWindow", "find callers"))
        self.output_diagram_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.output_diagram_check.setText(_translate("MainWindow", "create diagram?"))
        self.label.setText(_translate("MainWindow", "Search term:"))
        self.output_full_path_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.output_full_path_check.setText(_translate("MainWindow", "Results as full file path?"))
        self.create_header_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.create_header_check.setText(_translate("MainWindow", "create header for file?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.start_query_all.setText(_translate("MainWindow", "show every function"))
        self.create_md_check.setText(_translate("MainWindow", "create .md"))
        self.create_csv_check.setText(_translate("MainWindow", "create .csv"))
        self.create_html_check.setText(_translate("MainWindow", "create .html"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menusettings.setTitle(_translate("MainWindow", "settings"))
        self.menurebuild.setTitle(_translate("MainWindow", "rebuild"))
        self.actionopen_user_config.setText(_translate("MainWindow", "open user config"))
        self.actionrebuild_Database.setText(_translate("MainWindow", "rebuild Database"))

    def show_config_popup(self):
        self.sub = Ui_Dialog()
        self.sub.setupUi(MainWindow)


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
        _raw_output = query_all_calls.get_all_calls(to_md=self.create_md_check.isChecked(), to_csv=self.create_csv_check.isChecked())
        _output = 'all files and the functions they call:\n\n----------------------------------------\n\n'
        for rows in _raw_output:
            _output += '{}  -->  {}\n\n'.format(rows[0], rows[1])
        self.Output_window.setText(_output)


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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 371, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.line_config_ASfolder = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_config_ASfolder.setObjectName("line_config_ASfolder")
        self.line_config_ASfolder.setText(self.get_config_values('path_to_antistasi'))
        self.gridLayout.addWidget(self.line_config_ASfolder, 0, 1, 1, 1)
        self.line_config_Outputfolder = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_config_Outputfolder.setObjectName("line_config_Outputfolder")
        self.line_config_Outputfolder.setText(self.get_config_values('output_folder'))
        self.gridLayout.addWidget(self.line_config_Outputfolder, 1, 1, 1, 1)
        self.line_config_Outputname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_config_Outputname.setObjectName("line_config_Outputname")
        self.line_config_Outputname.setText(self.get_config_values('output_file'))
        self.gridLayout.addWidget(self.line_config_Outputname, 2, 1, 1, 1)
        self.select_ASfolder_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_ASfolder_button.setObjectName("select_ASfolder_button")
        self.gridLayout.addWidget(self.select_ASfolder_button, 0, 2, 1, 1)
        self.select_Output_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_Output_button.setObjectName("select_Output_button")
        self.gridLayout.addWidget(self.select_Output_button, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Output folder:"))
        self.label_2.setText(_translate("Dialog", "Antistasi folder:"))
        self.label.setText(_translate("Dialog", "Output name:"))
        self.select_ASfolder_button.setText(_translate("Dialog", "select"))
        self.select_Output_button.setText(_translate("Dialog", "select"))

    def get_config_values(self, field):
        u_configer = gil.GiConfigRex(cfg_file='user_config.ini', cfg_sections='all')
        return u_configer.read_config('from_user', field)

    def read_and_new_config(self):
        new_AS_folder = str(self.line_config_ASfolder.text())
        new_output_folder = str(self.line_config_Outputfolder.text())
        new_output_name = str(self.line_config_Outputname.text())
        with open(gil.pathmaker('cwd', 'config', 'user_config.ini'), 'w') as new_conf_f:
            new_conf_f.write("""[DEFAULT]
output_folder: %(path_to_antistasi)s
output_file: Antistasi_PhoneBook""")
            new_conf_f.write("""[from_user]
path_to_antistasi: {0}
antistasi_functions_folder: %(path_to_antistasi)s\functions
output_folder: {1}
output_file: {2}""".format(new_AS_folder, new_output_folder, new_output_name))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

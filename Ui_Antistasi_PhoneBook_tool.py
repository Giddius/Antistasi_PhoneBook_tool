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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_search_term = QtWidgets.QLineEdit(self.centralwidget)
        self.input_search_term.setGeometry(QtCore.QRect(210, 20, 341, 23))
        self.input_search_term.setObjectName("input_search_term")
        self.Output_window = QtWidgets.QTextEdit(self.centralwidget)
        self.Output_window.setGeometry(QtCore.QRect(40, 220, 691, 321))
        self.Output_window.setReadOnly(True)
        self.Output_window.setObjectName("Output_window")
        self.start_query = QtWidgets.QPushButton(self.centralwidget)
        self.start_query.setGeometry(QtCore.QRect(320, 110, 121, 27))
        self.start_query.setObjectName("start_query")
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
        self.actionset_paths = QtWidgets.QAction(MainWindow)
        self.actionset_paths.setObjectName("actionset_paths")
        self.actionrebuild_Database = QtWidgets.QAction(MainWindow)
        self.actionrebuild_Database.setObjectName("actionrebuild_Database")
        self.menusettings.addAction(self.actionopen_user_config)
        self.menusettings.addAction(self.actionset_paths)
        self.menurebuild.addAction(self.actionrebuild_Database)
        self.menubar.addAction(self.menusettings.menuAction())
        self.menubar.addAction(self.menurebuild.menuAction())

        self.retranslateUi(MainWindow)
        self.start_query.pressed.connect(self.pressed_search)
        self.menurebuild.triggered[QtWidgets.QAction].connect(self.show_ask_popup)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antistasi PhoneBook Tool"))
        self.start_query.setText(_translate("MainWindow", "find callers"))
        self.menusettings.setTitle(_translate("MainWindow", "settings"))
        self.menurebuild.setTitle(_translate("MainWindow", "rebuild"))
        self.actionopen_user_config.setText(_translate("MainWindow", "open user config"))
        self.actionset_paths.setText(_translate("MainWindow", "set paths"))
        self.actionrebuild_Database.setText(_translate("MainWindow", "rebuild Database"))

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

        else:
            pass

    def show_error_popup(self, IN_content):
        msg = QMessageBox()
        msg.setWindowTitle('ERROR!')
        msg.setText(IN_content)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)


    def pressed_search(self):
        if str(self.input_search_term.text()) == '':
            self.show_error_popup('you need to input an function name or the name of an .sqf file!')

        if '.sqf' in str(self.input_search_term.text()):
            _raw_output = query_from_file.query_from_file(str(self.input_search_term.text()))
            _output = '[{}] is called as a function, by the following files:\n\n'.format(str(self.input_search_term.text()))
            for rows in _raw_output:
                _output += '\t <-- {}\n'.format(rows[0])
            self.Output_window.setText(_output)

        elif 'A3A' in str(self.input_search_term.text()):
            _raw_output = query_from_fnc.query_from_fnc(str(self.input_search_term.text()))
            _output = '[{}] is called by the following files:\n\n'.format(str(self.input_search_term.text()))
            for rows in _raw_output:
                _output += '\t <-- {}\n'.format(rows[0])
            self.Output_window.setText(_output)
        else:
            self.Output_window.setText('what?')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

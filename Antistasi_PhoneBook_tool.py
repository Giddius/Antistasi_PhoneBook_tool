# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\UI\Antistasi_PhoneBook_tool.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        font.setPointSize(10)
        font.setKerning(False)
        self.Output_window.setFont(font)
        self.Output_window.setReadOnly(True)
        self.Output_window.setObjectName("Output_window")
        self.horizontalLayout.addWidget(self.Output_window)
        self.Snippett_window = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
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
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.output_full_path_check.setFont(font)
        self.output_full_path_check.setObjectName("output_full_path_check")
        self.verticalLayout_3.addWidget(self.output_full_path_check)
        self.create_header_check = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.create_header_check.setObjectName("create_header_check")
        self.verticalLayout_3.addWidget(self.create_header_check)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.create_vscsnippet_check = QtWidgets.QCheckBox(self.tab_2)
        self.create_vscsnippet_check.setGeometry(QtCore.QRect(390, 90, 181, 23))
        self.create_vscsnippet_check.setObjectName("create_vscsnippet_check")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 162, 83))
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
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.input_snippet_prefix.setFont(font)
        self.input_snippet_prefix.setPlaceholderText("")
        self.input_snippet_prefix.setObjectName("input_snippet_prefix")
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
        self.input_output_folder = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_output_folder.sizePolicy().hasHeightForWidth())
        self.input_output_folder.setSizePolicy(sizePolicy)
        self.input_output_folder.setReadOnly(True)
        self.input_output_folder.setObjectName("input_output_folder")
        self.horizontalLayout_3.addWidget(self.input_output_folder)
        self.get_outputpath_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(8)
        self.get_outputpath_button.setFont(font)
        self.get_outputpath_button.setObjectName("get_outputpath_button")
        self.horizontalLayout_3.addWidget(self.get_outputpath_button)
        self.output_combined_check = QtWidgets.QCheckBox(self.tab_2)
        self.output_combined_check.setGeometry(QtCore.QRect(260, 40, 181, 23))
        self.output_combined_check.setObjectName("output_combined_check")
        self.create_vscsnippet_check_2 = QtWidgets.QCheckBox(self.tab_2)
        self.create_vscsnippet_check_2.setGeometry(QtCore.QRect(390, 110, 181, 23))
        self.create_vscsnippet_check_2.setObjectName("create_vscsnippet_check_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.input_snippet_prefix.setToolTip(_translate("MainWindow", "-> e.g.[prefix]flagaction"))
        self.clipboard_button.setText(_translate("MainWindow", "copy to clipboard"))
        self.start_query_all.setText(_translate("MainWindow", "show every function"))
        self.get_outputpath_button.setText(_translate("MainWindow", "folder"))
        self.output_combined_check.setToolTip(_translate("MainWindow", "output file location and name must be specified in the config"))
        self.output_combined_check.setText(_translate("MainWindow", "combine caller?"))
        self.create_vscsnippet_check_2.setText(_translate("MainWindow", "create Atom snippets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menurebuild.setTitle(_translate("MainWindow", "rebuild"))
        self.actionrebuild_Database.setText(_translate("MainWindow", "rebuild Database"))

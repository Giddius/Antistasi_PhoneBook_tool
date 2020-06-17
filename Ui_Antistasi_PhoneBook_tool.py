# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Antistasi_PhoneBook_tool\UI\Antistasi_PhoneBook_tool.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(250, 1000))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.search_singlefile_radiobutton = QtWidgets.QRadioButton(self.groupBox_2)
        self.search_singlefile_radiobutton.setObjectName("search_singlefile_radiobutton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.search_singlefile_radiobutton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_fileinput_lineedit = DragDropLineEdit(self.groupBox_2)
        self.search_fileinput_lineedit.setObjectName("search_fileinput_lineedit")
        self.horizontalLayout_2.addWidget(self.search_fileinput_lineedit)
        self.search_openfiledialog_button = QtWidgets.QToolButton(self.groupBox_2)
        self.search_openfiledialog_button.setObjectName("search_openfiledialog_button")
        self.horizontalLayout_2.addWidget(self.search_openfiledialog_button)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.search_completelist_radiobutton = QtWidgets.QRadioButton(self.groupBox_2)
        self.search_completelist_radiobutton.setObjectName("search_completelist_radiobutton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.search_completelist_radiobutton)
        self.search_startsearch_button = QtWidgets.QPushButton(self.groupBox_2)
        self.search_startsearch_button.setObjectName("search_startsearch_button")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.search_startsearch_button)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.print_fileinput_lineedit = DragDropLineEdit(self.groupBox_3)
        self.print_fileinput_lineedit.setBaseSize(QtCore.QSize(0, 0))
        self.print_fileinput_lineedit.setObjectName("print_fileinput_lineedit")
        self.gridLayout.addWidget(self.print_fileinput_lineedit, 0, 0, 1, 1)
        self.print_openfiledialog_button = QtWidgets.QToolButton(self.groupBox_3)
        self.print_openfiledialog_button.setObjectName("print_openfiledialog_button")
        self.gridLayout.addWidget(self.print_openfiledialog_button, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.print_csv_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.print_csv_checkbox.setObjectName("print_csv_checkbox")
        self.verticalLayout_4.addWidget(self.print_csv_checkbox)
        self.print_md_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.print_md_checkbox.setObjectName("print_md_checkbox")
        self.verticalLayout_4.addWidget(self.print_md_checkbox)
        self.print_startprint_button = QtWidgets.QPushButton(self.groupBox_3)
        self.print_startprint_button.setObjectName("print_startprint_button")
        self.verticalLayout_4.addWidget(self.print_startprint_button)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.tab_2)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.toolBoxPage1 = QtWidgets.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 228, 186))
        self.toolBoxPage1.setObjectName("toolBoxPage1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.toolBoxPage1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.snippets_createsnippets_button = QtWidgets.QPushButton(self.toolBoxPage1)
        self.snippets_createsnippets_button.setObjectName("snippets_createsnippets_button")
        self.gridLayout_3.addWidget(self.snippets_createsnippets_button, 3, 0, 1, 2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.toolBoxPage1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.snippets_prefix_lineedit = QtWidgets.QLineEdit(self.toolBoxPage1)
        self.snippets_prefix_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.snippets_prefix_lineedit.setObjectName("snippets_prefix_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.snippets_prefix_lineedit)
        self.verticalLayout_7.addLayout(self.formLayout)
        self.snippets_forvsc_radiobutton = QtWidgets.QRadioButton(self.toolBoxPage1)
        self.snippets_forvsc_radiobutton.setObjectName("snippets_forvsc_radiobutton")
        self.verticalLayout_7.addWidget(self.snippets_forvsc_radiobutton)
        self.snippets_foratom_radiobutton = QtWidgets.QRadioButton(self.toolBoxPage1)
        self.snippets_foratom_radiobutton.setObjectName("snippets_foratom_radiobutton")
        self.verticalLayout_7.addWidget(self.snippets_foratom_radiobutton)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.toolBox.addItem(self.toolBoxPage1, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 98, 151))
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.taks_output_plaintextedit = QtWidgets.QTextEdit(self.page)
        self.taks_output_plaintextedit.setEnabled(True)
        self.taks_output_plaintextedit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taks_output_plaintextedit.setReadOnly(True)
        self.taks_output_plaintextedit.setObjectName("taks_output_plaintextedit")
        self.gridLayout_2.addWidget(self.taks_output_plaintextedit, 0, 0, 1, 1)
        self.task_createtask_button = QtWidgets.QPushButton(self.page)
        self.task_createtask_button.setEnabled(True)
        self.task_createtask_button.setObjectName("task_createtask_button")
        self.gridLayout_2.addWidget(self.task_createtask_button, 1, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.gridLayout_4.addWidget(self.toolBox, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget, 0, QtCore.Qt.AlignTop)
        self.output_treewidget = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fira Mono Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.output_treewidget.setFont(font)
        self.output_treewidget.setStyleSheet("QTreeView {\n"
"    alternate-background-color:rgba(162, 243, 255, 50);\n"
"}\n"
"QTreeView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"     border: 1px solid #d9d9d9;\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
"}\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    \n"
"    border-image: url(:/images/ressources/images/vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    \n"
"    border-image: url(:/images/ressources/images/branch-more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"   \n"
"    border-image: url(:/images/ressources/images/branch-end.png) 0;\n"
"}\n"
"\n"
"")
        self.output_treewidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.output_treewidget.setAutoScrollMargin(20)
        self.output_treewidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.output_treewidget.setAlternatingRowColors(True)
        self.output_treewidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.output_treewidget.setAutoExpandDelay(1)
        self.output_treewidget.setIndentation(175)
        self.output_treewidget.setRootIsDecorated(False)
        self.output_treewidget.setUniformRowHeights(True)
        self.output_treewidget.setItemsExpandable(True)
        self.output_treewidget.setAnimated(False)
        self.output_treewidget.setAllColumnsShowFocus(False)
        self.output_treewidget.setWordWrap(False)
        self.output_treewidget.setHeaderHidden(False)
        self.output_treewidget.setObjectName("output_treewidget")
        self.output_treewidget.header().setCascadingSectionResizes(True)
        self.output_treewidget.header().setDefaultSectionSize(100)
        self.output_treewidget.header().setHighlightSections(True)
        self.output_treewidget.header().setMinimumSectionSize(100)
        self.output_treewidget.header().setSortIndicatorShown(False)
        self.output_treewidget.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.output_treewidget)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.db_status_lineedit = QtWidgets.QLineEdit(self.groupBox_4)
        self.db_status_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.db_status_lineedit.setReadOnly(True)
        self.db_status_lineedit.setObjectName("db_status_lineedit")
        self.verticalLayout_5.addWidget(self.db_status_lineedit)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.fncnumber_lcdnumber = QtWidgets.QLCDNumber(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fncnumber_lcdnumber.setFont(font)
        self.fncnumber_lcdnumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fncnumber_lcdnumber.setMidLineWidth(1)
        self.fncnumber_lcdnumber.setDigitCount(4)
        self.fncnumber_lcdnumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.fncnumber_lcdnumber.setObjectName("fncnumber_lcdnumber")
        self.verticalLayout_5.addWidget(self.fncnumber_lcdnumber)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fontsize_spinbox = QtWidgets.QSpinBox(self.groupBox_5)
        self.fontsize_spinbox.setObjectName("fontsize_spinbox")
        self.verticalLayout_6.addWidget(self.fontsize_spinbox)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.options_asfilepath_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.options_asfilepath_checkbox.setObjectName("options_asfilepath_checkbox")
        self.verticalLayout_2.addWidget(self.options_asfilepath_checkbox)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.groupBox_4, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionrebuild_DB = QtWidgets.QAction(MainWindow)
        self.actionrebuild_DB.setObjectName("actionrebuild_DB")
        self.actionopen_Settings = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ressources/misc/cog_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen_Settings.setIcon(icon)
        self.actionopen_Settings.setIconVisibleInMenu(True)
        self.actionopen_Settings.setObjectName("actionopen_Settings")
        self.menuSettings.addAction(self.actionopen_Settings)
        self.menuDatabase.addAction(self.actionrebuild_DB)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antistasi PhoneBook Tool"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search Call List:"))
        self.search_singlefile_radiobutton.setText(_translate("MainWindow", "Single File or Function"))
        self.search_openfiledialog_button.setText(_translate("MainWindow", "..."))
        self.search_completelist_radiobutton.setText(_translate("MainWindow", "List complete Call List"))
        self.search_startsearch_button.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Search for:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Print to File"))
        self.print_openfiledialog_button.setText(_translate("MainWindow", "..."))
        self.print_csv_checkbox.setText(_translate("MainWindow", "create CSV"))
        self.print_md_checkbox.setText(_translate("MainWindow", "Create Markdown"))
        self.print_startprint_button.setText(_translate("MainWindow", "to File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Search"))
        self.snippets_createsnippets_button.setText(_translate("MainWindow", "create Snippets"))
        self.label_2.setText(_translate("MainWindow", "Prefix:"))
        self.snippets_forvsc_radiobutton.setText(_translate("MainWindow", "for VS Code"))
        self.snippets_foratom_radiobutton.setText(_translate("MainWindow", "for Atom"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), _translate("MainWindow", "Snippets Creator"))
        self.lineEdit.setText(_translate("MainWindow", "in the PhoneBook basefolder"))
        self.taks_output_plaintextedit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Trebuchet MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This will create a <span style=\" color:#5e5f13;\">.json</span> file.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" color:#5a5d1b;\">.json</span> file contains the code needed for implementing</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the <span style=\" color:#5e2c2c;\">second .exe</span> file into VS code as a &quot;Task&quot; that calls the .exe.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This means that you can call the task from within Vs code</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and in the console it will return you all callers of the .sqf file</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that you currently have open.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">YOU WILL HAVE TO COPY THE CONTENTS OF THE .JSON TO VS CODE</span></p></body></html>"))
        self.task_createtask_button.setText(_translate("MainWindow", "create"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Task/Batch Creator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Extras"))
        self.output_treewidget.setSortingEnabled(False)
        self.output_treewidget.headerItem().setText(0, _translate("MainWindow", "Results"))
        self.label_3.setText(_translate("MainWindow", "Number of functions"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Font size"))
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.options_asfilepath_checkbox.setText(_translate("MainWindow", "as File Path"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionrebuild_DB.setText(_translate("MainWindow", "rebuild DB"))
        self.actionopen_Settings.setText(_translate("MainWindow", "open Settings"))
from self_created.gid_qt import DragDropLineEdit
import PhoneBook_tool_ressources_rc

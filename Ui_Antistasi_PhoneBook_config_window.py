# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\UI\Antistasi_PhoneBook_config_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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


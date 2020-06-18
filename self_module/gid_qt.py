import os
import self_created.gid_land as gil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QDialog, QFileDialog, QLineEdit, QMessageBox,
                             QTreeWidgetItem, QTextEdit, QListWidget, QListWidgetItem)


def make_icons(in_path, in_size_1, in_size_2):
    _new_icon = QIcon()
    _new_icon.addFile(in_path, size=QtCore.QSize(in_size_1, in_size_2), state=QIcon.On)
    return _new_icon

def create_new_font(in_font_name='Fira Mono Medium', in_size=14, in_bold=False, in_weight=50):
    _new_font = QFont()
    _new_font.setFamily(in_font_name)
    _new_font.setPointSize(in_size)
    _new_font.setBold(in_bold)
    _new_font.setWeight(in_weight)
    return _new_font

def create_new_dialog(in_dialog_class, *args, **kwargs):
    _dialog = QDialog()
    _dialog.ui = in_dialog_class('dialog', *args, **kwargs)
    _dialog.exec_()


#TODO:make combo fill class with multiple ways to fill
def fill_combo_from_db(in_triumvirate, in_tbl_name, in_collumn_name, in_combo):
    in_combo.clear()
    with in_triumvirate[0].opendb() as conn:
        _sql = f"SELECT {in_collumn_name} FROM {in_tbl_name}"
        conn.execute(_sql)
        _fields = [rows[0] for rows in conn.fetchall()]
        in_combo.addItems(_fields)

def enable_button(in_button, *args):
    _arg_list = [*args]
    if all([cond != '' for cond in _arg_list]):
        in_button.setEnabled(True)
    else:
        in_button.setEnabled(False)


def as_filedialog(in_type='open', in_title=None, in_dir=None, in_filter_name=None, in_ext=None, in_output_object=None):
    _show_dirs_only = QFileDialog.ShowDirsOnly
    _title = 'Open file' if in_title is None else in_title
    _start_dir = os.getcwd() if in_dir is None else in_dir
    _extensions = '' if in_ext is None else f'{in_filter_name} ({in_ext})'

    if in_type == 'open':
        filename = QFileDialog.getOpenFileName(None, _title, _start_dir, _extensions)
        _out = filename[0]
    elif in_type == 'directory':
        filename = QFileDialog.getExistingDirectory(None, _title, _start_dir, _show_dirs_only)
        _out = filename
    elif in_type == 'save':
        filename = QFileDialog.getSaveFileName(None, _title, _start_dir, _extensions)
        _out = filename[0]

    if in_output_object is not None:
        in_output_object(_out)

    return (_out, f'"{_out}" loaded as file path')


def treewidgeter_simple(in_parent, in_icon=None, in_font=None, in_expand=None, **kwargs):
    _twidget = QTreeWidgetItem(in_parent)
    for key, value in kwargs.items():
        _twidget.setText(key, value)
    if in_icon is not None:
        _twidget.setIcon(0, in_icon)
    if in_font is not None:
        for key in kwargs:
            _twidget.setFont(key, in_font)
    if in_expand is not None:
        _twidget.setExpanded(in_expand)
    return _twidget


class LittlePopuper:

    def __init__(self):
        self.msg = QMessageBox()

    def warning_dialog(self, in_message, in_detail_message=None, in_fnc=None, in_title='Warning'):
        self.msg.setWindowTitle(in_title)
        self.msg.setText(in_message)
        if in_detail_message is not None:
            self.msg.setDetailedText(in_detail_message)
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Abort)
        x = self.msg.exec()
        if in_fnc is not None and x == self.msg.Ok:
            in_fnc()
        else:
            pass

    def error_dialog(self, in_message, in_detail_message=None, in_fnc=None, in_title='Error'):
        self.msg.setWindowTitle(in_title)
        self.msg.setText(in_message)
        if in_detail_message is not None:
            self.msg.setDetailedText(in_detail_message)
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)
        x = self.msg.exec()
        if in_fnc is not None and x == self.msg.Ok:
            in_fnc()
        else:
            pass

    def information_dialog(self, in_message, in_detail_message=None, in_fnc=None, in_title='Info'):
        self.msg.setWindowTitle(in_title)
        self.msg.setText(in_message)
        if in_detail_message is not None:
            self.msg.setDetailedText(in_detail_message)
        else:
            self.msg.setDetailedText('')
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        x = self.msg.exec()
        if in_fnc is not None and x == self.msg.Ok:
            in_fnc()
        else:
            pass

    def question_dialog(self, in_message, in_detail_message=None, in_fnc=None, in_title='Info'):
        self.msg.setWindowTitle(in_title)
        self.msg.setText(in_message)
        if in_detail_message is not None:
            self.msg.setDetailedText(in_detail_message)
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        x = self.msg.exec()
        if in_fnc is not None and x == self.msg.Yes:
            in_fnc()
        else:
            pass


    def __repr__(self):

        return "LittlePopuper ()"


    def __str__(self):
        return 'Popup Dialog creator'



class DragDropLineEdit(QLineEdit):
    def __init__(self, parent, title='Drag and Drop'):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            _path = url.toLocalFile()
            self.setText(_path)


class DragDropListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_list = []
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        md = event.mimeData()
        if md.hasUrls():
            for url in md.urls():
                self.addItem(url.toLocalFile())
                self.file_list.append(url.toLocalFile())
            event.acceptProposedAction()



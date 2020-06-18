import ui_conf_dialog as cgui
import self_module.gid_qt as giq

class Configurator(cgui.Ui_Dialog):
    def __init__(self, Dialog, in_triumvirate):
        super().setupUi(Dialog)
        self.triumvirate = in_triumvirate
        self.db_tv = self.triumvirate[0]
        self.sc_tv = self.triumvirate[1]
        self.uc_tv = self.triumvirate[2]
        self.conf_buttonBox.accepted.connect(lambda: self.write_into_user_config(Dialog.accept))
        self.conf_buttonBox.rejected.connect(Dialog.reject)
        self.inputconf_antistasipath_filedialog_button.pressed.connect(lambda: self.open_filedialog_folder(self.inputconf_antistasipath_lineedit.setText))
        self.inputconf_functionspath_filedialog_button.pressed.connect(lambda: self.open_filedialog_folder(self.inputconf_functionspath_lineedit.setText))
        self.outputconf_standardfolder_filedialog_button.pressed.connect(lambda: self.open_filedialog_folder(self.outputconf_standardfolder_lineedit.setText))
        self.inputconf_antistasipath_lineedit.setText(self.uc_tv.from_user['path_to_antistasi'])
        self.inputconf_functionspath_lineedit.setText(self.uc_tv.from_user['antistasi_functions_folder'])
        self.outputconf_standardfolder_lineedit.setText(self.uc_tv.from_user['output_folder'])
        self.outputconf_standardname_lineedit.setText(self.uc_tv.from_user['output_file'])


    def open_filedialog_folder(self, out_put):
        giq.as_filedialog(in_type='directory', in_title='Open folder', in_dir=None, in_filter_name=None, in_ext=None, in_output_object=out_put)


    def write_into_user_config(self, accept_thing):

        self.uc_tv.cfg_handle.read(self.uc_tv.cfg_full_loc)
        if self.inputconf_antistasipath_lineedit.text() != '':
            self.uc_tv.cfg_handle.set('from_user', 'path_to_antistasi', self.inputconf_antistasipath_lineedit.text())

        if self.inputconf_functionspath_lineedit.text() != '':
            self.uc_tv.cfg_handle.set('from_user', 'antistasi_functions_folder', self.inputconf_functionspath_lineedit.text())

        if self.outputconf_standardfolder_lineedit.text() != '':
            self.uc_tv.cfg_handle.set('from_user', 'output_folder', self.outputconf_standardfolder_lineedit.text())

        if self.outputconf_standardname_lineedit.text() != '':
            self.uc_tv.cfg_handle.set('from_user', 'output_file', self.outputconf_standardname_lineedit.text())

        self.uc_tv.cfg_handle.set('from_user', 'changed_by_user', 'yes')

        with open(self.uc_tv.cfg_full_loc, 'w') as new_c:
            self.uc_tv.cfg_handle.write(new_c)
        accept_thing()

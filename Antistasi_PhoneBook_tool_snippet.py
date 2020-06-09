import ui_snippet_window as sgui


class SnippetWindow(sgui.Ui_Dialog):
    def __init__(self, Dialog, in_text):
        super().setupUi(Dialog)
        self.text = in_text
        self.snippet_output_textedit.setText(self.text)

        self.snippet_output_clipboard_button.pressed.connect(self.copy_snippets)


    def copy_snippets(self):
        self.snippet_output_textedit.selectAll()
        self.snippet_output_textedit.copy()

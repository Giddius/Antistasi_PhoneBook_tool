import os

# os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(os.getcwd())

for dirname, folderlist, filelist in os.walk("../../src"):
    for _folder in folderlist:
        print(os.path.join(dirname, _folder))
        if all(_spec_folder not in dirname for _spec_folder in ['dev_ui_ressources', 'designer_files']):
            _filepath = os.path.join(dirname, _folder, "__init__.py")
            with open(_filepath, 'w') as file:
                file.write('')

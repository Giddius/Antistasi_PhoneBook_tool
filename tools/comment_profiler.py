import os
from enum import Enum, auto
import sys


class Switch(Enum):
    Activate = auto()
    Deactivate = auto()


def switch_comment_profile(state: Switch):
    _changed_files = []
    for dirname, _, filelist in os.walk("../../src"):
        for _file in filelist:
            if _file.endswith('.py'):
                _path = os.path.join(dirname, _file)
                with open(_path, 'r') as _oldf:
                    _old_content = _oldf.read().splitlines()
                _new_content = []
                for line in _old_content:
                    if state == Switch.Deactivate:
                        if '@profile' in line:
                            _changed_files.append(_file)
                            line = line.replace('@profile', '# @profile')
                    elif state == Switch.Activate:
                        if '# @profile' in line:
                            _changed_files.append(_file)
                            line = line.replace('# @profile', '@profile')
                    _new_content.append(line)
                with open(_path, 'w') as _newf:
                    _newf.write('\n'.join(_new_content))
    if state == Switch.Activate:
        print('done Activating profile decorator')
    elif state == Switch.Deactivate:
        print('done Deactivating profile decorator')
    _changed_files = list(set(_changed_files))
    print('these files were changed:\n\n' + '\n'.join(_changed_files))


if __name__ == '__main__':
    if sys.argv[1] == '--activate':
        _argument = Switch.Activate
    elif sys.argv[1] == '--deactivate':
        _argument = Switch.Deactivate
    else:
        raise TypeError('you need to specify "--activate" or "--deactivate"!')

    switch_comment_profile(_argument)

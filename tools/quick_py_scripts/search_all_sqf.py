import os
from src.utility.misc_helpers.misc_functions import loadjson, writejson, pathmaker, writeit, clearit, appendwriteit
import re
_out = {}
_regexes = []
FUNC_LIST = loadjson("all_functions.json")
for func in FUNC_LIST:
    _regexes.append((func, re.compile(func + "\W")))


clearit('quick_check.html')
for dirname, _, filelist in os.walk(r"D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi"):
    for _file in filelist:
        if _file.endswith('.sqf'):
            full = os.path.join(dirname, _file)
            with open(full, 'r') as fi:
                _content = fi.read().splitlines()
            for index, line in enumerate(_content):
                for func, regex in _regexes:
                    if regex.search(line):
                        _nfunc = "<b>" + func + '</b>'
                        nline = line.strip().replace(func, _nfunc)
                        appendwriteit('quick_check.html', nline.strip() + '<br>-----------------------------------------------------<br>')

                        _after_line = line.split(func)[-1]
                        _after_letter = _after_line[0:1]
                        if _after_letter in ["A", "B", "C", "D", "H", "L", "M", "O", "P", "R", "S", "T", "U"]:
                            print(line.strip())
                        if _after_letter not in _out:
                            _out[_after_letter] = 1
                        else:
                            _out[_after_letter] += 1
writejson(_out, 'letter_after_func.json')

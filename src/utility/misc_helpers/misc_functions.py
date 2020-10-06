import os
import json
import sys
import subprocess


def loadjson(in_file):
    with open(in_file, 'r') as jsonfile:
        _out = json.load(jsonfile)
    return _out

# -------------------------------------------------------------- pathmaker -------------------------------------------------------------- #


def pathmaker(first_segment, *in_path_segments, rev=False):
    # -------------------------------------------------------------- pathmaker -------------------------------------------------------------- #
    """
    Normalizes input path or path fragments, replaces '\\\\' with '/' and combines fragments.

    Parameters
    ----------
    first_segment : str
        first path segment, if it is 'cwd' gets replaced by 'os.getcwd()'
    rev : bool, optional
        If 'True' reverts path back to Windows default, by default None

    Returns
    -------
    str
        New path from segments and normalized.
    """
    _first = os.getcwd() if first_segment == 'cwd' else first_segment
    _path = os.path.join(_first, *in_path_segments)
    _path = _path.replace('\\\\', '/')
    _path = _path.replace('\\', '/')
    if rev is True:
        _path = _path.replace('/', '\\')

    return _path.strip()

# -------------------------------------------------------------- writeit -------------------------------------------------------------- #


def writeit(in_file, in_data, append=False, in_encoding='utf-8'):
    # -------------------------------------------------------------- writeit -------------------------------------------------------------- #
    """
    Writes to a file.

    Parameters
    ----------
    in_file : str
        The target file path
    in_data : str
        The data to write
    append : bool, optional
        If True appends the data to the file, by default False
    in_encoding : str, optional
        Sets the encoding, by default 'utf-8'
    """
    if isinstance(in_file, (tuple, list)):
        _file = pathmaker(*in_file)
    elif isinstance(in_file, str):
        _file = pathmaker(in_file)
    _write_type = 'w' if append is False else 'a'
    _in_data = in_data
    with open(_file, _write_type, encoding=in_encoding) as _wfile:
        _wfile.write(_in_data)


def writejson(in_object, in_file, sort_keys=True, indent=0):
    writeit(in_file, json.dumps(in_object, sort_keys=sort_keys, indent=indent))


def appendwriteit(in_file, in_data, in_encoding='utf-8'):
    with open(in_file, 'a', encoding=in_encoding) as appendwrite_file:
        appendwrite_file.write(in_data)


# -------------------------------------------------------------- clearit -------------------------------------------------------------- #
def clearit(in_file):
    # -------------------------------------------------------------- clearit -------------------------------------------------------------- #
    """
    Deletes the contents of a file.

    Parameters
    ----------
    in_file : str
        The target file path
    """
    writeit(pathmaker(in_file), '')

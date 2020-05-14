import re
import pprint
import pandas as pd
import pathlib
import os
import collections




class Antistasi_file:
    """Antistasi Base class for File usage"""
    rellocout = 'python/Search_Output/Search_Result.txt'

    def __init__(self, type, relloc):
        self.curloc = os.getcwd()
        self.antistasiloc = 'D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi'
        self.type = type
        self.relloc = relloc
        self.absloc = pathlib.Path(self.curloc + '\\' + self.relloc)
        self.abslocout = pathlib.Path(self.curloc + '\\' + Antistasi_file.rellocout)












fncHpp = Antistasi_file('fnc','python/CSV_Output/Output.csv')
sqf = Antistasi_file('Files','python/CSV_Output/File_List.csv')

print(fncHpp.absloc)
print(sqf.absloc)
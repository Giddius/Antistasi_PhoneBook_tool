#region imports
import os
import pprint
import pandas as pd
import armaclass
from collections import OrderedDict
import sqlite3
#endregion


#region baseclass
class base_mission_filesearch:
    """File handling for searching mission folders for sqf and hpp files"""

    def __init__(self, outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None):
        self.outputfolder = outputFolderName
        self.outfile = outfile
        self.type = type
        self.curID = 0
        self.pybasefolder = baseFolder.replace('\\', '/')
        self.pyoutfile = os.path.join(cwd, subfol, self.outputfolder, self.outfile)
        if filenamedict is None:
            self.filenamedict = {}
        else:
            self.filenamedict = filenamedict

        if filefolderdict is None:
            self.filefolderdict = {}
        else:
            self.filefolderdict = filefolderdict

        if filefullpathdict is None:
            self.filefullpathdict = {}
        else:
            self.filefullpathdict = filefullpathdict



    def printfilefullpathdict(self):
        pprint.pprint(self.filefullpathdict)


    def printfilenamedict(self):
        pprint.pprint(self.filenamedict)

    def printfilefolderdict(self):
        pprint.pprint(self.filefolderdict)

    def addtocurID(self):
        self.curID = self.curID + 1

    def appendoutput(self,OUTPUT):
        with open(self.pyoutfile,'a') as f:
            f.write(OUTPUT)

    def initOutputfile(self):
        with open(self.pyoutfile,'w') as f:
            f.write('%s_file_curID,%s_file_basepath,%s_file_completepath,%s_file_name\n' % (self.type, self.type, self.type, self.type))

    def normpath(self, PATH):
        doubleslash = '\\' + '\\'
        if doubleslash in PATH:
            return PATH.replace(doubleslash, '\\')
        if '/' in PATH:
            return PATH.replace('/', '\\')

    @staticmethod
    def create_tables():
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE fnchpp_tbl (
                fnchpp_ID integer,
                fnchpp_path text,
                fnchpp_file text
                )""")

        c.execute("""CREATE TABLE sqf_tbl (
                sqf_ID integer,
                sqf_path text,
                sqf_file text
                )""")

        c.execute("""CREATE TABLE fnc_tbl (
                fnc_ID integer,
                fnc_path text,
                fnc_file text,
                fnc_callname text
                )""")

        c.execute("""CREATE TABLE call_list_tbl (
                sqf_ID integer,
                fnc_ID integer
                )""")

        conn.commit()
        conn.close()


    def walkthefile(self):
        for roots, directories, files in os.walk(self.pybasefolder):
            for file in files:
                if self.type in file:
                    roots = roots.replace('\\', '/')
                    roots = roots.replace('//', '/')
                    self.insert_upperdata(self.curID, self.normpath(roots), file)
                    self.filefolderdict[self.curID] = roots
                    self.filefullpathdict[self.curID] = str(roots + '/' + file)
                    self.filenamedict[self.curID] = file
                    self.addtocurID()

        if self.curID != 0:
            print("searched for all '%s' and saved it to '%s' in '%s'!" % (self.type, self.outfile, self.outputfolder))
        else:
            print("FAILURE: '%s' not found in the name of any files in '%s' or its subfolders!" % (self.type, baseFolder))


    def getcontent(self,KEY):
        with open(self.filefullpathdict[KEY],'r') as f:
            return f.read()

    @staticmethod
    def callerdatain(cID, tID):
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO call_list_tbl VALUES (?, ?)", (cID, tID))
        conn.commit()
        conn.close()


#endregion

#region class for functions.hpp files
class functions_hpp(base_mission_filesearch):

    def __init__(self, outfile, filenamedict=None, filefolderdict=None, filefullpathdict=None, functionsdict=None):

        super().__init__(outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None)
        self.type = 'functions.hpp'
        if functionsdict is None:
            self.functionsdict = {}
        else:
            self.functionsdict = functionsdict

    def insert_upperdata(self, ID, PATH, FILE):
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO fnchpp_tbl VALUES (?, ?, ?)", (ID, PATH, FILE))
        conn.commit()
        conn.close()

    def insert_lowerdata(self, ID, PATH, FILE, CALLNAME):
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO fnc_tbl VALUES (?, ?, ?, ?)", (ID, PATH, FILE, CALLNAME))
        conn.commit()
        conn.close()

    def getfunctions(self):
        fncID = 0
        ASfncFolder = os.path.join(baseFolder, 'functions')
        for i in range(len(self.filefullpathdict)):
            test = armaclass.parse(self.getcontent(i))
            for prefix, value in test.items():
                for folder, belue in value.items():
                    for function in belue:
                        path = os.path.join(ASfncFolder, folder)
                        funct = prefix + '_fnc_' + function
                        functfile = 'fn_' + function + '.sqf'
                        pathfull = os.path.join(ASfncFolder, folder, functfile)
                        self.insert_lowerdata(fncID, path, functfile, funct)
                        self.functionsdict[fncID] = funct
                        fncID = fncID + 1



#endregion

#region class for sqf files
class sqf_files(base_mission_filesearch):

    def __init__(self, outfile, filenamedict=None, filefolderdict=None, filefullpathdict=None):

        super().__init__( outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None)
        self.type = '.sqf'

    def insert_upperdata(self, ID, PATH, FILE):
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO sqf_tbl VALUES (?, ?, ?)", (ID, PATH, FILE))
        conn.commit()
        conn.close()




#endregion

#region external in and Outputs, is temporary
cwd = os.getcwd()
subfol = 'python'
baseFolder = 'D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi'
outputFolderName = 'CSV_Output'
sqfOutputFileName = 'Mission_File_list_SQF.csv'
fncOutputFileName = 'Mission_File_list_Fnc.csv'
functemppath = os.path.join(subfol, outputFolderName, 'Output.csv')
#endregion






def initialize_db():
    base_mission_filesearch.create_tables()
    fnc = functions_hpp(fncOutputFileName)
    sqf = sqf_files(sqfOutputFileName)
    fnc.walkthefile()
    sqf.walkthefile()
    fnc.getfunctions()


    for i in range(len(sqf.filefullpathdict)):
        content = sqf.getcontent(i)
        for nu in range(len(fnc.functionsdict)):
            func = fnc.functionsdict[nu]
            if func in content:
                base_mission_filesearch.callerdatain(i, nu)



initialize_db()
print('done!')

#TODO: change written paths to relative
#TODO: change csv to sql tables
#TODO: put function names in dict with ID for searching

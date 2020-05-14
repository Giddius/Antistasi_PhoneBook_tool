
# #region imports #c01b1b

import os
import pprint
import re
import sqlite3

import armaclass
import gidlib as gl

# #endregion imports




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

    def commentcleaner(self,content):
        a = re.compile(r'/\*\*.*\*\*\/', re.DOTALL)
        b = a.findall(content)
        for stuff in b:
            content = content.replace(stuff,'')
        return content

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

#region table creation
    @staticmethod
    def create_tables():
        conn = sqlite3.connect('AS_phonebook.db')
        conn.execute('pragma foreign_keys=on')
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
# TODO: make row for folder
        c.execute("""CREATE TABLE fnc_tbl (
                fnc_ID integer,
                fnc_path text,
                fnc_file text,
                fnc_callname text
                )""")

        c.execute("""CREATE TABLE call_list_tbl (
                sqf_ID integer references sqf_tbl,
                fnc_ID integer references fnc_tbl
                )""")

        conn.commit()
        conn.close()
#endregion

    def walkthefile(self):
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
        for roots, directories, files in os.walk(self.pybasefolder):
            for file in files:
                if self.type in file:
                    roots = roots.replace('\\', '/')
                    roots = roots.replace('//', '/')
                    c.execute("INSERT INTO " + self.tableN + " VALUES (?, ?, ?)", (self.curID, self.normpath(roots), file))
                    self.filefolderdict[self.curID] = roots
                    self.filefullpathdict[self.curID] = str(roots + '/' + file)
                    self.filenamedict[self.curID] = file
                    self.addtocurID()
        conn.commit()
        conn.close()

        if self.curID != 0:
            print("searched for all '%s' and saved it to '%s' in '%s'!" % (self.type, self.outfile, self.outputfolder))
        else:
            print("FAILURE: '%s' not found in the name of any files in '%s' or its subfolders!" % (self.type, baseFolder))
# TODO: Replace message when done searching, implement way more messages to see where the function is at right now, maybe do a function to print stuff.



    def getcontent(self,KEY):
        with open(self.filefullpathdict[KEY],'r') as f:
            wic = f.read()
            woc = self.commentcleaner(wic)
            return woc





#endregion

#region class for functions.hpp files
class functions_hpp(base_mission_filesearch):

    def __init__(self, outfile, filenamedict=None, filefolderdict=None, filefullpathdict=None, functionsdict=None):

        super().__init__(outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None)
        self.type = 'functions.hpp'
        self.tableN = 'fnchpp_tbl'
        if functionsdict is None:
            self.functionsdict = {}
        else:
            self.functionsdict = functionsdict





    def getfunctions(self):
        conn = sqlite3.connect('AS_phonebook.db')
        c = conn.cursor()
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
                        c.execute("INSERT INTO fnc_tbl VALUES (?, ?, ?, ?)",(fncID, path, functfile, funct))
                        self.functionsdict[fncID] = funct
                        fncID = fncID + 1
        conn.commit()
        conn.close()



#endregion

#region class for sqf files
class sqf_files(base_mission_filesearch):

    def __init__(self, outfile, filenamedict=None, filefolderdict=None, filefullpathdict=None):

        super().__init__( outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None)
        self.type = '.sqf'
        self.tableN = 'sqf_tbl'

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
functemppath2 = os.path.join(subfol, outputFolderName, 'forGraphviz.gv')
#endregion

def fncintosqf(fncfunction):

    fassqf = fncfunction.replace('A3A_fnc', 'fn')
    fassqf = fassqf.replace('JN_fnc', 'fn')
    fassqf = fassqf + '.sqf'
    return fassqf

def makeGraphvizcontent(listS, listF,listC):
    with open(functemppath2,'a') as f:
        f.write('node[shape="cds",style="filled",colorscheme="X11",fillcolor="gold2"];\n')
        for i in listS:
            if 'fn_customHint.sqf' not in i:
                if 'fn_log.sqf' not in i:
                    if 'fn_sizeMarker.sqf' not in i:
                        f.write(i + '\n')
        f.write('node[shape="component",style="filled",colorscheme="X11",fillcolor="aquamarine2"];\n')
        for h in listF:
            if 'fn_customHint.sqf' not in h:
                if 'fn_log.sqf' not in h:
                    if 'fn_sizeMarker.sqf' not in h:
                        f.write(h + '\n')
        for g in listC:
            if 'fn_customHint.sqf' not in g:
                if 'fn_log.sqf' not in g:
                    if 'fn_sizeMarker.sqf' not in g:
                        f.write(g)







def initialize_db():
    if os.path.isfile('AS_phonebook.db'):
        os.remove('AS_phonebook.db')
    SQF_fileslisted = []
    FNC_fileslisted = []
    GV_list = []
    base_mission_filesearch.create_tables()
    fnc = functions_hpp(fncOutputFileName)
    sqf = sqf_files(sqfOutputFileName)
    fnc.walkthefile()
    sqf.walkthefile()
    fnc.getfunctions()
    with open(functemppath,'w') as f:
        f.write('{},{},{},{},{}\n'.format('caller_ID', 'caller_path', 'caller_name', 'target_ID', 'target_callname'))
    with open(functemppath2,'w') as f:
        f.write('strict digraph Antistasi_calls { graph[mode="ipsep", mclimit="2.0",start="random",nodesep="25",sep="150000",K="2500",esep="800",overlap=false,outputorder="nodesfirst",center="50", compound="false",scale="5",splines="polyline"];\n')
        f.write('edge[color="gray37"];\n')
    conn = sqlite3.connect('AS_phonebook.db')
    c = conn.cursor()
    for i in range(len(sqf.filefullpathdict)):
        content = sqf.getcontent(i)
        for nu in range(len(fnc.functionsdict)):
            func1 = fnc.functionsdict[nu]
            func = re.compile(rf'(?<=\W){func1}(?=\W)')
            func2 = func.search(content)
            with open(functemppath,'a') as f:
                if func2:
                    c.execute("INSERT INTO call_list_tbl VALUES (?, ?)", (i, nu))
                    f.write('{},{},{},{}\n'.format(i, sqf.filefolderdict[i], sqf.filenamedict[i], fnc.functionsdict[nu]))
                    SQF_fileslisted.append('"{}" ;\n'.format(sqf.filenamedict[i]))
                    FNC_fileslisted.append('"{}" ;\n'.format(fncintosqf(fnc.functionsdict[nu])))
                    GV_list.append('"%s" -> "%s" ;\n' % (sqf.filenamedict[i], fncintosqf(fnc.functionsdict[nu])))
    makeGraphvizcontent(SQF_fileslisted, FNC_fileslisted, GV_list)
    conn.commit()
    conn.close()


    with open(functemppath2,'a') as f:
        f.write('}')

initialize_db()

print('done!')

#TODO: change written paths to relative
#TODO: implement BIS functions

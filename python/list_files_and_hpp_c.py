import os
import pprint
import pandas as pd


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

    def walkthefile(self):
        self.initOutputfile()
        for roots, directories, files in os.walk(self.pybasefolder):
            for file in files:
                if self.type in file:
                    roots = roots.replace('\\', '/')
                    roots = roots.replace('//', '/')
                    self.appendoutput('%s,%s,%s\\%s,%s\n' % (self.curID, self.normpath(roots), self.normpath(roots), file, file))
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

class functions_hpp(base_mission_filesearch):

    def __init__(self, outfile, filenamedict=None, filefolderdict=None, filefullpathdict=None):

        super().__init__(outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None)
        self.type = 'functions.hpp'



class sqf_files(base_mission_filesearch):

    def __init__(self, outfile, filenamedict=None, filefolderdict=None, filefullpathdict=None):

        super().__init__( outfile, type, filenamedict=None, filefolderdict=None, filefullpathdict=None)
        self.type = '.sqf'


cwd = os.getcwd()
subfol = 'python'
baseFolder = 'D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi'
outputFolderName = 'CSV_Output'
sqfOutputFileName = 'Mission_File_list_SQF.csv'
fncOutputFileName = 'Mission_File_list_Fnc.csv'
functemppath = os.path.join(subfol, outputFolderName, 'Output.csv')

fnc = functions_hpp(fncOutputFileName)
sqf = sqf_files(sqfOutputFileName)

fnc.walkthefile()
sqf.walkthefile()

fncData_df = pd.read_csv(
    functemppath,      # relative python path to subdirectory
    sep=',',
    dtype={'fnc_As_ID': int,'fnc_As_path': str,'fnc_As_filename': str,'fnc_As_name': str},
    usecols=['fnc_As_ID','fnc_As_name'],   # Only load the three columns specified.
    na_values=['.', '??']       # Take any '.' or '??' values as NA
)
FncDict = {}
for ind in fncData_df.index:
    FncDict[fncData_df['fnc_As_ID'][ind]] = fncData_df['fnc_As_name'][ind]

for i in range(len(sqf.filefullpathdict)):
    for ida, namea in FncDict.items():
        if namea in sqf.getcontent(i):
            pprint.pprint('{},{}'.format(i,ida))
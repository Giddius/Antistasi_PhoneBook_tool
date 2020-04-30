import os
import pprint



class base_mission_filesearch:
    """File handling for searching mission folders for sqf and hpp files"""

    def __init__(self, outfile, type, filelist=None, filelistID=None, filelistnames=None):
        self.outputfolder = outputFolderName
        self.outfile = outfile
        self.type = type
        self.curID = 0
        self.pybasefolder = baseFolder.replace('\\', '/')
        self.pyoutfile = os.path.join(cwd, subfol, self.outputfolder, self.outfile)
        if filelist is None:
            self.filelist = []
        else:
            self.filelist = filelist

        if filelistID is None:
            self.filelistID = []
        else:
            self.filelistID = filelistID

        if filelistID is None:
            self.filelistnames = []
        else:
            self.filelistnames = filelistnames

    def printfilelist(self):
        pprint.pprint(self.filelist)

    def printfilelistID(self):
        pprint.pprint(self.filelistID)

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
        else:
            return PATH.replace('/', '\\')

    def walkthefile(self):
        self.initOutputfile()
        for roots, directories, files in os.walk(self.pybasefolder):
            for file in files:
                if self.type in file:
                    fullpath = roots + '\\' + file
                    self.appendoutput('%s,%s,%s\\%s,%s\n' % (self.curID, self.normpath(roots), self.normpath(roots), file, file))
                    self.filelistID.append(self.curID)
                    self.filelistnames.append(file)
                    self.addtocurID()

        if self.curID != 0:
            print("searched for all '%s' and saved it to '%s' in '%s'!" % (self.type, self.outfile, self.outputfolder))
        else:
            print("FAILURE: '%s' not found in the name of any files in '%s' or its subfolders!" % (self.type, baseFolder))




cwd = os.getcwd()
subfol = 'python'
baseFolder = 'D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi'
outputFolderName = 'CSV_Output'
sqfOutputFileName = 'Mission_File_list_SQF.csv'
fncOutputFileName = 'Mission_File_list_Fnc.csv'


fnc = base_mission_filesearch(fncOutputFileName, 'functions.hpp')
sqf = base_mission_filesearch(sqfOutputFileName, '.sqf')

fnc.walkthefile()
sqf.walkthefile()




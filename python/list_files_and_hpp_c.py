import os
import pprint



class mission_file:
    """File handling for searching mission folders for sqf and hpp files"""

    def __init__(self, outfile, type):
        self.basefolder = baseFolderPath.replace('\\', '/')
        self.outputfolder = outputFolderName
        self.outfile = outfile
        self.type = type
        self.ID = 0

        self.pyoutfile = os.path.join(cwd, subfol, self.outputfolder, self.outfile)

        with open(self.pyoutfile,'w') as f:
            f.write('%s_file_ID,%s_file_basepath,%s_file_completepath,%s_file_name\n' % (self.type, self.type, self.type, self.type))

    def addtoID(self):
        self.ID = self.ID + 1

    def appendoutput(self,OUTPUT):
        with open(self.pyoutfile,'a') as f:
            f.write(OUTPUT)

    def walkthefile(self):
        for roots, directories, files in os.walk(self.basefolder):
            for file in files:
                if self.type in file:
                    self.appendoutput('%s,%s,%s\\%s,%s\n' % (self.ID, roots, roots, file, file))
                    self.addtoID()


cwd = os.getcwd()
subfol = 'python'
baseFolderPath = 'D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi'
outputFolderName = 'CSV_Output'
sqfOutputFileName = 'Mission_File_list_SQF.csv'
fncOutputFileName = 'Mission_File_list_Fnc.csv'


fnc = mission_file(fncOutputFileName, 'functions.hpp')
sqf = mission_file(sqfOutputFileName, 'sqf')

fnc.walkthefile()
sqf.walkthefile()

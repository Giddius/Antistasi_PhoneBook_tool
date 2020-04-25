# -----------------------------------------------------------
#
#
# Name: List_all_files_to_CSV.py
#
# Date(created): 2020-04-24
#
# Date(last updated): 2020-04-25
#
# Version: 1.0.1
#
# Author: Giddi
#
# Github: https://varGithub.com/Giddius
#
#
#
# Description: walks through the Antistasi folder and lists all files, with the exception of .txt files, into a CSV with ID, the path to the file, the path plus the filename, the filename.
#
# TODO: rename variable of functions to be easier to recognize what they are.
# TODO: clean up path to relative paths
#
# -----------------------------------------------------------

"""Walks through the Antistasi folder and lists all files, with the exception of .txt files, into a CSV with ID, the path to the file, the path plus the filename, the filename."""

import re
import os
import pathlib




def slashCorrector(invar1):
    file = invar1
    doublestring = str('\\'+'\\')
    outvar1 = file.replace(doublestring,'\\')
    return outvar1

def OverwriteAndSetCollumnName(invar1):
    file = invar1
    with open(file,'w') as clean_and_collumnheader_output:
        clean_and_collumnheader_output.write('%s,%s,%s,%s\n' % ('Antistasi_Files_id', 'Antistasi_Files_Path', 'Antistasi_Files_CompletePath', 'Antistasi_Files_Name'))






def main(invar1, invar2, outvar1, IDvar1):
    outfile = outvar1
    ID = IDvar1
    OverwriteAndSetCollumnName(outvar1)
    os.chdir(invar1)

    with open(outfile,'a') as outputCSV:
        for roots, directories, files in os.walk(invar2):
            for file  in files:
                if '.sqf' in file:
                    cleanRoot = slashCorrector(roots)
                    cleanFile = slashCorrector(file)
                    outputCSV.write(str(ID) + ',' + cleanRoot + ',' + cleanRoot + '\\' + cleanFile + ',' + cleanFile + '\n')
                    ID = ID + 1

    return ID



curID = 0
currDir = os.getcwd()
pathToAntistasiAbsolute = pathlib.PureWindowsPath('D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi')
antistasiBaseFolder = "A3-Antistasi"
outputFile = "\CSV_Output\File_List.csv"
outputPath = currDir + outputFile
outputPath = pathlib.Path(outputPath)


curID = main(pathToAntistasiAbsolute,antistasiBaseFolder,outputPath,curID)
print('done')

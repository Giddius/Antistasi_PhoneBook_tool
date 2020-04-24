# -----------------------------------------------------------
#
#
# Name: List_all_files_to_CSV.py
#
# Date(created): 2020-04-24
#
# Date(last updated): 2020-04-24
#
# Version: 1.0.0
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
    outvar1 = invar1.replace(str('\\'+'\\'),'\\')
    return outvar1

def OverwriteAndSetCollumnName(invar1):
    with open(invar1,'w') as clean_and_collumnheader_output:
        clean_and_collumnheader_output.write('Antistasi_Files_id' +','+ 'Antistasi_Files_Path' + ',' + 'Antistasi_Files_CompletePath' + ',' + 'Antistasi_Files_Name' +'\n')






def main(invar1, invar2, outvar1, IDvar1):
    ID = IDvar1
    os.chdir(invar1)
    OverwriteAndSetCollumnName(outvar1)
    with open(outvar1,'a') as outputCSV:
        for roots, directories, files in os.walk(invar2):
            for file  in files:
                if '.txt' in file:
                    continue
                else:
                    cleanRoot = slashCorrector(roots)
                    cleanFile = slashCorrector(file)
                    outputCSV.write(str(ID) + ',' + cleanRoot + ',' + cleanRoot + '\\' + cleanFile + ',' + cleanFile + '\n')
                    ID = ID + 1

    return ID


curID = 0

pathToAntistasi = pathlib.PureWindowsPath('D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi')
antistasiBaseFolder = "A3-Antistasi"
outputFile = pathlib.PureWindowsPath('D:\Dropbox\hobby\Modding\Projects\coding\python\Antistasi_tools\Outputs\File_List.csv')

curID = main(pathToAntistasi,antistasiBaseFolder,outputFile,curID)
print('done')

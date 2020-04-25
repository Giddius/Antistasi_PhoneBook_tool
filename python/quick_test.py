import re
import pprint
import pandas as pd
import pathlib
import os


def slashCorrector(invar1):
    file = invar1
    outvar1 = file.replace('\\','/')
    print(outvar1)
    return outvar1

currDir = os.getcwd()
antistasiPath = 'D:\Dropbox\hobby\Modding\Programs\Github\Foreign_Repos\A3-Antistasi'
fncCollectionPath = "CSV_Output/Output.csv"
#fncCollectionPath = currDir + "/CSV_Output/Output.csv"
#fncCollectionPath = pathlib.Path(fncCollectionPath)

fileCollectionPath = "CSV_Output/File_List.csv"
#fileCollectionPath = currDir + "/CSV_Output/File_List.csv"
#fileCollectionPath = pathlib.Path(fileCollectionPath)

outPutPath = currDir + "/Search_Output/Search_Result.txt"
outPutPath = pathlib.Path(outPutPath)

outPutPathCSV = currDir + "/Search_Output/Search_Result.CSV"
outPutPathCSV = pathlib.Path(outPutPathCSV)

fileDict = {}

fncData_df = pd.read_csv(
    fncCollectionPath,      # relative python path to subdirectory
    sep=',',
    dtype={'fnc_As_ID': int,'fnc_As_path': str,'fnc_As_filename': str,'fnc_As_name': str},
    usecols=['fnc_As_filename','fnc_As_name'],   # Only load the three columns specified.
    na_values=['.', '??']       # Take any '.' or '??' values as NA
)

fileData_df = pd.read_csv(
    fileCollectionPath,      # relative python path to subdirectory
    sep=',',
    quotechar="'",        # single quote allowed as quote character
    dtype={'Antistasi_Files_id': int,'Antistasi_Files_Path': str, 'Antistasi_Files_CompletePath': str, 'Antistasi_Files_Name': str},
    usecols=['Antistasi_Files_Path', 'Antistasi_Files_CompletePath', 'Antistasi_Files_Name'],   # Only load the three columns specified.
    na_values=['.', '??']       # Take any '.' or '??' values as NA
)


fncList = fncData_df['fnc_As_name'].tolist()

for ind in fileData_df.index:
    fileDict[fileData_df['Antistasi_Files_CompletePath'][ind]] = fileData_df['Antistasi_Files_Name'][ind]


os.chdir(antistasiPath)
with open(outPutPathCSV,'w') as outFile:
    outFile.write('%s,%s,%s\n' % ('CallerFile', 'Connector', 'TargetFunction'))


with open(outPutPath,'a') as outPutFile:
    for sqfpaths, files in fileDict.items():
        sqfpaths = antistasiPath + '\\' + sqfpaths
        sqfpaths = slashCorrector(sqfpaths)
        with open(sqfpaths,'r') as openfile:
            antistasiFileContent = openfile.read()
            for fnc in fncList:
                if fnc in antistasiFileContent:
                    outPutFile.write(""""%s" %s "%s"\n""" % (str(files), '->', str(fnc)))
                    with open(outPutPathCSV,'a') as outPutFileCSV:
                        outPutFileCSV.write(""""%s", %s ,"%s"\n""" % (str(files), '->', str(fnc)))
                    pprint.pprint('%s%s%s' % (str(files), '->', str(fnc)))
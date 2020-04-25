# -----------------------------------------------------------
#
#
# Name: find_and_list_functions.py
#
# Date(created): 2020-04-23
#
# Date(last updated): 2020-04-23
#
# Version: 1.0.0
#
# Author: Giddi
#
# Github: https://Github.com/Giddius
#
#
#
# Description: Reads the function.hpp and jeroens function.hpp file and creates a CSV with ID, Path, Name of the fnc file and name of the function(how it is called).
# The clear calls are stil in there as I had a weird bug were I found parts of a local variable from the first input file in the output of the second input file and wanted to make sure I didn't accidentally appended a list or so.
#
# Bug: 3 categorise in Antistasi functions.hpp aren't recognized yet "class ModsAndDLC" "class Missions" "class Intel"
#
# TODO: rename variable of functions to be easier to recognize what they are.
#
# TODO: clean up path to relative paths
#
# -----------------------------------------------------------

"""Reads the function.hpp and jeroens function.hpp file and creates a CSV with ID, Path, Name of the fnc file and name of the function(how it is called)."""
import re
import collections
import pprint
import os
import pathlib



# Regex forfinding the classname that defines the function name, eg [A3A]_fnc_somefunction. looks for not indented class.
prefixFindRegex = re.compile(r'(?<=^class\s).*')

# Regex to find the classnames that define the folder the function file is in. looks for class that is only indented by one tab.
foldernameFindRegex = re.compile(r'(?<=^\tclass\s).*', re.MULTILINE)

# Reads in the input file as a whole
def ReadInFile(invar1):
    with open(invar1,'r') as file:
        content = file.read()
        return content

# uses the "prefixFindRegex" from above to find the name for the Prefix. Then joins it as the single string gets returned as a list initially.
def getPrefix(fnfile):
    Prefixtemp = prefixFindRegex.findall(fnfile)
    A3Aprefix = ''.join(Prefixtemp)
    Prefixtemp.clear()
    return A3Aprefix


# uses "foldernameFindRegex" from above to to find the folder names and stores it in a list.
def getFolderNames(fnfile):
    nameList = foldernameFindRegex.findall(fnfile)
    #print(nameList)
    return nameList


# remove comments out of the text, is relying on compiled Regex in cleanvariousletters function, as I wasn't sure if this loop in the function would work like I would wanted it to.
def commentremover(temptext,var1):
    for i in var1:
        temptext = temptext.replace(i,'')
    return temptext


# Removes various little bits from the text, so we can later grab anything between two "folder" classes.
def cleanvariousletters(invar1):
    formattedinput = invar1.replace('{','')
    formattedinput = formattedinput.replace('}','')
    formattedinput = formattedinput.replace(';','')
    formattedinput = formattedinput.replace('\t','')

    commentslist = re.findall(rf'^//.*(?=\n)',formattedinput, re.MULTILINE)
    formattedinputnew = commentremover(formattedinput,commentslist)
    formattedinput = formattedinputnew

    formattedinput = formattedinput.replace('class','')
    formattedinput = formattedinput.replace('\n','')
    #print(formattedinput)
    commentslist.clear()
    return formattedinput
    formattedinput.clear()

# Overwrites the outout CSV files, with the id for each collumn, so we start from a fresh csv file.
def OverwriteAndSetCollumnName(invar1):
    with open(invar1,'w') as clean_and_collumnheader_output:
        clean_and_collumnheader_output.write('%s,%s,%s,%s\n' % ('fnc_As_ID', 'fnc_As_path', 'fnc_As_filename', 'fnc_As_name'))


# Loops through the function list and stores everything between two folder in dict. Key is the first folder name and value is everything found between the two names.
# loop is only until the second to last key as the last key wouldn't have another key to match inbetween. last key gets called extra and just takes the rest of the text.
def SortFunctionsToDict(invar1,invar2,invar3):
    classA =''
    classB =''
    poscur = 0
    posnext = 1
    for folder in invar1[0:-1]:
        classA = invar1[poscur]
        classB = invar1[posnext]
        fncnameFindRegex = re.compile(rf'(?<=\b{classA}\b).*(?=\b{classB}\b)')
        invar2[folder] = fncnameFindRegex.findall(invar3)
        poscur = poscur + 1
        posnext = posnext + 1

    classA = invar1[-1]
    fncnameFindRegex = re.compile(rf'(?<={classA}).*', re.DOTALL)
    invar2[classA] = fncnameFindRegex.findall(invar3)
    #print(invar2)
    return invar2


# Takes the dict, loops through keys then splits the value in strings and loops through that. Prints a CSV formatted string to the output file and as debug also prints it to the console.
# ID gets returned so a new function.hpp can be appended without starting at 0 ID again.
def WriteFncToCsv(invar1,invar2,invar3,invar4,invar5):
    ID = invar3
    for key, value in invar1.items():
        for lines in value:
            value0 = lines.split()
            for value1 in value0:
                with open(invar2,'a') as result_file:
                    result_file.write(str(ID) +','+ invar4 + '\\' + str(key) +'\\'+ str(value1) + '.sqf' + ',' + str(value1) + '.sqf' + ',' + invar5 + '_' + 'fnc' + '_' + str(value1) + '\n')
                    pprint.pprint(str(ID) +','+ invar4 + str(key) +'\\'+ str(value1) + '.sqf' + ',' + invar5 + '_' + 'fnc' + '_' + str(value1) + '\n')
                ID = ID + 1
        pprint.pprint('A3-Antistasi\\functions\\' + str(key) + ' !!!DONE!!!')
    return ID




# Main function that call all the others,
# just gives the ID forth from the WriteFncToCsv function.
def main(varIN,varOut,varID,varDir):


    hppcontent = ReadInFile(varIN)


    fncPrefix = getPrefix(hppcontent)

    foldernameList = getFolderNames(hppcontent)

    formattedhppcontent = cleanvariousletters(hppcontent)

    fncdict = dict.fromkeys(foldernameList, 0)

    fncdict = SortFunctionsToDict(foldernameList,fncdict,formattedhppcontent)

    curID = WriteFncToCsv(fncdict,varOut,varID,varDir,fncPrefix)
    fncdict.clear()
    foldernameList.clear()
    return curID




#defines first input and output file
currDir = os.getcwd()
inputFile = "D:\\Dropbox\\hobby\\Modding\\Programs\\Github\\Foreign_Repos\\A3-Antistasi\\A3-Antistasi\\functions.hpp"
outputFile = currDir + "\CSV_Output\Output.csv"
outputFile = pathlib.Path(outputFile)

curID = 0                               #Starting ID
headDir = 'A3-Antistasi\\functions'     #How the Directory above the functions is called, as this is sadly different for each function.hpp.
OverwriteAndSetCollumnName(outputFile)

#calls main functions and starts the cascade
curID = main(inputFile, outputFile, curID, headDir)

inputFile = "D:\\Dropbox\\hobby\\Modding\\Programs\\Github\\Foreign_Repos\\A3-Antistasi\\A3-Antistasi\\JeroenArsenal\\functions.hpp"

headDir = 'JeroenArsenal'


#Jeroens function.hpp needs some preprocessing as it has a different style and bracket style.
# It gets saved as a temp file, just so the established workflow has not to be modified.
jeroenFormatted = ReadInFile(inputFile)
jeroenFormatted = jeroenFormatted.replace(' {','')
jeroenFormatted = jeroenFormatted.replace('}','')
jeroenFormatted = jeroenFormatted.replace(';','')
jeroenFormatted = jeroenFormatted.replace('postinit = 1','')
jeroentextsearch = re.compile(r'\t\tfile.*\n')
jeroenToFormatList = jeroentextsearch.findall(jeroenFormatted)

for lines in jeroenToFormatList:
    jeroenFormatted = jeroenFormatted.replace(lines,'')

jeroenNewInputFile = currDir + "\CSV_Output\jeroentemp.hpp"
jeroenNewInputFile = pathlib.Path(jeroenNewInputFile)

with open(jeroenNewInputFile,'w') as jeroenTempInput:
    jeroenTempInput.write(jeroenFormatted)

curID = main(jeroenNewInputFile, outputFile, curID, headDir)



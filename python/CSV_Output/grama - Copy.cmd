@echo off
setlocal enableextensions enabledelayedexpansion
pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool"
call "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\python\list_files_and_hpp_c.py"
pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\python\CSV_Output"
neato -Ecolor=#55555522 -Tpdf -Tsvg -oAS_Graph.pdf -oforGraphviz.svg forGraphviz.gv
Echo done
timeout /T 60
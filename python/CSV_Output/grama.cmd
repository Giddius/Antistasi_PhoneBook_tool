@echo off
setlocal enableextensions enabledelayedexpansion
pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool"
call "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\python\list_files_and_hpp_c.py"
timeout /T 1
pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\python\CSV_Output"

ccomps -x forGraphviz2.gv | sfdp -Goverlap=prism50000 | gvpack | circo -Tpdf -oAS_fnc_Graph3.pdf

timeout /T 30
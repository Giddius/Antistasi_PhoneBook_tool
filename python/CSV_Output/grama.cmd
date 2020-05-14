@echo off
setlocal enableextensions enabledelayedexpansion
pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool"
call "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\python\list_files_and_hpp_c.py"

pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool\python\CSV_Output"
rem neato -Ecolor=#310202f5 -Tpdf -Tsvg -oAS_Graph.pdf -oforGraphviz.svg forGraphviz.gv
rem fdp forGraphviz.gv | sfdp -Tpdf -oAS_fnc_Graph3.pdf
rem twopi forGraphviz.gv | ccomps -x -C | gvpack | unflatten | neato -Gepsilon=.0001 -Ecolor=#e50914 -Gstart=rand -Tpdf -Tsvg -oAS_Graph.pdf -oforGraphviz.svg
rem sfdp forGraphviz.gv | mingle | sccmap | neato -Gepsilon=.001 -Ecolor=#e50914 -Gstart=rand -Tpdf -Tsvg -oAS_Graph.pdf -oforGraphviz.svg

rem sfdp forGraphviz.gv | ccomps -x -C | neato | gvpack | neato -n1 -Gepsilon=.00000001 -Ecolor=#a15e5e -Gstart=rand -Tpdf -oAS_Graph5.pdf
neato -n1 -Gepsilon=.00000001 -Ecolor=#a15e5e -Gstart=rand -Tpdf -oAS_Graph5.pdf forGraphviz.gv
echo 5 done
timeout /T 30
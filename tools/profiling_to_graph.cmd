@rem taskarg: ${file}
@Echo off
set OLDHOME_FOLDER=%~dp0
set PATH_GRAPHVIZ="C:\Program Files (x86)\Graphviz2.38\bin\dot.exe"
pushd %OLDHOME_FOLDER%
call ..\.venv\Scripts\activate
rem ---------------------------------------------------
set _date=%DATE:/=-%
set _time=%TIME::=%
set _time=%_time: =0%
rem ---------------------------------------------------
rem ---------------------------------------------------
set _decades=%_date:~-2%
set _years=%_date:~-4%
set _months=%_date:~3,2%
set _days=%_date:~0,2%
rem ---------------------------------------------------
set _hours=%_time:~0,2%
set _minutes=%_time:~2,2%
set _seconds=%_time:~4,2%
rem ---------------------------------------------------


set INPATH=%~dp1
set INFILE=%~nx1
set INFILEBASE=%~n1

echo %INPATH%
echo %INFILE%
echo %INFILEBASE%


pushd %INPATH%
python -m cProfile -o %INFILEBASE%_graph.pstats %INFILE%

timeout /t 2
MKDIR %INPATH%reports\graph_profiling
call gprof2dot.exe -f pstats %INFILEBASE%_graph.pstats | %PATH_GRAPHVIZ% -Tsvg -o %INPATH%reports\graph_profiling\[%_years%-%_months%-%_days%_%_hours%-%_minutes%-%_seconds%]_%INFILEBASE%.svg
DEL %INFILEBASE%_graph.pstats
echo finished


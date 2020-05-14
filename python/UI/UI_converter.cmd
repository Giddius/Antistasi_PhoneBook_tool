@Echo off
>nul 2>&1 fsutil dirty query %systemdrive% || echo CreateObject^("Shell.Application"^).ShellExecute "%~0", "ELEVATED", "", "runas", 1 > "%temp%\uac.vbs" && "%temp%\uac.vbs" && exit /b
SETLOCAL EnableDelayedExpansion
Set INFILE=python\UI\As_phonebook_pyQT_temp.ui
Set OUTFILE=python\AS_phonebook_ui.py
pushd "D:\Dropbox\hobby\Modding\Programs\Github\My Repos\Antistasi_PhoneBook_tool"
pyuic5 -x %INFILE% -o %OUTFILE%
timeout /t 5
EXIT
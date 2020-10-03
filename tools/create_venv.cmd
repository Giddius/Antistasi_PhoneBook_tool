@Echo off
set OLDHOME_FOLDER=%~dp0
set INPATH=%~dp1
set INFILE=%~nx1
set INFILEBASE=%~n1
set _date=%DATE:/=-%


pushd %OLDHOME_FOLDER%
mkdir ..\.venv
python -m venv ..\.venv
pushd ..\.venv
call .\Scripts\activate.bat


rem upgrading pip to get rid of stupid warning
python.exe -m pip install --upgrade pip


rem DEV DEPENDENCIES ---------------------------------

pip install --no-cache-dir --force-reinstall wheel
pip install --no-cache-dir pywin32
pip install --no-cache-dir --force-reinstall https://github.com/pyinstaller/pyinstaller/tarball/develop
pip install --no-cache-dir memory-profiler
pip install --no-cache-dir matplotlib
pip install --no-cache-dir import-profiler
pip install --no-cache-dir objectgraph
pip install  --no-cache-dir pipreqs
pip install --no-cache-dir setuptools
pip install --no-cache-dir --force-reinstall --pre PyQt5-tools~=5.15


rem QT DEPENDENCIES ------------------------------------

rem pip install --no-cache-dir PyQt5
rem pip install --no-cache-dir pyopengl
rem pip install --no-cache-dir PyQt3D
rem pip install --no-cache-dir PyQtChart
rem pip install --no-cache-dir PyQtDataVisualization
rem pip install --no-cache-dir PyQtWebEngine
rem pip install --no-cache-dir pyqtgraph
rem pip install --no-cache-dir QScintilla


rem DEPENDENCIE FROM GITHUB --------------------------

pip install --no-cache-dir git+https://github.com/overfl0/Armaclass.git



rem MISC DEPENDECIES --------------------------------------------------------

pip install --no-cache-dir pyperclip
rem pip install --no-cache-dir --force-reinstall jinja2
rem pip install --no-cache-dir --force-reinstall bs4



rem TEST DEPENDENCIES ---------------------------------

pip install --no-cache-dir pytest-qt
pip install --no-cache-dir pytest


pip freeze > ..\requirements_dev.txt
echo. > ..\requirements.txt

rem the following only works most likely on my system, I made it to automate a stupid task and Its a hack and needs to be commentes out on other systems. It sets the Vscode path settings for the qt tools to the exe files within the venv.
call set_qt_workspace_settings.exe %cd%

pushd %OLDHOME_FOLDER%
rem INSTALL THE PACKAGE ITSELF AS -dev PACKAGE SO I DONT HAVE TO DEAL WITH RELATIVE PATHS
call dev_install_this_package.cmd


@Echo off
SETLOCAL EnableDelayedExpansion


echo start?
pause
pyinstaller --noconsole --onefile -i "D:\Dropbox\hobby\Modding\Projects\My_Repos\Antistasi_PhoneBook_tool\ressources\misc\Double-J-Design-Apple-Festival-App-phone.ico" --name Antistasi_PhoneBook Ui_Antistasi_PhoneBook_tool.py
timeout /t 60
pyinstaller --onefile -i "D:\Dropbox\hobby\Modding\Projects\My_Repos\Antistasi_PhoneBook_tool\ressources\misc\Wrench2.ico" --name Configurator_PhoneBook configurator.py
pause

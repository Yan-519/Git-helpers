@echo off

set TEMP_DIR=pyinstaller_temp

if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"

mkdir "%TEMP_DIR%"

pyinstaller --onefile --windowed --name Pull --workpath "%TEMP_DIR%\build\Pull" --distpath "%TEMP_DIR%\dist\Pull" Pull.pyw
pyinstaller --onefile --windowed --name Push --workpath "%TEMP_DIR%\build\Push" --distpath "%TEMP_DIR%\dist\Push" Push.pyw

move /y "%TEMP_DIR%\dist\Pull\Pull.exe" ".\Pull.exe"
move /y "%TEMP_DIR%\dist\Push\Push.exe" ".\Push.exe"

rmdir /s /q "%TEMP_DIR%"

del /q Pull.spec 2>nul
del /q Push.spec 2>nul

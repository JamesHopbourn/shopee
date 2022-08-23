cd %USERPROFILE%\Downloads

scp james@james.local:$HOME/code/shopee/shopee_launch.py ./

set /p version="input new version:"

del shopee_upload.spec

pyinstaller -F --add-data "api-ms-win-core-path-l1-1-0.dll;." --icon=shopee-logo.ico shopee_launch.py

move /Y dist\shopee_launch.exe "%USERPROFILE%\Desktop\shopee %version%.exe"

scp "%USERPROFILE%\Desktop\shopee %version%.exe" "james@james.local:~/Desktop"

exit
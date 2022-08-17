cd %USERPROFILE%\Downloads

scp james@james.local:$HOME/code/shopee/shopee_upload.py ./

set /p version="input new version:"

del shopee_upload.spec

pyinstaller -F --add-data "api-ms-win-core-path-l1-1-0.dll;." --icon=shopee-logo.ico shopee_upload.py

move /Y dist\shopee_upload.exe "%USERPROFILE%\Desktop\shopee %version%.exe"

scp "%USERPROFILE%\Desktop\shopee %version%.exe" "james@james.local:~/Desktop"

exit
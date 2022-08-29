cd %USERPROFILE%\Downloads

scp james@james.local:$HOME/code/shopee/shopee_launch.py ./

set /p version="input new version:"

del shopee_upload.spec

pyinstaller -F --icon=shopee-logo.ico shopee_launch.py

move /Y dist\shopee_launch.exe "%USERPROFILE%\Desktop\shopee %version%.exe"

scp "%USERPROFILE%\Desktop\shopee %version%.exe" "james@james.local:~/Code/shopee"

scp james@james.local:$HOME/code/shopee/*.xlsx "%USERPROFILE%/Desktop"

scp james@james.local:$HOME/code/shopee/cookies.txt "%USERPROFILE%/Desktop"

exit
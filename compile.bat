set /p version="input new version:"

cd C:\Users\Administrator\Downloads

del shopee_upload.spec

pyinstaller -F --icon=shopee-logo.ico shopee_upload.py

move /Y dist\shopee_upload.exe "%USERPROFILE%\Desktop\shopee %version%.exe"
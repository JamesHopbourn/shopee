set /p version="input new version:"

cd C:\Users\Administrator\Downloads

pyinstaller -F shopee_upload.py

move /Y dist\shopee_upload.exe "shopee_upload %version%.exe"
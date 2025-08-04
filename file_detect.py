# 使用 Python 進行檔案偵測
import os

str = r"C:\Windows\WinSxS\amd64_microsoft-windows-lsa-minwin_31bf3856ad364e35_10.0.26100.1591_none_d92b9cc442553e63"
print(str)
if os.path.exists(str):
    print("該路徑為檔案!")
elif os.path.isdir(str):
    print("該路徑為目錄!")
else:
    print("other")

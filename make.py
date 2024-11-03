import os

os.system("pyinstaller -F -i logo.ico -w app.py")  
# os.system("pyinstaller -F -w app.py")  

# pyinstaller -F app.py
# pyinstaller -F -i "logo.ico" app.py
# pyinstaller -F -i "logo.ico" -w app.py
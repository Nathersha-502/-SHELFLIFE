@echo off
cd /d C:\Users\smjai\.gemini\antigravity\scratch\shelflife
echo Testing backend (database + auth)...
C:\Users\smjai\AppData\Local\Python\pythoncore-3.14-64\python.exe test_backend.py > C:\Users\smjai\Documents\shelflife_test.txt 2>&1
echo Test complete. Check shelflife_test.txt
type C:\Users\smjai\Documents\shelflife_test.txt

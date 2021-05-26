from directory_maker import directory_maker
from make_folders import makefolders
import time, sys, os

def call_diskpart():
    os.system("diskpart.exe")
    

def folder_maker():
    directory_maker()
    print("Directory folder is created.")
    time.sleep(2)
    makefolders()
    time.sleep(1)
    
folder_maker()
time.sleep(2)
call_diskpart()

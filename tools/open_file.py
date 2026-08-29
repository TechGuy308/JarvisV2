#Open Files
import os
import pathlib


def open(filename):
    os.startfile(filename)

def search_for_file(filename:str):
    file_list=[]
    desktop = pathlib.Path("C:/Users/chris/Downloads")
    for file in desktop.rglob("*"):
        if str(filename).lower() in file.name.lower() and file.is_file():
            file_list.append(file)
        
    return file_list


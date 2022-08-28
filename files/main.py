__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile
import shutil
from os import listdir
from os.path import isfile, join


path = os.getcwd()
zip_path = path +'\\files\\data.zip'
path = path+ '\\files\\cache'

def clean_cache():
    """
     creates an empty folder named cache in the current directory.
     If it already exists, it deletes everything in the cache folder.
    """
    # Check whether the specified path exists or not
    if os.path.exists(path):
        #Delete directory and create new one
        #os.rmdir(path)
        shutil.rmtree(path, ignore_errors=False)
        # Create a new directory because it does not exist now 
        os.makedirs(path)
    else :
        os.makedirs(path)
        

def cache_zip(zip_file_path,cache_path):
    zf = ZipFile(zip_file_path, 'r')
    zf.extractall(cache_path)
    zf.close()
    

def cached_files():
    filepathlist = [os.path.join(path, f) for f in listdir(path) if isfile(join(path, f))]
    return filepathlist

def find_password(file_list):
    for file in file_list:
        filetext = open(file).read()
        for line in filetext.split("\n"):
            if "password" in line:
                return line.strip('password: ').strip()
    

clean_cache()
cache_zip(zip_path, path)
#D:\GITCODE\WINC\files\cache\0.txt   
#print(cached_files())
file_list = cached_files()
password = find_password(file_list)
print(password)
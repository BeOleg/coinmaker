"""
A set of utilities used by coinmaker.py

- copyanything
    copies files and folders
- replace
    recursively replaces strings in files of a directory
- rename
    recursively renames files in a directory 
    
"""

import os
import shutil
import errno

def copy_anything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def replace(rootdir, replaces, ignore_types=[]):
    for root, subFolders, files in os.walk(rootdir):
        print root
        for f in files:
            if not any([f.endswith(ext) for ext in ignore_types]):
                filepath = os.path.join(root, f)
                in_file = open(filepath).read()
                out_file = open(filepath, 'w')
                for rep in replaces:
                    in_file = in_file.replace(rep[0], rep[1])
                out_file.write(in_file)
                out_file.close

def rename(rootdir, replaces):
    for root, subFolders, files in os.walk(rootdir):
        for f in files:
            for rep in replaces:
                if rep[0] in f:
                    filepath = os.path.join(root, f)
                    newfilepath = os.path.join(root,f.replace(rep[0],rep[1]))
                    os.rename(filepath, newfilepath)

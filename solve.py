#!/usr/bin/python

# Important: sudo apt-get install ppmd kgb arj rzip bzip2 cabextract nomarch

import os
import subprocess 

def check(a):
    r = ''
    for i in range(0, len(a)):
        if a[i] == ',' or a[i] == '-' :
            break 	
        else:
            r += a[i]
    return r

i = 0
while True:
    c = os.popen("file secret").read()
    s = check(c)
    i += 1
    current = str(i) + ": " + c + " => " + s + "\n"
    print(current)

    if s == "secret: KGB Archiver file with compression level 3\n" :
        os.system('mv secret secret.kgb && kgb secret.kgb && rm secret.kgb')
    
    elif s == "secret: ARJ archive data":
        os.system('mv secret secret.arj && arj e secret.arj && rm secret.arj')
    
    elif s == "secret: PPMD archive data\n":
        os.system('mv secret secret.ppmd && ppmd d secret.ppmd && rm secret.ppmd')
    
    elif s == "secret: rzip compressed data ":
        os.system('mv secret secret.rz && rzip -d secret.rz')	
    
    elif s == "secret: gzip compressed data":
        os.system('mv secret secret.gz && gzip -d secret.gz')
    
    elif s == "secret: POSIX tar archive (GNU)\n":
        os.system('mv secret secret.tar && tar -xvf secret.tar && rm secret.tar')
    
    elif s == "secret: Zip archive data":
        os.system('mv secret secret.zip && unzip secret.zip && rm secret.zip ')
    
    elif s == "secret: Microsoft Cabinet archive data":
        os.system('mv secret secret.cab && cabextract -F "secret" secret.cab && rm secret.cab')	
    
    elif s == "secret: bzip2 compressed data":
        os.system('mv secret secret.bz2 && bzip2 -d secret.bz2 ')
    
    elif s == "secret: ARC archive data":
        os.system('mv secret secret.arc && nomarch secret.arc && rm secret.arc ')
    
    elif s == "secret: XZ compressed data\n":
        os.system(' mv secret secret.xz && xz -d secret.xz  ')
    
    elif s == "secret: 7":
        os.system('mv secret secret.7z && p7zip -d secret.7z')
    
    elif s == "secret: Zoo archive data":
        os.system('mv secret secret.zoo && zoo -extract secret.zoo && rm secret.zoo')
    
    elif s == "secret: RAR archive data":
        os.system('mv secret secret.rar && unrar e secret.rar && rm secret.rar')

    else:
        print("Extraction ended: Either not an archive file or a non-handled format.\n'file secret' output: " + c + "\nIf this is a new format add it as a new elif statement.")
        break

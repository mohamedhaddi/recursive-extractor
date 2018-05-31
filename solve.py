# Cybertalents-f100
Challenge Can You Find Me ? Forinces


#!/usr/bin/python 

'''
Code for Solve : Can You Find Me ? 
File : f100.zip
Point : 100
>>> cybertalents <<<
0x00Zero 
Note : Run This Script in Ubuntu After You Download The Tool .


Important
1- sudo apt-get install ppmd
2- sudo apt-get install kgb 
3- sudo apt-get install arj
4- sudo apt-get install rzip
5- sudo apt-get install bzip2
6- sudo apt-get install cabextract
7- sudo apt-get install nomarch
'''


import os
import subprocess 

def check(a):
	r=''
	for i in range(0,len(a)):
		if a[i]==',' or a[i]=='-' :
			break 	
		else:
			r+=a[i]
	return r

c = os.popen("file secret").read()
s = check(c)


if s == "secret: KGB Archiver file with compression level 3\n" :
	os.system('mv secret secret.kgb ; kgb secret.kgb ; rm secret.kgb')

if s == "secret: ARJ archive data":
	os.system('mv secret secret.arj ; arj e secret.arj ; rm secret.arj')
	
if s == "secret: PPMD archive data\n":
	os.system('mv secret secret.ppmd ; ppmd d secret.ppmd ; rm secret.ppmd')
	

if s == "secret: rzip compressed data ":
	os.system('mv secret secret.rz ; rzip -d secret.rz')	
	

if s == "secret: gzip compressed data":
	os.system('mv secret secret.gz ; gzip -d secret.gz')
	

if s == "secret: POSIX tar archive (GNU)\n":
	os.system('mv secret secret.tar ; tar -xvf secret.tar ; rm secret.tar')
	
if s == "secret: Zip archive data":
	os.system('mv secret secret.zip ; unzip secret.zip ; rm secret.zip ')
	
if s == "secret: Microsoft Cabinet archive data":
	os.system('mv secret secret.cab ; cabextract -F "secret" secret.cab ; rm secret.cab')	
	

if s == "secret: bzip2 compressed data":
	os.system('mv secret secret.bz2 ; bzip2 -d secret.bz2 ')
	

if s == "secret: ARC archive data":
	os.system('mv secret secret.arc ; nomarch secret.arc ; rm secret.arc ')
	
if s == "secret: XZ compressed data\n":
	os.system(' mv secret secret.xz ; xz -d secret.xz  ')
	
if s == "secret: 7":
	os.system('mv secret secret.7z ; p7zip -d secret.7z')
		
if s == "secret: Zoo archive data":
	os.system('mv secret secret.zoo ; zoo -extract secret.zoo ; rm secret.zoo')

if s == "secret: RAR archive data":
	os.system('mv secret secret.rar ; unrar e secret.rar ; rm secret.rar')




import os
import time
import sys

URL = 'https://github.com/CH3COOOH/henInfra2/releases/download/latest/'

path_default = os.getcwd() + '/bin'
path_app = input('Set the download path, or use ' + path_default + '\n')

if len(path_app) == 0:
	try:
		os.mkdir('bin')
	except:
		print('Cannot create new directory \"bin\" in current path. Is it exist?')
	path_app = path_default

isDownload = input('Path setting finished. Download APPs now?')
if isDownload == 'y':
	applist = []
	with open('./applist.txt', 'r') as o:
		while True:
			buf = o.readline()[:-1]
			if buf == '':
				break
			if '#' not in buf:
				applist.append(buf)

	os.chdir(path_app)
	print(applist)
	for a in applist:
		print('Downloading [%s]...' % a)
		os.system('wget %s%s -O %s' % (URL, a, a))

	os.system('chmod +x %s/*' % path_app)
	print('All finished.')
	print('NOTICE: it is not recommended to modify the env.\nYou\'d better to use full path.')
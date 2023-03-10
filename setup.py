import os
import time
import sys

URL = 'https://github.com/CH3COOOH/henInfra2/releases/download/latest/'

path_default = os.getcwd() + '/bin'
path_app = input('Set the PATH, or use ' + path_default + '\n')

if len(path_app) == 0:
	try:
		os.mkdir('bin')
	except:
		print('Cannot create new directory \"bin\" in current path. Is it exist?')
	path_app = path_default

if len(sys.argv) == 2 and sys.argv[1] == '-i':

	os.system('cp /etc/profile /etc/profile_%d' % time.time())
	os.system('cp /etc/rc.local /etc/rc.local_%d' % time.time())

	try:
		# with open('/etc/rc.local', 'r+') as o:
		# 	buf = o.read()
		# 	o.seek(0, 0)
		# 	o.write('export PATH=$PATH:%s\n' % path_app + buf)
		with open('/etc/profile', 'a') as o:
			o.write('\n\nexport PATH=$PATH:%s\n' % path_app)
		os.system('source /etc/profile')
	except:
		print('Failed to write /etc/profile. Are you sudoer?')
		exit(-1)

isDownload = input('PATH setting finished. Download APPs now?')
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
	print('NOTICE: if you want to run APPs with sudo, you need to add')
	print('[%s]' % path_app)
	print('behind\nDefaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin')
	print('by execute \"visudo\".')

#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
import time

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  ___ __  __  ____ _   _ ____         _    ____ ___ 
  / __ \|_ _|  \/  |/ ___| | | |  _ \       / \  |  _ \_ _|
 / / _` || || |\/| | |  _| | | | |_) |____ / _ \ | |_) | | 
| | (_| || || |  | | |_| | |_| |  _ <_____/ ___ \|  __/| | 
 \ \__,_|___|_|  |_|\____|\___/|_| \_\   /_/   \_\_|  |___|
  \____/                                                   
\n[$] IMGUR-API IMAGES UPLOADER.
[$] URL = ("https://www.Brazzers.com/").
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '[^] WELCOME TO ANONFILE-API PYTHON UPLOADER. [^]'
print '\n[^] SCRIPT WILL START WITHIN 1S. [^]\n'
time.sleep(1)
print '[^] PLEASE CHOOSE WAY TO UPLOAD IMAGE.\n'

client_id = 'e0b45b9f226195f' # YOUR HEAEDR AUTHORIZATION CLIENT ID.
client = 'Client-ID ' + client_id

img_url = raw_input("[^] ENTER IMAGE URL X> ")
headers = {'Authorization': client}
request = requests.post("https://api.imgur.com/3/upload", data=img_url, headers=headers)
#print(request.json())
try:
	if 'link' in request.text:
		img_url = request.json()['data']['link']
		print '[X] YOUR IMG URL IS $> ' + img_url
	else:
		print '[^] INVALID URL TO UPLOAD ON IMGUR. [^]'
except (IOError, TypeError) as e:
	print '[^] UNEXPECTED SYS ERROR. [^]'
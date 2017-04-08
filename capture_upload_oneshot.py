#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://deviceplus.jp/hobby/raspberrypi_entry_043/
#
import time
import picamera
import datetime
import os
from ftplib import FTP

now = datetime.datetime.now()
dir_name = now.strftime('%Y%m%d')
dir_path = '/home/pi/nas/'+dir_name
print(dir_path)
file_name = now.strftime('%H%M%S')

if not os.path.exists(dir_path):
    os.makedirs(dir_path)           #インデントを付けていなかったのでエラーが出ていた
    os.chmod(dir_path, 0777)

picamera = picamera.PiCamera()
picamera.resolution = (1024, 768)
#picamera.start_preview()
    # Camera warm-up time、これがないと色が青白くて使い物にならない
time.sleep(2)
file_name = file_name+'.jpg'
picamera.capture(dir_path+'/'+file_name)


print "Now start Upload."
_ftp = FTP('192.168.12.151')
_ftp.set_debuglevel(1) # デバッグログをリアルタイムで確認
_ftp.login('ftpuser','oishii78')

_file = open(dir_path+'/'+file_name, 'rb') #target file
_ftp.cwd('picture')
try:
    _ftp.cwd(dir_name) #target_dir
except Exception as e:
    if str(e) == '550 Failed to change directory.':
        _ftp.mkd(dir_name)
        _ftp.cwd(dir_name)
_ftp.storbinary('STOR ' + file_name, _file)
_file.close()

_ftp.quit()

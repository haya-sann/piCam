#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://deviceplus.jp/hobby/raspberrypi_entry_043/
#
import time
import picamera
import datetime
import os
from ftplib import FTP_TLS
archive_server = 'servername.jp-npo-jspe'
pw = 'password for server'
userID = 'userName.lolipop.jp'
put_directory  = 'test_timelapse'

now = datetime.datetime.now()
dir_name = now.strftime('%Y%m%d')
dir_path = '/home/pi/nas/'+dir_name
print(dir_path)
file_name = now.strftime('%H%M%S')

if not os.path.exists(dir_path):
    os.makedirs(dir_path)           #インデントを付けていなかったのでエラーが出ていた
    os.chmod(dir_path, 0777)

picamera = picamera.PiCamera()
picamera.resolution = (1920, 1080) #HD Quality Size=1.5MB
#picamera.resolution = (1024, 768) # こちらは554KB
#picamera.start_preview()
# Camera warm-up time、これがないと色が青白くて使い物にならない
time.sleep(2)
file_name = file_name+'.jpg'
picamera.capture(dir_path+'/'+file_name)

print "Now start Upload."
_ftps = FTP_TLS(userID)
_ftps.set_debuglevel(1) # デバッグログをリアルタイムで確認
_ftps.login(archive_server,pw)

_file = open(dir_path+'/'+file_name, 'rb') #target file. 次のステップでアップロード成功したら削除してもよいのではないか？
_ftps.cwd(put_directory)
try:
    _ftps.cwd(dir_name) #target_dir
except Exception as e:
    #ディレクトリがなければ '550 Failed to change directory.'　が帰ってくる。
    #もし、"550"があれば．．．まだその日のフォルダはないので、新規作成
    ##    if str(e).count('550') :　文字列が含まれるかどうかの判定はこの関数を使ってもよいが、次の書き方が分かりやすい。
    if '550' in str(e):
        _ftps.mkd(dir_name)
        _ftps.cwd(dir_name)
_ftps.storbinary('STOR ' + file_name, _file)
_file.close()

_ftps.quit()

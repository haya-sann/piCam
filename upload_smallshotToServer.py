#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
import time
import picamera
import datetime
import os
from ftplib import FTP_TLS
import ConfigParser
configfile = ConfigParser.SafeConfigParser()
configfile.read("./config.conf")

archive_server = configfile.get("settings","host") #サーバーのドメイン名
pw = configfile.get("settings","password")  #ログインパスワード
userID = configfile.get("settings","id") #サーバーログインUser id

put_directory  = 'daily_timelapse'

now = datetime.datetime.now()
dir_name = now.strftime('%Y%m%d')
dir_path = '/home/pi/nas/'+put_directory + "/" + dir_name #ローカルのSDカード上もput_directoryに納める
print(dir_path)
file_name = now.strftime('%H%M%S')

if not os.path.exists(dir_path):
    os.makedirs(dir_path)           
    os.chmod(dir_path, 0777)

picamera = picamera.PiCamera()
#picamera.resolution = (1920, 1080) #HD Quality Size=1.5MB、研究材料としては最低限これくらいはほしい。稲穂の様子はこの撮影データを拡大して確認したい
#picamera.resolution = (1024, 768) # こちらは554KBで済む
picamera.resolution = (800, 600) # こちらは●●●KBで済む
#picamera.start_preview()
# Camera warm-up time、Whiteバランスをとるための猶予時間。これがないと色が青白くて使い物にならない
time.sleep(2)
file_name = file_name+'.jpg'
picamera.capture(dir_path+'/'+file_name)

print "Now start Upload."
_ftps = FTP_TLS(userID)
_ftps.set_debuglevel(1) # デバッグログをリアルタイムで確認
_ftps.login(archive_server,pw)

_file = open(dir_path+'/'+file_name, 'rb') #target file. 次のステップでアップロード成功したら削除した方がよいのではないか？
#SD Memoryがパンクする恐れがあるので、次のステップでアップロードが成功したらファイルは削除するように、改良しましょう。

_ftps.cwd(put_directory)
try:
    _ftps.cwd(dir_name) #target_dir 撮影データは日付付きのフォルダ内に納められる。
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

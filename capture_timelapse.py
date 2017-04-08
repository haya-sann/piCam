#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://deviceplus.jp/hobby/raspberrypi_entry_043/
#
import time
import picamera
import datetime
import os

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
picamera.start_preview()
    # Camera warm-up time、これがないと色が青白くて使い物にならない
time.sleep(2)
picamera.capture(dir_path+'/'+file_name+'.jpg')
# It worked

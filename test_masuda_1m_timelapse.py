#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)  #解像度を指定
    camera.hflip = True             #水平方向に反転
    camera.vflip = True            #垂直方向に反転する。反転させない場合はこの行を削除するか、Falseを指定する
    camera.start_preview()
    time.sleep(1)
    for i, filename in enumerate(camera.capture_continuous('/home/pi/nas/photo/image_masuda{counter:02d}.jpg')):
        print('Captured image %s' % filename)
        if i == 10:                 #撮影したい枚数
            break
        time.sleep(10)              #10秒に１枚撮影。10分間隔ならこれを600にする
    camera.stop_preview()

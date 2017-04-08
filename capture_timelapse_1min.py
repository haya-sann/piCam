#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://picamera.readthedocs.io/
#にあったサンプル

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    # if no paremeter given, piture will be taken in full size picture
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('/home/pi/nas/Picture_test/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(60) # wait 1 minutes

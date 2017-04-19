#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import time
import datetime
import os

now = datetime.datetime.now()
dir_path = './capture'
file_name = now.strftime('%H%M%S')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    os.chmod(dir_path, 0777)

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = True
camera.hflip = False
#camera.brightness = 60
camera.rotation = 0
camera.start_preview()
# Camera warm-up time
time.sleep(2)
camera.capture(dir_path + '/'+file_name+'.jpg')


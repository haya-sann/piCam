#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import datetime
import time

now = datetime.datetime.now()
dir_path = './dateFolder/'
file_name = now.strftime('%Y%m%d%H%M%S')
print "File Name will be  " + file_name + ".jpg"
picamera = picamera.PiCamera()
picamera.start_preview()
# Camera warm-up time
for i in range(0, 50, 5):
    time.sleep(2)
    picamera.contrast = i
    picamera.annotate_text = file_name + " Camera Contrast is : " + str(picamera.contrast)
    picamera.capture(dir_path + file_name + '.jpg')

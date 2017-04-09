#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import datetime

now = datetime.datetime.now()
dir_path = '/home/pi/nas/photo/testProgram/piCam/datedphoto/'
file_name = now.strftime('%Y%m%d%H%M%S')
print "now.strftime is " + file_name
picamera = picamera.PiCamera()
picamera.capture(dir_path + file_name + '.jpg')

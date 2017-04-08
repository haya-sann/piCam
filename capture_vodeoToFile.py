#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://picamera.readthedocs.io/
#にあったサンプル


import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('/home/pi/nas/my_video.h264')
camera.wait_recording(60)
camera.stop_recording()

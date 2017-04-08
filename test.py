#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
camera = picamera.PiCamera()
camera.capture('/home/pi/nas/photo/image_test.jpg')


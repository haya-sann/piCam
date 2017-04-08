#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://picamera.readthedocs.io/
#にあったサンプル

import time
import picamera
from datetime import datetime, timedelta

def wait():
    # Calculate the delay to the start of the next hour
#    next_hour = (datetime.now() + timedelta(hour=1)).replace(

    next_hour = (datetime.now() + timedelta(hours=1)).replace(
        minute=0, second=0, microsecond=0)
    delay = (next_hour - datetime.now()).seconds
    time.sleep(delay)

with picamera.PiCamera() as camera:
    camera.start_preview()
    wait()
    for filename in camera.capture_continuous('/home/pi/nas/img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
        print('Captured %s' % filename)
        wait()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://picamera.readthedocs.io/
#にあったサンプル
#
#camera.start_recording(stream, format='h264', quality=23)
#というコードは何をしているのか？
#このストリームを、どうやってみるのか？

from io import BytesIO
from picamera import PiCamera

stream = BytesIO()
camera = PiCamera()
camera.resolution = (640, 480)
camera.start_recording(stream, format='h264', quality=23)
camera.wait_recording(60)
camera.stop_recording()

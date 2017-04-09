#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

num=1
while num < 10:
    while True:
        todaydetail = datetime.datetime.today()
        if todaydetail.second%10 == 0:
            os.system('python /home/pi/nas/datedjpeg.py')
            print todaydetail.second
    num += 1
print "End"


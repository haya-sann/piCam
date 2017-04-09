#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

num = 1
while num < 3:
    while True:
        todaydetail = datetime.datetime.today()
        if todaydetail.second%10 == 0:
            os.system('python ./datedjpeg.py')
            print todaydetail.second
            break
    num += 1
print "End"

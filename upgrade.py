#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from time import localtime

task = "insight-fm"
type = "warm"
trigger_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime())
end_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime())
upgrade_ip = "192.168.47.25"
ansible_host = "fm-server"
str = "\""

print trigger_time, end_time
print str
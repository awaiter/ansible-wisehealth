#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
config = configparser.ConfigParser()
config.read("hosts", encoding="utf-8")
# sections() 得到所有的section，以列表形式返回
print(config.sections())
# r = config.options("prod-clcs-server")
for i in config.sections():
    print config.items(i)
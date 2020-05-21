#!/usr/bin/env python
# -*- coding: utf-8 -*-

ansible_hosts = './hosts'
f = open(ansible_hosts)

for i in f.readlines():
    print i
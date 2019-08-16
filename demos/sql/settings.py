# -*- coding: utf-8 -*-

from __future__ import unicode_literals


'''
配置内容，从配置文件获取。每个section都是一个对象，每个key就是一个属性。

如：
[db_info]
ip=127.0.0.1
port=3306
db_name = ik

初始化后，则直接通过CONF.db_info.ip访问

'''
CONF = None

Session = None

proxy_flow = {}
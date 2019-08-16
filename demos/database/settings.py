# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from collections import namedtuple
from configparser import ConfigParser

from redis import StrictRedis

from config import basedir

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


def dictToObject(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = dictToObject(v)
    return namedtuple('object', d.keys())(*d.values())


def init_config(conf=None):
    """读取配置文件信息"""

    # 创建一个配置管理器实例用来管理配置信息
    conf = ConfigParser()

    file_name = os.path.join(basedir, 'demos/database/config.ini')
    conf.read(file_name)

    sections = {}
    for section in conf.sections():
        items = dict(conf.items(section))
        if items:
            sections.update({section: items})
    CONF = dictToObject(sections)


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:3306/{}?charset=utf8".format(
        CONF.mysql_db_info.user,
        CONF.mysql_db_info.passwd,
        CONF.mysql_db_info.ip,
        CONF.mysql_db_info.db_name)

redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')
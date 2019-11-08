# -*- coding:utf-8 -*-
# @Author: 'XingXiaolei'
# @Time  : '2019-10-15 11:09'
import configparser
import os
import sys

curPath = os.path.dirname(__file__)
rootPath = os.path.dirname(curPath)
configPathPro = os.path.join(rootPath,'config','test_config.ini')
configPath = os.path.abspath(configPathPro)
sys.path.append(rootPath)

class ConfigRead:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(configPath,encoding='utf-8')

    def urlConfig(self):
        url = self.conf.get('url','weburl')
        return url

    def userConfig(self):
        uname = self.conf.get('userinfo','uname')
        pwd = self.conf.get('userinfo','pwd')
        return uname,pwd




# -*- coding:utf-8 -*-
# @Author: 'XingXiaolei'
# @Time  : '2019-10-16 11:24'

import logging
import os,sys,datetime

def log(msg):
    logger = logging.getLogger('APPUI')#创建logger对象

    formetter = logging.Formatter('%(asctime)s %(levelname)-6s: %(message)s')#定义日志格式

    today = datetime.date.today()

    log_Path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/log/'
    logPath = log_Path + str(today) + '_test_log.txt'
    f_handler = logging.FileHandler(logPath,encoding='utf-8')#创建输出到文件的handler
    f_handler.setFormatter(formetter)#给handler添加输出格式
#============================================================================
    logger.addHandler(f_handler)

    logger.setLevel(logging.INFO)

    logger.info(msg)

    print(logPath)

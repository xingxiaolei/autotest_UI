# -*- coding:utf-8 -*-
# @Author: 'XingXiaolei'
# @Time  : '2019-10-15 10:40'
# from selenium import webdriver
# webdriver.Chrome(r'E:\autotest_TJBUI_new\driver\chromedriver.exe')

import xlrd
import os,sys
from public.config_read import rootPath
dataPath = os.path.abspath(os.path.join(rootPath,'data','TestCase.xlsx'))

def readCase():

    file = xlrd.open_workbook(dataPath)
    sheet = file.sheets()[0]
    nrows = sheet.nrows
    case_list = [
        {
            "case_name": (sheet.cell(i, 1).value,str(sheet.cell(i, 2).value)),
            # 'action_name': sheet.cell(i, 2).value,
            "display_status": int(sheet.cell(i, 3).value),
            "locate_method": sheet.cell(i, 4).value,
            "locate_element": sheet.cell(i, 5).value,
            "locate_data": sheet.cell(i, 6).value,
            "locate_click": int(sheet.cell(i, 7).value),
            "real_result": sheet.cell(i, 8).value,
            "assertLocate_method": sheet.cell(i, 9).value,
            "assertLocate_element": sheet.cell(i, 10).value,

        } for i in range(3,nrows)
    ]
    return case_list


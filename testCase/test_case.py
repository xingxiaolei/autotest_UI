# -*- coding:utf-8 -*-
# @Author: 'XingXiaolei'
# @Time  : '2019-10-15 13:56'

import os,sys,time
import unittest
from ddt import ddt,data
from selenium import webdriver
from public.config_read import ConfigRead,rootPath
from public.local_method import LocalMethod
from public.read_excel import readCase
from selenium import webdriver
from public import log_build
driverPath = os.path.abspath(os.path.join(rootPath,'driver','chromedriver.exe'))
url = ConfigRead()
urlPro = url.urlConfig()

# driver = webdriver.Chrome(driverPath)
caselist = readCase()

@ddt
class Test_TJBWeb(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(driverPath)
        driver = self.driver
        driver.get(urlPro)
        time.sleep(3)

    @data(*caselist)
    def test_web(self,case_detail):
        print(case_detail)
        method = case_detail['locate_method']
        element = case_detail['locate_element']
        casedata = case_detail['locate_data']
        click = case_detail['locate_click']
        run_web = LocalMethod(self.driver,method,element,casedata,click)
        try:
            print('开始')
            run_web.l_action()
            print('结束')
        except Exception:
            log_build.log('定位元素失败：'+case_detail['case_name'][1])
            raise

        #断言
        r_method = case_detail['assertLocate_method']
        r_element = case_detail['assertLocate_element']
        r_result = case_detail['real_result']
        r_data = ''
        r_click = ''
        r_run_web = LocalMethod(self.driver,r_method,r_element,r_data,r_click)
        try:
            # r_run_web.l_action()
            r_text = r_run_web.l_method().text
            # ret = r_run_web.l_method()
            # print(dir(ret))
            if r_text == '':
                r_text = r_run_web.l_method().get_property("value")
            # print('r_text:'+ r_text)
        except:
            raise

        if r_result == '':
            pass
        else:
            try:
                self.assertEqual(r_result,str(r_text))

            except Exception:
                log_build.log('断言失败：'+ r_result)
        time.sleep(5)

    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()


if __name__=='__main__':
    unittest.main()

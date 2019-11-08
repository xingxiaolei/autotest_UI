# -*- coding:utf-8 -*-
# @Author: 'XingXiaolei'
# @Time  : '2019-10-15 15:16'
from selenium.webdriver.support.ui import WebDriverWait

class LocalMethod():
    def __init__(self,driver,method,element,data,click):
        self.driver = driver
        self.method = method
        self.element = element
        self.data = data
        self.click = click

    def l_method(self):
        driver = self.driver
        try:
            if self.method == 'css':
                position = WebDriverWait(driver,3).until(
                    lambda driver: driver.find_element_by_css_selector(self.element)
                )
            if self.method == 'xpath':
                position = WebDriverWait(driver,3).until(
                    lambda driver: driver.find_element_by_xpath(self.element)
                )
        except:
            '元素未找到'

        return position

    def l_action(self):
        p_position = self.l_method()
        if self.data != '':
            p_position.send_keys(self.data)
        if self.click == 1:
            p_position.click()
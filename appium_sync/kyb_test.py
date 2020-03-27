# -*- conding: utf-8 -*-
# @Time      :2019/11/4 15:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :kyb_test.py
from selenium.common.exceptions import NoSuchElementException

class KybTest():
    def __init__(self,driver):
        self.driver = driver
    def check_cancelBtn(self):
        print('check_cancelBtn')

        try:
            cancelBtn = self.driver.find_element_by_id('android:id/button2')
        except NoSuchElementException:
            print('no cancelBtn')
        else:
            cancelBtn.click()
    def check_skipBtn(self):
        print('check_skipBtn')
        try:
            skipBtn = self.driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        except NoSuchElementException:
            print('no skipBtn')
        else:
            skipBtn.click()


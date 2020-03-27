# -*- conding: utf-8 -*-
# @Time      :2019/10/18 15:02
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :baseView.py
from appium import webdriver
class BaseView(object):
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
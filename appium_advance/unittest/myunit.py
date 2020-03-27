# -*- conding: utf-8 -*-
# @Time      :2019/10/18 17:45
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :myunit.py
import unittest
from appium_advance.page_object.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("=======setUp=========")
        self.driver = appium_desired()
    def tearDown(self):
        logging.info("=====tearDown")
        sleep(5)
        self.driver.close_app()

# -*- conding: utf-8 -*-
# @Time      :2019/10/17 10:39
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :kyb_logger.py
import yaml
import logging
import logging.config
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

file=open('../yaml/desired_caps.yaml','r')
data=yaml.load(file)

CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()
#
# desired_caps={}
# desired_caps['platformName']=data['platformName']
# print(desired_caps['platformName'])
# desired_caps['platformVersion']=data['platformVersion']
# desired_caps['deviceName']=data['deviceName']
#
# desired_caps['app']=data['app']
# desired_caps['appPackage']=data['appPackage']
# desired_caps['appActivity']=data['appActivity']
# desired_caps['noReset']=data['noReset']
#
# logging.info('start app...')
# driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
#
# def check_cancelBtn():
#     logging.info('check cancelBtn')
#
#     try:
#         cancelBtn = driver.find_element_by_id('android:id/button2')
#     except NoSuchElementException:
#         logging.info('no cancelBtn')
#     else:
#         cancelBtn.click()
#
# def check_skipBtn():
#     logging.info('check skipBtn')
#
#     try:
#         skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
#     except NoSuchElementException:
#         logging.info('no skipBtn')
#     else:
#         skipBtn.click()
#
# check_cancelBtn()
# check_skipBtn()

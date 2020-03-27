# -*- conding: utf-8 -*-
# @Time      :2019/10/18 11:14
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :desired_caps.py
import yaml,logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging.config


CON_LOG="../log/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    stream = open("../yaml/desired_caps.yaml", "r")
    data = yaml.load(stream)

    desired_caps={}
    desired_caps["platformName"]=data["platformName"]

    desired_caps["platformVersion"]=data["platformVersion"]
    desired_caps["deviceName"]=data["deviceName"]

    desired_caps["app"]=data["app"]
    desired_caps["noReset"]=data["noReset"]

    # desired_caps["unicodeKeyboard"]=data["unicodeKeyboard"]
    # desired_caps["resetKeyboard"]=data["resetKeyboard"]


    desired_caps["appPackage"]=data["appPackage"]
    desired_caps["appActivity"]=data["appActivity"]

    logging.info("start run app")
    driver = webdriver.Remote("http://"+str(data["ip"])+":"+str(data["port"])+"/wd/hub",desired_caps)

    driver.implicitly_wait(5)
    return driver

if __name__ == '__main__':
    appium_desired()




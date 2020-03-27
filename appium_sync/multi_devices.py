# -*- conding: utf-8 -*-
# @Time      :2019/10/16 14:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :capability_yaml.py
from appium import webdriver
import yaml
from time import ctime
from appium_sync.kyb_test import KybTest

with open("desired_caps.yaml","r") as file:
    data = yaml.load(file)

devices_list=['127.0.0.1:62001',"127.0.0.1:62025"]
def appium_desired(udid,port):
    desired_caps={}
    desired_caps["platformName"]=data["platformName"]
    desired_caps["platformVersion"]=data["platformVersion"]
    desired_caps["deviceName"]=data["deviceName"]
    desired_caps["udid"]=udid

    desired_caps["app"]=data["app"]
    desired_caps["noReset"]=data["noReset"]
    desired_caps["appPackage"]=data["appPackage"]
    desired_caps["appActivity"]=data["appActivity"]
    print('appium port:%s start run %s at %s' %(port,udid,ctime()))

    driver = webdriver.Remote("http://"+str(data["ip"])+":"+str(data["port"])+"/wd/hub",desired_caps)
    driver.implicitly_wait(5)

    k = KybTest(driver)
    k.sk
    return driver

if __name__ == '__main__':
    appium_desired(devices_list[0],4723)
    # appium_desired(devices_list[1],4725)
# -*- conding: utf-8 -*-
# @Time      :2019/10/16 14:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :capability_yaml.py
from appium import webdriver
import yaml

file = open("desired_caps.yaml","r")
data = yaml.load(file)
print(data)

desired_caps={}
desired_caps["platformName"]=data["platformName"]

desired_caps["platformVersion"]=data["platformVersion"]
desired_caps["deviceName"]=data["deviceName"]

desired_caps["app"]=data["app"]
desired_caps["noReset"]=data["noReset"]

desired_caps["appPackage"]=data["appPackage"]
desired_caps["appActivity"]=data["appActivity"]


driver = webdriver.Remote("http://"+str(data["ip"])+":"+str(data["port"])+"/wd/hub",desired_caps)
driver.implicitly_wait(5)

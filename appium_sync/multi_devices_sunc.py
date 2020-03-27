# -*- conding: utf-8 -*-
# @Time      :2019/10/16 14:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :capability_yaml.py
from appium import webdriver
import yaml
from time import ctime
import multiprocessing

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
    return driver

desired_process=[]

for i in range(len(devices_list)):
    port=4723+2*i
    desired = multiprocessing.Process(target=appium_desired,args = (devices_list[i],port))
    desired_process.append(desired)
if __name__ == '__main__':
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


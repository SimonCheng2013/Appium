# -*- conding: utf-8 -*-
# @Time      :2019/11/1 17:44
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :appium_devices_sync.py
from appium_sync.multi_appium import appium_start
from appium_sync.multi_devices import appium_desired
from appium_sync.check_port import *
from time import sleep
import multiprocessing

devices_list = ["127.0.0.1:62001","127.0.0.1:62025"]

def start_appium_action(host,port):
    if check_port(host,port):
        appium_start(host,port)
        return True
    else:
        print('appium %s start fail '%port)
        return False
def start_devices_action(udid,port):
    host = "127.0.0.1"
    if start_appium_action():
        appium_desired(udid,port)
    else:
        release_port(port)
def appium_start_sync():
    print('===appium_start_sync===')
    appium_process=[]

    for i in range(2):
        host = '127.0.0.1'
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=appium_start, args=(host, port))
        appium_process.append(appium)

    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    sleep(5)
def devices_start_sync():
    print('===devices_start_sync===')

    desired_process = []

    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))
        desired_process.append(desired)
if __name__ == '__main__':
    appium_start_sync()
    devices_start_sync()

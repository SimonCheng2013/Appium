# -*- conding: utf-8 -*-
# @Time      :2019/10/11 18:01
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :screenshot.py
from find_element.capability import driver,NoSuchElementException
#保存本地
driver.save_screenshot("login.png")
#保存指定目录
driver.get_screenshot_as_file("./image/login.png")


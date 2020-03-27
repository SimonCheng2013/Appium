# -*- conding: utf-8 -*-
# @Time      :2019/10/10 14:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :kyb_login.py
from find_element.capability import driver,NoSuchElementException
def login():

    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("自学网2018")

    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("zxw2018")
    driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

try:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except:
    login()
else:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()
    login()
    driver.findui


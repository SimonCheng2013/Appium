# -*- conding: utf-8 -*-
# @Time      :2019/10/9 14:45
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :kyb_test.py
from appium import webdriver

desired_caps={}
desired_caps["platformName"]="Android"
# desired_caps["deviceName"]="127.0.0.1:62025"
# desired_caps["platforVersion"]="9"

desired_caps["deviceName"]="Redmi"
desired_caps["platforVersion"]="9"
desired_caps["udid"]="f5f8caf5"


desired_caps["app"]=r"E:\testapk\110_2ce05c0555c386df7b6cfe917dfd012d.apk"
desired_caps["appPackage"]="com.tal.kaoyan"
desired_caps["appActivity"]="com.tal.kaoyan.ui.activity.SplashActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id("com.tal.kaoyan:id/tip_commit").click()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("111")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("111")





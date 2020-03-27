# -*- conding: utf-8 -*-
# @Time      :2019/10/11 15:48
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :get_toast.py
from find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("2018")

driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("2018")
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

error_message="用户名密码错误，你还可以尝试4次"
limit_message = "验证失败次数过多，请15分钟之后再试"

message='//*[@text=\'{}\']'.format(error_message)
# message='//*[@text=\'{}\']'.format(limit_message)

toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)



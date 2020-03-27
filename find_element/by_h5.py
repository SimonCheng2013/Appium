# -*- conding: utf-8 -*-
# @Time      :2019/10/12 11:19
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :by_h5.py
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
desired_caps = {}
desired_caps["platformName"]="Android"
desired_caps["platforVersion"]="9"
desired_caps["deviceName"]="127.0.0.1:62025"


desired_caps["app"]=r"E:\testapk\dr.fone3.2.0.apk"
desired_caps["appPackage"]="com.wondershare.drfone"
desired_caps["appActivity"]="com.wondershare.drfone.ui.activity.WelcomeActivity"

desired_caps["noReset"]="True"
# desired_caps["unicodeKeyboard"]="True"
# desired_caps["resetKeyboard"]="True"

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)
#btnBackup按钮
btnBackup = driver.find_element_by_id("com.wondershare.drfone:id/btnBackup")
driver.implicitly_wait(3)
btnBackup.click()
#Next按钮
WebDriverWait(driver,15).until(lambda x:x.find_element_by_id("com.wondershare.drfone:id/btnRecoverData"))
driver.find_element_by_id("com.wondershare.drfone:id/btnRecoverData").click()
driver.implicitly_wait(6)

WebDriverWait(driver,15).until(lambda x:x.find_element_by_class_name("android.webkit.WebView"))
contexts = driver.contexts
print(contexts)


driver.switch_to.context("WEBVIEW_com.wondershare.drfone")
driver.find_element_by_id("email").send_keys("shuqing2018@163.com")
driver.find_element_by_class_name("btn_send").click()

driver.switch_to.context("NATIVE_APP")
driver.find_element_by_class_name("android.widget.ImageButton").click()

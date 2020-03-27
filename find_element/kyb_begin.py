# -*- conding: utf-8 -*-
# @Time      :2019/10/10 14:15
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :kyb_login.py
from find_element.capability import driver,NoSuchElementException
import time
driver.find_element_by_id("com.tal.kaoyan:id/activity_splash_top").click()
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/home_top_search_layout").click()
time.sleep(3)
# driver.find_element_by_id("	com.tal.kaoyan:id/customsearchview_contentedittext").click()
driver.find_element_by_id("com.tal.kaoyan:id/customsearchview_contentedittext").send_keys("心理学")
time.sleep(3)
driver.find_element_by_id("com.tal.kaoyan:id/customsearchview_searchbtn").click()




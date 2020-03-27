# -*- conding: utf-8 -*-
# @Time      :2019/10/14 15:56
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :swipe.py
from find_element.capability import driver
from time import sleep

def get_size():
    x = driver.get_window_size("width")
    y = driver.get_window_size("height")

    return x,y
l = get_size()
print(l)

#向左滑动
def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

def swipeUp():
    l = get_size()
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.95)
    y2 = int(l[0]*0.35)
    driver.swipe(x1,y1,x1,y2,1000)
#向左滑动2次
for i in range(2):
    swipeLeft()
    sleep(0.5)

# driver.find_element()



# -*- conding: utf-8 -*-
# @Time      :2019/10/15 17:47
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :yaml_load.py
import yaml
# file = open("famliyInfo.yaml")
# data = yaml.load(file)
#
# print(data)
#
# print(data["name"])
# print(data["age"])
#
# print(data['spouse']["name"])
# print(data['spouse']["age"])
#
# print(data['children'][0]["name"])
# print(data['children'][0]["age"])
#
# data["name"] = "51zxw"
# print(data)

slogan = ["welcome","to","51zxw"]
website = {"url":"www.51zxw.net"}

print(slogan)
print(website)

print(yaml.dump(slogan))
print(yaml.dump(website))

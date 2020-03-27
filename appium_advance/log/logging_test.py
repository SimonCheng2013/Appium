# -*- conding: utf-8 -*-
# @Time      :2019/10/16 17:06
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :logging_test.py
import logging


logging.basicConfig(level=logging.INFO,filename="runlog.log",
                    format="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s")

logging.debug("debug.info")
logging.info("hello 51zxw")
logging.warning("warning info")
logging.error("debug.info")
logging.critical("debug.info")

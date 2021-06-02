#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 11:17
# @Author  : Brawenlu
# @File    : test_selenium.py
# @Software: Sinfor
import logging
# from selenium.webdriver.chrome import webdriver
# from selenium import webdriver
# 不是调用它里面的驱动
import time

import yaml
from selenium import webdriver


class Test_show_cookies():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://idtrust.sangfor.com:100/ac_portal/default/pc.html?auth=oauth&authToken=85B3E4BB958A9CD848420C503332CD4C13F43BB976C2A02C7CC5525ECC294279F57A6C660863BF9EDDAA&appToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiIzNjQyNjgwOTgxIiwicmVkaXJlY3RfdXJpIjoiaHR0cDovLzIwMC4yMDAuMC4xMzM6ODA2MC9BdXRvTG9naW4uYXNweCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwic3RhdGUiOiJNVEV5TlE9PXwifQ.2_I-6_hXrewIePZdOeH69XorFz20E7eQnnJwnYAxyhY&template=default")

    def teardown(self):
        self.driver.quit()

    # 获取cookies
    def test_get_cookies(self):
        time.sleep(10)
        cookie = self.driver.get_cookies()
        with open("data2.yml", "w", encoding='utf-8') as f:
            yaml_data = yaml.dump(cookie, f)
        time.sleep(10)

    # 使用cookie登录
    def test_set_cookies(self):
        with open("data2.yml", encoding='utf-8') as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(5)
        self.driver.get("http://bpmmarket.sangfor.com/DataList/DZ_RJDZDataList###")
        self.driver.refresh()
        time.sleep(5)
        # self.driver.find_element_by_id('menu_profile').click()
        time.sleep(8)





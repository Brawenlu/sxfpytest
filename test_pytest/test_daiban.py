#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 14:38
# @Author  : Brawenlu
# @File    : test_daiban.py
# @Software: Sinfor
import logging
import time

import allure
import requests
import yaml
from requests.cookies import RequestsCookieJar
from selenium import webdriver

# logging.basicConfig(level=logging.DEBUG)  #只对一般py文件有用
#
# webdriver.Chrome().get("http://172.22.230.200:8001/td_app/")


class Testdaiban():
    @allure.title("访问待办的定制信息系统")
    def setup_class(self):
        # self.chrome_options =
        self.logging = logging.basicConfig(level=logging.DEBUG)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.debugger_address = "127.0.0.1:9222" # chrome --remote-debugging-port=9222  关闭谷歌,开启调试端口,就不会出现那个自动化软件控制的问题
        self.chrome_options.add_argument("--start-maximized")  #--start-maximized
        # self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver.maximize_window() #最大化
        self.driver.get("http://idtrust.sangfor.com:100/ac_portal/default/pc.html?auth=oauth&authToken=85B3E4BB958A9CD848420C503332CD4C13F43BB976C2A02C7CC5525ECC294279F57A6C660863BF9EDDAA&appToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiIzNjQyNjgwOTgxIiwicmVkaXJlY3RfdXJpIjoiaHR0cDovLzIwMC4yMDAuMC4xMzM6ODA2MC9BdXRvTG9naW4uYXNweCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwic3RhdGUiOiJNVEV5TlE9PXwifQ.2_I-6_hXrewIePZdOeH69XorFz20E7eQnnJwnYAxyhY&template=default")
        self.driver.implicitly_wait(3)
        time.sleep(2)


    def teardown_class(self):
        self.driver.close()  #关闭当前活动窗口，quit关闭浏览器窗口  quit在多个浏览器窗口不会关


    def test_get_cookies(self):
        time.sleep(5)
        self.driver_cookies = self.driver.get_cookies()
        with open("daiban.yml","w",encoding="utf-8") as f:
            self.yaml_cookies = yaml.dump(self.driver_cookies,f,encoding="utf-8",allow_unicode=True)

    #先加cookie再访问必须要
    @allure.story("使用获取到的cookie进行登录")
    @allure.title("验证待办是否成功访问")

    # @allure.link("<script> alert(location.href)</script>")
    #
    # allure.attach("", attachment_type=allure.attachment_type.HTML)

    def test_login_daiban(self):
        time.sleep(3)
        s = requests.session()  #:维持会话,可以让我们在跨请求时保存某些参数
        jar=RequestsCookieJar()  #设置cookie，用来获取cookie
        with open("daiban.yml") as f:
            self.cookies = yaml.safe_load(f)
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
            jar.set(cookie['name'],cookie['value'])  #通过selenium来获取cookie
        print(jar)
        time.sleep(2)
        self.driver.get("http://bpmmarket.sangfor.com/Home/Index")
        self.driver.refresh()
        self.driver.implicitly_wait(3)
        time.sleep(3)
        self.driver.get_screenshot_as_file("./daiban.png")  #获取图片到本地

        allure.attach.file("./daiban.png",name="登陆后截图",attachment_type=allure.attachment_type.JPG)
        self.res = s.get(url="http://bpmmarket.sangfor.com/DataList/DZ_RJDZDataList",cookies=jar)   #session用来get会话
        time.sleep(5)
        print(self.res.text)
        # allure.attach.file(self.res.text,attachment_type=allure.attachment_type.TEXT)
        with open("res.text","w",encoding="utf-8") as f:
            f.write(self.res.text)
        res = "待办-深信服科技流程平台"
        # with allure.issue()
        # with allure.testcase("")

        with allure.step("验证测试结果，通过返回值"):
            assert res in self.res.text
            self.driver.get("http://bpmmarket.sangfor.com/DataList/DZ_RJDZDataList")
            self.driver.implicitly_wait(2)
            time.sleep(2)
            self.driver.get_screenshot_as_file("./daiban2.png")
            allure.attach.file("./daiban2.png", name="点击定制的截图", attachment_type=allure.attachment_type.JPG)

        #下面是通过selenium定位元素来判断
        # with allure.step("验证页面元素是否存在"):
        #     try:
        #         self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul[2]/li/a/span")
        #         print("正常登录成功")
        #         assert True
        #     except:
        #         print("需要重新登录")
        #         assert  False
        # self.response = requests.get
        time.sleep(2)





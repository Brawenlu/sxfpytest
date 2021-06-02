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
import pprint
import time
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testsele():

    def setup_class(self):
        logging.basicConfig(level=logging.DEBUG)
        # options = Options()  #实例化Options用来调用浏览器启动的一些参数
        chrome_options = webdriver.ChromeOptions()  #实例化Options用来调用浏览器启动的一些参数
        # chrome_options.debugger_address = "localhost:9222"  # chrome --remote-debugging-port=9222  关闭谷歌开启调试端口
        # 打开调试后，不会出现页面响应
        # print(chrome_options.debugger_address)
        chrome_options.add_argument("--headless")  #无可视化界面
        chrome_options.add_argument("--start-maximized")#最大化窗口
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        sleep(6)
        # self.driver.get(r"http://200.200.12.250:5000/")
        # self.driver.maximize_window()
        # self.driver.get(r"http://cs.devops.sangfor.org/users/sign_in")
        # time.sleep(5)
        # self.driver.implicitly_wait(10)
        # self.driver.implicitly_wait()

    def teardown_class(self):
        # self.driver.implicitly_wait(4)
        # sleep(3)
        self.driver.quit()
        print("结束浏览器")

    # 获取一次就可以，可以判断从外部脚本一次，定时会失效
    def test_get_cookies(self):
        chrome_options = webdriver.ChromeOptions()  # 实例化Options用来调用浏览器启动的一些参数
        # chrome_options.debugger_address = "localhost:9222"  #chrome --remote-debugging-port=9222  关闭谷歌开启调试端口
        # 打开调试后，不会出现页面响应
        # print(chrome_options.debugger_address)
        chrome_options.add_argument("--headless")  #无可视化界面
        chrome_options.add_argument("--start-maximized")  # 最大化窗口
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        sleep(6)
        self.driver.get(r"http://200.200.12.250:5000/")
        time.sleep(5)
        self.driver.find_element_by_id("login_username").send_keys("唐颖璇98290")
        self.driver.find_element_by_id("login_passwd").send_keys("sangfor98290")
        self.driver.find_element_by_id("login-btn").click()
        time.sleep(10)
        cookie = self.driver.get_cookies()
        pprint.pprint(cookie)#返回格式化的对象字符串
        print(type(cookie))
        # 写入本地的yaml文件
        with open('data.yaml',"w",encoding="utf-8") as f: #第一个，文件，w是写入
            yaml_data=yaml.dump(cookie,f,encoding='utf-8',allow_unicode=True)  #data数据中有汉字时，加上：encoding='utf-8',allow_unicode=True   , safe_dump生成基本的yaml标签
            # yaml.safe_dump()

class Test_login():
    def setup_class(self):
        logging.basicConfig(level=logging.DEBUG)
        # options = Options()  #实例化Options用来调用浏览器启动的一些参数
        chrome_options = webdriver.ChromeOptions()  # 实例化Options用来调用浏览器启动的一些参数
        # chrome_options.debugger_address = "localhost:9222"  #chrome --remote-debugging-port=9222,最好别加这个
        # 打开调试后，不会出现页面响应
        # print(chrome_options.debugger_address)
        chrome_options.add_argument("--headless")  #无可视化界面
        chrome_options.add_argument("--start-maximized")  # 最大化窗口
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        sleep(6)

    def teardown_class(self):
        # self.driver.implicitly_wait(4)
        # sleep(3)
        self.driver.quit()
        print("结束浏览器")
    #使用cookie登录
    def test_open(self):
        self.driver.get("http://200.200.12.250:5000")
        # 最终顺序：先访问再add，再刷新
        time.sleep(3)
        with open("data.yaml") as f:
            cookies = yaml.safe_load(f)  #Loader=yaml.FullLoader要加上默认的load，否则会报错    只解析基本的yaml标记，用来保证代码的安全性，不过这对于平常保存数据是足够了
        print(type(cookies))
        # self.driver.add_cookie(cookies)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            print(cookie)
            self.driver.add_cookie(cookie) #在这里添加cookie，一个个添加
        # self.driver.get(r"http://bpmmarket.sangfor.com/DataList/DZ_RJDZDataList")
        time.sleep(3)
        self.driver.refresh() #刷新一下 唐颖璇98290/sangfor98290
        # print("成功打开")
        # print(result.text())
        time.sleep(7)
        try:  #当元素不存在的情况下，代码仍可继续执行到except的部分
            self.driver.find_element_by_id("ext-gen55")
            print("正常登录成功")
        except:
            print("请先登录!")
            fun1 = Testsele() #引用另一个类里面的方法，先实例化
            fun1.test_get_cookies()
        # test_get_cookies
        self.driver.get("http://200.200.12.250:5000/?launchApp=SYNO.SDS.Drive.Application")
        time.sleep(6)





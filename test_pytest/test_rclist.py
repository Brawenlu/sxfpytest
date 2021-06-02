#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 9:32
# @Author  : Brawenlu
# @File    : test_rclist.py
# @Software: Sinfor
import json
import logging
import time

import allure
import requests
import yaml
from selenium import webdriver
from requests.cookies import RequestsCookieJar

@allure.title("验证ec登录访问资源注销")
class Testrclist():
    @allure.title("初始的第一步：访问客户端登录界面")
    def setup_class(self):
        self.options = webdriver.ChromeOptions()
        self.logging = logging.basicConfig(level=logging.DEBUG)
        self.options.debugger_address = "127.0.0.1:9222"
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get("https://10.242.1.200")
        self.driver.implicitly_wait(3)
        time.sleep(2)

    def teardown_class(self):
        print("结束测试")
        # self.driver.close()

    # def teardown_class(self):
    #     self.driver.close()

    @allure.feature("登录请求")
    @allure.testcase("http://cs.tp.sangfor.com/#/testcase/home", name="测试用例连接")
    def test_login(self):
        # time.sleep(5)
        # with allure.testcase("http://cs.tp.sangfor.com/#/testcase/home",name="测试用例连接")
        self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[1]/div[1]/div/div[1]/input").send_keys("test1")
        self.driver.find_element_by_id("loginPwd").send_keys("1")
        # self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[3]/span/div[1]").click()
        # self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[4]/button").click()
        self.driver.implicitly_wait(2)
        time.sleep(2)
        # 先点击，再判断是否有提示，如果有，再勾选，再点击,判断是否定位错误
        # try:
        #     self.cuowu = self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[2]/div").text
        #     print(self.cuowu)
        # except Exception as f:
        #     print(type(format(f)))
        #     print(f"错误xpath参数: {f}")

        #先判断是否复选框被勾选，如果没有，判断勾选使用class方法，勾选用xpath，用class可能定位不到，
        # webelent = self.driver.find_elements_by_class_name("checkbox__input")[0]
        # print(webelent)
        if (self.driver.find_elements_by_class_name("checkbox__input")[0]).is_selected():
            s = (self.driver.find_elements_by_class_name("checkbox__input")[0]).is_selected()
            print(s)
            print("查看是否勾选免责：已经选中默认免责")
            self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[3]/span/div[1]").click()
            # print(self.driver.find_elements_by_class_name("checkbox__input")[0])
            # self.driver.find_element_by_css_selector("#Calc > div.include-box__privacy > span > div.checkbox__label.checkbox--small").click()  #通过css来定位点击
            self.driver.find_elements_by_class_name("checkbox__label.checkbox--small")[0].click()  #不能有空格，换成.才可以
            s = (self.driver.find_elements_by_class_name("checkbox__input")[0]).is_selected()
            print(s)
        else:
            print("查看是否勾选免责：没有选中默认免责")
            s = (self.driver.find_elements_by_class_name("checkbox__input")[0]).is_selected()
            self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[3]/span/div[1]").click()  #通过xpath来定位选中
            print(s)
            # self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[3]/span/div[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"Calc\"]/div[4]/button/span").click()
        self.driver.implicitly_wait(5)
        time.sleep(20)
        self.driver.get_screenshot_as_file("./rclist/login.png")
        allure.attach.file("./rclist/login.png",name="登录后的截图",attachment_type=allure.attachment_type.JPG)



    @allure.feature("rclist下发查看")
    def test_rclist(self):
        print("访问rclist界面,下面是rclist下发内容")
        self.driver.implicitly_wait(3)
        # self.driver.get("https://10.242.1.200")
        self.cookies = self.driver.get_cookies()
        with open("rclist/cookie.yaml", "w", encoding="utf-8") as f:
            yaml.dump(self.cookies, f, encoding="utf-8", allow_unicode=True)
        self.session = requests.session()
        self.jar = RequestsCookieJar()
        with open("rclist/cookie.yaml", "r") as f:
            self.yaml_cookies = yaml.safe_load(f)
        # print(self.yaml_cookies)
        for cookie in self.yaml_cookies:
            self.jar.set(cookie["name"], cookie["value"])
        # print(self.jar)
        self.headers = {'Content-Type': 'text/html;charset=UTF-8'}
        self.rclist = self.session.get("https://10.242.1.200/por/rclist.csp", headers=self.headers, cookies=self.jar,
                                       verify=False)
        print(self.rclist.content.decode())
        with allure.step("验证rclist下发是否正常"):
            assert "Rcs" in self.rclist.content.decode()
        self.driver.get("https://10.242.1.200/por/rclist.csp")
        time.sleep(3)
        self.driver.get_screenshot_as_file("./rclist/rclist.png")
        allure.attach.file("./rclist/rclist.png", name="rclist界面截图", attachment_type=allure.attachment_type.JPG)


    @allure.feature("访问web资源")
    def test_fanngwenweb(self):
        print("开始访问web资源，下面是web资源请求返回内容")
        # self.driver.get("https://10.242.1.200")
        self.driver.implicitly_wait(2)
        self.cookies = self.driver.get_cookies()
        with open("rclist/cookie.yaml","w",encoding="utf-8") as f:
            yaml.dump(self.cookies,f,encoding="utf-8",allow_unicode=True)  #dump下载下来
        self.session = requests.session()
        self.jar = RequestsCookieJar()
        with open("rclist/cookie.yaml","r") as f:
            self.yaml_cookies = yaml.safe_load(f)  #从文件中读取下来
        for cookie in self.yaml_cookies:
            self.jar.set(cookie["name"],cookie["value"])
        # with allure
        self.fwweb = self.session.get("https://10.242.1.200/web/1/http/0/10.10.1.72/websso/testwebsso.php",cookies=self.jar,verify=False)
        # self.get_web = requests.get("")
        # self.fwweb = self.session.get("https://10.242.1.200/por/rclist.csp", cookies=jar,verify=False)
        print(self.fwweb.content.decode())
        with allure.step("验证web资源访问返回是否正确"):
            assert "Get method:"  in self.fwweb.content.decode()
        self.driver.get("https://10.242.1.200/web/1/http/0/10.10.1.72/websso/testwebsso.php")
        time.sleep(3)
        self.driver.get_screenshot_as_file("./rclist/web.png")
        allure.attach.file("./rclist/web.png",name="访问web资源后的截图",attachment_type = allure.attachment_type.JPG)
        # s = requests.get("http://10.10.1.72/websso/Resource.html")
        # print(s.text)

    @allure.feature("访问tcp资源")
    def test_fangwentcp(self):
        print("开始访问tcp资源，下面是tcp资源请求返回内容")
        # self.driver.get("https://10.242.1.200")
        self.driver.implicitly_wait(2)
        self.cookies = self.driver.get_cookies()
        with open("rclist/cookie.yaml", "w", encoding="utf-8") as f:
            yaml.dump(self.cookies, f, encoding="utf-8", allow_unicode=True)  # dump下载下来
        self.session = requests.session()
        self.jar = RequestsCookieJar()
        with open("rclist/cookie.yaml", "r") as f:
            self.yaml_cookies = yaml.safe_load(f)  # 从文件中读取下来
        for cookie in self.yaml_cookies:
            self.jar.set(cookie["name"], cookie["value"])
        # with allure
        self.fwtcp= self.session.get("http://10.10.1.72/websso/websso.htm",
                                      cookies=self.jar, verify=False)
        # self.get_web = requests.get("")
        # self.fwweb = self.session.get("https://10.242.1.200/por/rclist.csp", cookies=jar,verify=False)
        # print(type(self.fwtcp))
        # print(self.fwtcp.status_code)
        # print(type(self.fwtcp.content))
        # print(self.fwtcp.content)
        # print(str(self.fwtcp.content).decode())
        print(self.fwtcp.content)
        with allure.step("验证tcp资源访问返回是否正确"):
            assert "GK2312" in str(self.fwtcp.content)
        self.driver.get("http://10.10.1.72/websso/websso.htm")
        time.sleep(3)
        self.driver.get_screenshot_as_file("./rclist/tcp.png")
        allure.attach.file("./rclist/tcp.png",name="访问tcp资源后的截图", attachment_type=allure.attachment_type.JPG)

        # print(self.fwtcp.content.decode('utf-8', errors='ignore'))

        # with allure.step("验证tcp资源访问返回是否正确"):
        #     assert True
        # self.driver.get("http://10.10.1.72/websso/websso.htm")
        # time.sleep(3)
        # self.driver.get_screenshot_as_file("./rclist/tcp.png")
        # allure.attach.file("./rclist/tcp.png", name="访问tcp资源后的截图", attachment_type=allure.attachment_type.JPG)

    @allure.feature("访问L3资源")
    def test_fangwenl3(self):
        print("开始访问L3资源，下面是L3资源请求返回内容")
        # self.driver.get("https://10.242.1.200")
        self.driver.implicitly_wait(2)
        self.cookies = self.driver.get_cookies()
        with open("rclist/cookie.yaml", "w", encoding="utf-8") as f:
            yaml.dump(self.cookies, f, encoding="utf-8", allow_unicode=True)  # dump下载下来
        self.session = requests.session()
        self.jar = RequestsCookieJar()
        with open("rclist/cookie.yaml", "r") as f:
            self.yaml_cookies = yaml.safe_load(f)  # 从文件中读取下来
        for cookie in self.yaml_cookies:
            self.jar.set(cookie["name"], cookie["value"])
            # with allure
        self.headers = { 'Content-Type': 'text/html;charset=UTF-8'}
        self.fwL3 = self.session.get("http://10.10.1.72/websso/Resource.html",headers = self.headers,
                                          cookies=self.jar, verify=False)
            # self.get_web = requests.get("")
            # self.fwweb = self.session.get("https://10.242.1.200/por/rclist.csp", cookies=jar,verify=False)
        # print(type(self.fwtcp))
        # print(self.fwtcp.status_code)
        print(self.fwL3.content.decode())   #直接decode就可以获取指定编码

            # print(json.load(self.fwtcp.text))
        with allure.step("验证L3资源访问返回是否正确"):
            assert "定制地址大全" in self.fwL3.content.decode()
        self.driver.get("http://10.10.1.72/websso/Resource.html")
        time.sleep(3)
        self.driver.get_screenshot_as_file("./rclist/L3.png")
        allure.attach.file("./rclist/L3.png", name="访问L3资源后的截图", attachment_type=allure.attachment_type.JPG)


    @allure.feature("注销查看")
    def test_logout(self):
        print("开始注销，下面是注销后访问rclist的界面返回")
        self.driver.implicitly_wait(3)
        self.driver.get("https://10.242.1.200")
        time.sleep(2)
        self.driver.find_elements_by_xpath("//*[@id=\"rsUserInfo\"]/div[1]/div[1]/div/span")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//*[@id=\"rsUserInfo\"]/div[2]/a[2]/span")[0].click()
        time.sleep(1)
        # self.driver.find_elements_by_class_name("button__text")[0].click()
        self.driver.find_elements_by_xpath("//*[@id=\"app_dialog_container\"]/div[2]/div/div[2]/div/div[4]/div[1]/button/span")[0].click()
        time.sleep(24)
        self.driver.get_screenshot_as_file("./rclist/logout.png")
        allure.attach.file("./rclist/logout.png",name="注销后的截图", attachment_type=allure.attachment_type.JPG)

        # self.driver.get("https://10.242.1.200/por/rclist.csp")

        self.cookies = self.driver.get_cookies()
        with open("rclist/cookie.yaml", "w", encoding="utf-8") as f:
            yaml.dump(self.cookies, f, encoding="utf-8", allow_unicode=True)  # dump下载下来
        self.session = requests.session()
        self.jar = RequestsCookieJar()
        with open("rclist/cookie.yaml", "r") as f:
            self.yaml_cookies = yaml.safe_load(f)  # 从文件中读取下来
        for cookie in self.yaml_cookies:
            self.jar.set(cookie["name"], cookie["value"])
            # with allure
        self.headers = {'Content-Type': 'text/html;charset=UTF-8'}
        self.logout = self.session.get("https://10.242.1.200/por/rclist.csp", headers=self.headers,
                                     cookies=self.jar, verify=False)
        print(self.logout.content.decode())
        time.sleep(3)
        with allure.step("判断注销后是否可以访问资源"):
            assert "unexpected user service" in self.logout.content.decode()




















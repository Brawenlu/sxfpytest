#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 20:29
# @Author  : Brawenlu
# @File    : test_calc.py
# @Software: Sinfor


# 测试类定义
import pytest
import requests
from test_pytest.calc import Calcular
import allure
import allure

# 导入这个类中的方法



@allure.feature("计算器的功能")
class TestCalc:
    # 测试方法定义(不在类中的叫做函数，在类中叫做方法

    def setup_class(self):
        self.calc = Calcular()
        print("开始计算")
        # 实例化方法作用域只在setup(需要实例化calc，后面才可以调用，通过self),其实没必要每个测试用例都实例化可以用setup_class,而不是setup

    def teardown_class(self):
        print("计算结束")

    @allure.story("加法")
    def test_add(self):
        # 实例化方法
        # calc = Calcular()
        # 输出结果，调用方法，定义变量接收方法
        result = self.calc.add(1,1)
        # 实例化后，使用这个方法来定义
        # 断言来判断是否正确
        assert result == 2

    @allure.story("加法2")
    def test_add1(self):
        # 实例化方法
        # calc = Calcular()
        # 输出结果，调用方法，定义变量接收方法
        result = self.calc.add(-1,-1)
        # 断言来判断是否正确
        assert result == -2

    # def test_error(self):
    #     assert False
    @allure.story("加法3")
    def test_add2(self):
        # 实例化方法
        # calc = Calcular()
        # 输出结果，调用方法，定义变量接收方法
        result = self.calc.add(0.3,0.3)
        # 断言来判断是否正确
        assert result == 0.6

    # def test_error(self):
    #     assert False

#1233123
# 指定测试类的方法pytest -vs test_calc.py::TestC2::test_a（文件名::类::方法）-vs详细输出，包括打印  -x遇到报错就停止运行 (pytest test_calc.py -vs  --maxfail=0 失败后继续运行,)
# (pytest test_calc.py -vs  --lf上次失败的测试用例)

@allure.feature("输出文字的方法")
class TestC2():
    def test_a(self):
        print("这是另外的一个测试类的方法")


@allure.feature("提测平台的验证功能")
class Testcanshu():
    #
    # def setup_class(self):
    #     result = requests
    # 参数化必须在测试用例上面第一个是参数，后面是列表形式，如果两个就用[]
    #函数上方以@开头
    @allure.title("成功验证，定制单号为：{danhao}")  #这里可以参数化
    @pytest.mark.parametrize("danhao",[
        "SJJ-2020102901","SSL-2020111201","SJJ-2020122501","EMM-2021010901"
    ])
    @allure.story("验证单号是否正确")
    @allure.link("http://172.22.230.200:8001/td_app/",name="这是一个连接")
    @allure.testcase("http://cs.tp.sangfor.com/#/testcase/home",name="测试用例连接")
    @allure.issue("http://cs.td.sangfor.com/#/defect/problem",name="bug连接")
    def test_web(self,danhao):
        print("开始测试访问")
        with allure.step("访问提测平台"):
            result=requests.get(f"http://172.22.230.200:8001/td_app/2021/td{danhao}/")
        # print(result.text)
        with allure.step("验证测试结果"):
            if danhao in result.text:
                print("找到了定制单号")
            else:assert False
        #加入图片展示结果，第一个图片路径，第二个是方法
        allure.attach.file("D:\\Users\\User\\Desktop\\pic\\570cbb77995bd.jpg",name="美女一手资源",attachment_type=allure.attachment_type.JPG)
        # allure.attach.file()

#allure执行 --alluredir ./result
#展示测试报告 allure serve
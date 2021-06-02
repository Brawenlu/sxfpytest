#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 14:20
# @Author  : Brawenlu
# @File    : test_setup.py
# @Software: Sinfor

# 文件运行前后只会调用一次
def setup_module():
    print("模块级别的 setup")
def teardown_module():
    print("模块级别的 teardown")






# 函数级别不会作用在类当中的

# import pytest 类似的setup,teardown同样更灵活，
# 模块级(setup_module/teardown_module)模块始末，全局的（优先最高）
# 函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
# 类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
# 方法级(setup_method/teardown_methond)开始于方法始末（在类中）
# 类里面的（setup/teardown）运行在调用方法的前后

def setup_function():
    print("函数级别的setup")

def teardown_function():
    print("函数级别的teardown")

def test_func1():
    print("测试函数 func1")


class TestDemo:

    # 只对于个人类才生效
    # 类前后调用etup_class、teardown_class

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    # 测试方法的前后调用setup、teardown
    def setup(self):
        print("默认的方法级别的 setup")

    def teardown(self):
        print("默认的方法级别的 teardown")


    def test_demo1(self):
        print("测试用例test_demo1")


    def setup_method(self):
        print("默认method级别的setup")

    def teardown_method(self):
        print("默认method级别的setup")

    def test_demo2(self):
        print("测试用例test_demo2")

class TestDemo1:

    # 只对于个人类才生效
    # 类前后调用etup_class、teardown_class


    # 测试方法的前后调用setup、teardown

    def test_demo1(self):
        print("测试用例test_demo1")

    def test_demo2(self):
        print("测试用例test_demo2")


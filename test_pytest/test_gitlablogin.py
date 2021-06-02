#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/27 17:38
# @Author  : Brawenlu
# @File    : test_gitlablogin.py
# @Software: Sinfor
import pprint



#判断MD5校验
import gitlab
import requests


class Testlogin():
    def setup_class(self):
        print("开始登陆gitlab")
        self.url = "http://cs.devops.sangfor.org"   #git的地址
        self.accesstoken = "Ze7LuDy5_jBQ2sV2Unyu"    #git的秘钥，在访问令牌里面
        self.project_name = "M7.6.8R2"
        # self.ower = "庞叶蒙52983"


    def teardown_class(self):
        print("登陆完成")

    def test_login(self):
        try:
            gl = gitlab.Gitlab(self.url, self.accesstoken)
            print(gl)
            # self.projects = gl.projects.list(all=True)   #返回的是一个列表，但是不全
            # project = gl.projects.get(self.ower + '/' + self.project_name)
            # print(self.projects)
            # print(type(self.projects))
            projects = gl.projects.list(search='7.6.8R2')  #查找768R2项目
            print(projects)
            for project in projects:
                # print(project.attributes)
                # print(type(project.attributes))
                # print(project.attributes["_links"]["repo_branches"])
                res = requests.get(project.attributes["_links"]["repo_branches"])
                # print(res)
            tmp = gl.projects.get(1134)
            print("tmp值="+str(tmp))
            # cursor = tmp.cursor()
            f = tmp.files.get(file_path="/packs/package/updatefiles/ssl-support.sh",ref="master")
            # print(type(f))
            content = f.decode()   # 第一次decode获得bytes格式的内容
            # print(content)
            content = content.decode()  #以字符串解码,以gb2312编码对字符串str进行解码，获得字符串类型对象,# 第二次decode获得str
            print(content)
            #     print("project.attributes['default_branch'] ", project.default_branch)

            # branches = projects.branches.list()
            # print(branches)

            # print(self.projects)
            # for project in self.projects:   #打印每一个元素的值
            #     # print(project.attributes)
            # self.git_path = "/sslvpn/vpn/custom/M7.6.8R2/blob/科大讯飞股份有限公司SSL-2020092504/packs/package/updatefiles/ssl-support.sh"
            # # f = gl.projects.get(file_path=self.git_path)
            # # print(f)
            # # self.filelist = f.repository_tree(all=True)
            # # print(self.filelist)
            # self.projectsbr = self.projects.get(1134)
            # print(self.projectsbr)
            # self.branch = self.projectsbr.branches.list()
            # print(self.branch)
        except:
            print("error")
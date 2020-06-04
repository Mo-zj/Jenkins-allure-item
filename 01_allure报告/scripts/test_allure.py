import os, sys
sys.path.append(os.getcwd())

import allure, pytest


@allure.feature("登录功能")
class TestAllure():

    @allure.step("测试步骤1：测试登录1")
    @allure.story("正常登录")
    def test_login1(self):
        allure.attach("方法中步骤描述：打印‘login1’")
        print("login1")
        # assert 1

    @allure.story("登录异常")
    @allure.severity("critical")
    def test_login2(self):
        print("login2")
        assert 0


















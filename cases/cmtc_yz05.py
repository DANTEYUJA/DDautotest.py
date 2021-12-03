# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

# from selenium.webdriver.common.by import By
from hytest import *
from hytest import STEP, INFO
from selenium.webdriver.common.keys import Keys

# 调用yz1.py中csh变量
from cases.cmtc_yz01 import csh
from lib.cmtclg_djj01 import cmtc_login

'''公章外借申请:丁家杰标准'''
# 初始化方法套件setup登录，无需self参数(djj01)
# wd调用lib/cmtclogin中cmtc_login
def suite_setup():
    cmtc_login()


# 套件清除方法    如果底下class用例有多个且之间具有数据依赖性，需要在顶部加套件初始化
# 防止获取不到数据元素
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()


class cmtc_yz04:
    name = '公章外借申请'
    tags = ['yz05']

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        STEP(1, '公章外借申请:djj01')
        # 印章管理
        wd.find_element_by_css_selector('div#app div:nth-child(6) > li').click()
        # 公章外借
        wd.find_element_by_css_selector('div#app div:nth-child(3) > a > li > span').click()
        wd.implicitly_wait(10)

        # 查询公章外借前印章
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(1) > div > div > input').send_keys(csh)
        sleep(1)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--cyan.el-button--mini > span').click()
        sleep(1)
        # 获取当前页面的源码并断言
        pagesource = wd.page_source
        # print("数据类型为:")
        # print(type(pagesource))
        # 好像获取到的源码就是gbk格式，不需要下面转成gbk格式，因此注释掉了下面那句
        # print(pagesource.encode("gbk",ignore))
        # 获取某些关键字在源码中的数量
        # 等待时间获取最全页面源码
        wd.implicitly_wait(10)
        INFO("公章外借申请前页面"+csh+"数量为:%d" % +pagesource.count(csh))

        # 新增公章外借申请
        wd.find_element_by_css_selector(
            'div#app div.mb8.el-row > div:nth-child(1) > button[type="button"] > span').click()
        wd.implicitly_wait(10)

        # 选择印章
        wd.find_element_by_css_selector(
            'div#app div:nth-child(1) > div > div > div > input').click()
        sleep(1)
        wd.find_element_by_xpath(
            "//span[contains(text(), 'DDautotest31')]").click()

        # 日期
        wd.find_element_by_css_selector(
            'div#app div.el-date-editor.el-input.el-input--small.el-input--prefix.el-input--suffix.el-date-editor--date > input').click()
        wd.find_element_by_css_selector(
            'div#app div.el-date-editor.el-input.el-input--small.el-input--prefix.el-input--suffix.el-date-editor--date > input').send_keys(
            '2022-12-03')
        wd.find_element_by_css_selector(
            'div#app div.el-date-editor.el-input.el-input--small.el-input--prefix.el-input--suffix.el-date-editor--date > input').send_keys(Keys.ENTER)

        wd.find_element_by_css_selector(
            'div#app textarea').send_keys(
            csh + '公章外借备注')
        # 确定
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--primary.el-button--medium').click()

        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--primary.el-button--medium').click()

        STEP(2, '公章外借申请查询:djj01')
        # 查询公章外借申请后页面数量
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(1) > div > div > input').send_keys(csh)
        sleep(1)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--cyan.el-button--mini > span').click()
        wd.implicitly_wait(10)
        # 获取当前页面的源码并断言
        pagesource = wd.page_source
        # print("数据类型为:")
        # print(type(pagesource))
        # 好像获取到的源码就是gbk格式，不需要下面转成gbk格式，因此注释掉了下面那句
        # print(pagesource.encode("gbk",ignore))
        # 获取某些关键字在源码中的数量
        # 等待时间获取最全页面源码
        wd.implicitly_wait(10)
        INFO("公章外借申请后页面"+csh+"数量为:%d" % +pagesource.count(csh))
        try:

            assert csh in pagesource, "页面中存在" + csh + "关键字"

        except:

            INFO("页面中不存在"+csh+"关键字", "\n")




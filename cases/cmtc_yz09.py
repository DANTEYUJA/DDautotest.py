# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
# from selenium.webdriver.common.by import By
from hytest import *
from hytest import STEP, INFO

# 调用yz1.py中csh变量
from cases.cmtc_yz01 import csh
from lib.cmtclg_db import cmtc_login


# 初始化方法套件setup登录，无需self参数(djj01)
# wd调用lib/cmtclogin中cmtc_login
def suite_setup():
    cmtc_login()


# 套件清除方法    如果底下class用例有多个且之间具有数据依赖性，需要在顶部加套件初始化
# 防止获取不到数据元素
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()

class cmtc_yz09:
    name = '印章作废审核'
    tags = ['yz09']

    '''------------------------------印章作废审核:丁彪------------------------------'''

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        wd.implicitly_wait(10)

        STEP(1, '印章作废申请:djj01')
        # 印章管理
        wd.find_element_by_css_selector('div#app div:nth-child(7) > li').click()
        wd.find_element_by_css_selector('div#app div:nth-child(1) > a > li').click()
        # 印章查询
        wd.find_element_by_css_selector('div#app form > div:nth-child(1) > div > div > input').send_keys(csh)
        wd.find_element_by_css_selector('div#app button[type="button"].el-button.el-button--cyan.el-button--mini > span').click()
        # 点击作废查看
        wd.find_element_by_css_selector(
            'div#app span > button[type="button"] > span').click()
        wd.implicitly_wait(10)
        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,1000)")
        # 审核提交
        wd.find_element_by_css_selector(
            'div#app div:nth-child(2) > button[type="button"].el-button.el-button--primary.el-button--medium').click()
        wd.find_element_by_css_selector(
            'div#app div.el-dialog__body > form > div > div > div > textarea').send_keys(csh+'丁彪作废审核意见')
        wd.find_element_by_css_selector(
            'div#app span > button[type="button"].el-button.el-button--primary.el-button--medium').click()
        wd.implicitly_wait(10)
        INFO(csh + ',丁彪印章作废审核成功')
























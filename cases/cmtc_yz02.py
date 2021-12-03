# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

# from selenium.webdriver.common.by import By
from hytest import *
from hytest import STEP, INFO

# 调用yz1.py中csh变量
from cases.cmtc_yz01 import csh
from lib.cmtclg_db import cmtc_login

'''印章申请审核:丁彪'''
# 初始化方法套件setup登录，无需self参数(djj01)
# wd调用lib/cmtclogin中cmtc_login
def suite_setup():
    cmtc_login()


# 套件清除方法    如果底下class用例有多个且之间具有数据依赖性，需要在顶部加套件初始化
# 防止获取不到数据元素
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()


class cmtc_yz02:
    name = '印章审核'
    tags = ['yz02']

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        STEP(1, '部门负责人审核:dingbiao')
        wd.implicitly_wait(10)
        # 印章管理/印章查询
        wd.find_element_by_css_selector('div#app div:nth-child(7) > li').click()
        wd.find_element_by_css_selector('div#app div:nth-child(1) > a > li').click()
        sleep(2)
        # 查询自动化印章
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[1]/div/div/input').send_keys(csh)
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[4]/div/button[1]/span').click()
        sleep(2)
        # 印章详情页
        wd.find_element_by_css_selector('div#app a > span').click()
        wd.implicitly_wait(20)
        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,800)")
        sleep(2)
        # dingbiao审核提交/弹窗确认
        wd.find_element_by_css_selector(
            'div#app div:nth-child(2) > button[type="button"].el-button.el-button--primary.el-button--medium > span').click()
        wd.find_element_by_css_selector(
            'div#app div.el-dialog__body > form > div > div > div > textarea').send_keys(csh + '自动化印章意见')
        wd.find_element_by_css_selector(
            'div#app span > button[type="button"].el-button.el-button--primary.el-button--medium > span').click()
        wd.implicitly_wait(10)
        sleep(2)
        # # '''alert弹窗'''
        # wd.find_element(By.CLASS_NAME, 'el-message__content')
        # # 打印 弹出框 提示信息
        # INFO(wd.switch_to.alert.text)
        INFO('审核通过')


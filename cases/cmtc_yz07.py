# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

# from selenium.webdriver.common.by import By
from hytest import *
from hytest import STEP, INFO
from selenium.webdriver import ActionChains

# 调用yz1.py中csh变量
from cases.cmtc_yz01 import csh
from lib.cmtclg_djj01 import cmtc_login


# 初始化方法套件setup登录，无需self参数(djj01)
# wd调用lib/cmtclogin中cmtc_login
def suite_setup():
    cmtc_login()


# 套件清除方法    如果底下class用例有多个且之间具有数据依赖性，需要在顶部加套件初始化
# 防止获取不到数据元素
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()


# 鼠标悬停
def hover(by, value):
    wd = GSTORE['wd']
    wd.findElement(by, value)
    ActionChains(wd.driver).move_to_element(wd).perform()


class cmtc_yz07:
    name = '公章外借审核'
    tags = ['yz07']

    '''------------------------------公章外借印章保管人审核:丁家杰标准------------------------------'''

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        wd.implicitly_wait(10)

        STEP(1, '公章外借审核:djj01')
        # 印章管理
        wd.find_element_by_css_selector('div#app div:nth-child(6) > li').click()
        # 公章外借
        wd.find_element_by_css_selector('div#app div:nth-child(3) > a > li > span').click()
        wd.implicitly_wait(10)
        sleep(2)

        # 查询csh公章外借
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(1) > div > div > input').send_keys(csh)
        sleep(2)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--cyan.el-button--mini > span').click()
        sleep(1)
        # 公章外借详情
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div/a/span").click()

        wd.implicitly_wait(10)
        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,1000)")
        sleep(2)
        # djj01点击提交
        wd.find_element_by_css_selector(
            'div#app div:nth-child(2) > button[type="button"] > span').click()
        sleep(1)
        wd.find_element_by_css_selector(
            "div#app div.el-dialog__body > form > div > div > div > textarea").send_keys(csh + 'djj01公章归还意见')
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/section/div[2]/div[2]/div[3]/div/div[3]/span/button[2]").click()
        sleep(2)
        INFO('印章保管人审核外借申请:' + csh + '审核通过')
        wd.implicitly_wait(10)

        '''------------------------------公章外借申请人归还:丁家杰标准------------------------------'''
        STEP(2, '公章外借归还:djj01')
        # 查询csh公章外借
        wd.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div[2]/form/div[1]/div/div/input').send_keys(csh)
        sleep(1)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--cyan.el-button--mini > span').click()
        sleep(1)
        # 公章外借详情
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div/a/span").click()

        wd.implicitly_wait(10)
        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,1000)")
        sleep(2)
        # djj01确认归还
        wd.find_element_by_css_selector(
            'div#app div:nth-child(2) > button[type="button"] > span').click()
        sleep(1)
        wd.find_element_by_css_selector(
            'div#app div.el-dialog__body > form > div > div > div > textarea').send_keys(csh + '公章借用确认归还意见')
        wd.implicitly_wait(10)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--primary.el-button--medium > span').click()
        sleep(2)
        INFO('申请人归还印章:' + csh + '归还成功')
        wd.implicitly_wait(10)

        '''------------------------------公章外借申请人归还:丁家杰标准------------------------------'''
        STEP(3, '公章外借确认归还:djj01')
        # 查询csh公章外借
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[1]/div/div/input').send_keys(csh)
        sleep(2)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--cyan.el-button--mini > span').click()
        sleep(1)
        # 公章外借详情
        wd.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/div/a/span").click()
        sleep(5)
        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,1000)")

        # djj01确认归还
        wd.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div[2]/div[2]/div[2]/button/span').click()

        sleep(1)
        wd.find_element_by_css_selector(
            'div#app div.el-dialog__body > form > div > div > div > textarea').send_keys(csh + '公章借用归还意见')
        sleep(1)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--primary.el-button--medium > span').click()
        sleep(1)
        INFO('印章保管人确认归还印章:' + csh + '确认归还成功')
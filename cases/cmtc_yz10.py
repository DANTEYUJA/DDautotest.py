# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

# from selenium.webdriver.common.by import By
from hytest import *
from hytest import STEP, INFO

# 调用yz1.py中csh变量
from cases.cmtc_yz01 import csh
from lib.cmtclg_qx import cmtc_login


# 初始化方法套件setup登录，无需self参数(djj01)
# wd调用lib/cmtclogin中cmtc_login
def suite_setup():
    cmtc_login()


# 套件清除方法    如果底下class用例有多个且之间具有数据依赖性，需要在顶部加套件初始化
# 防止获取不到数据元素
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()


class cmtc_yz10:
    name = '印章作废审核'
    tags = ['yz09']

    '''------------------------------印章作废审核:齐侠------------------------------'''

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        wd.implicitly_wait(10)

        STEP(1, '印章作废审核:qixia')
        # 印章管理
        wd.find_element_by_css_selector('div#app div:nth-child(3) > li').click()
        wd.find_element_by_css_selector('div#app div:nth-child(1) > a > li').click()
        # 印章查询
        wd.find_element_by_css_selector('div#app form > div:nth-child(1) > div > div > input').send_keys(csh)
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--cyan.el-button--mini > i').click()
        wd.implicitly_wait(10)
        # 点击作废查看
        wd.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[11]/div/button/span').click()
        wd.implicitly_wait(10)
        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,1000)")
        # 审核提交
        wd.find_element_by_css_selector(
            'div#app div:nth-child(2) > button[type="button"].el-button.el-button--primary.el-button--medium').click()
        wd.find_element_by_css_selector(
            'div#app div.el-dialog__body > form > div > div > div > textarea').send_keys(csh + '齐侠作废审核意见')
        wd.find_element_by_css_selector(
            'div#app span > button[type="button"].el-button.el-button--primary.el-button--medium').click()
        sleep(3)

        # 再次印章查询
        wd.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div[2]/form/div[1]/div/div/input').send_keys(csh)
        wd.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div[2]/form/div[4]/div/button[1]/span').click()
        wd.implicitly_wait(10)
        # 点击查看
        wd.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[11]/div/button').click()
        sleep(3)
        SELENIUM_LOG_SCREEN(wd, width='50%')
        # 向下滑动800个像素
        # wd.execute_script("window.scrollBy(0,500)")
        wd.implicitly_wait(10)
        # 查看流程履历 一个src变量只能对应一个调用方法
        # wd.switch_to.frame('iframe')
        # get_attribute获取src属性，get src地址跳转流程履历
        src = wd.find_element_by_id(
            'iframe').get_attribute('src')
        INFO(csh + '流程履历地址为:' + src)
        wd.get(src)
        sleep(2)
        INFO(csh + ',印章作废审核完成')

# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

# from selenium.webdriver.common.by import By
import pyautogui
from hytest import *
from hytest import STEP, INFO
from pykeyboard import PyKeyboard
from selenium.webdriver.common.keys import Keys

# 调用yz1.py中csh变量
from cases.cmtc_yz01 import csh
from lib.cmtclg_djj01 import cmtc_login

'''印章登记:丁家杰标准'''
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
    name = '印章登记'
    tags = ['yz04']

    # 测试用例开始执行
    def teststeps(self):
        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        STEP(1, '新增用印登记:djj01')
        wd.implicitly_wait(10)
        # 印章管理
        wd.find_element_by_css_selector('div#app div:nth-child(6) > li').click()
        # 用印登记
        wd.find_element_by_css_selector('div#app div:nth-child(2) > a > li').click()
        wd.find_element_by_css_selector(
            'div#app div.mb8.el-row > div:nth-child(1) > button[type="button"] > span').click()
        sleep(2)
        # 新增用印登记弹窗
        wd.find_element_by_css_selector('body > div.el-dialog__wrapper > div').click()
        wd.find_element_by_css_selector('div:nth-child(1) > div > div > div > input').click()
        sleep(2)
        # 定位新增用印登记弹窗（黄色为弹窗，蓝色为页面）
        wd.find_element_by_xpath(
            '/html/body/div[2]/div')
        # 定位下拉框列表元素，缩小范围方便下级text定位
        wd.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul")
        wd.find_element_by_xpath("//span[contains(text(),'DDautotest31')]").click()

        wd.find_element_by_css_selector(
            'div.el-dialog__body > form > div:nth-child(3) > div > div.el-date-editor.el-input.el-input--small.el-input--prefix.el-input--suffix.el-date-editor--date > input').send_keys(
            '2022-12-01')
        # 因为会弹窗日期框，所以回车确定
        wd.find_element_by_css_selector(
            'div.el-dialog__body > form > div:nth-child(3) > div > div.el-date-editor.el-input.el-input--small.el-input--prefix.el-input--suffix.el-date-editor--date > input').send_keys(
            Keys.ENTER)
        sleep(1)
        wd.find_element_by_css_selector(
            'div:nth-child(4) > div > div.el-textarea.el-input--medium > textarea').send_keys(
            '自动化印章用印文件')
        wd.find_element_by_css_selector(
            'div > span.el-input-number__increase').click()
        # 上传文件
        wd.find_element_by_css_selector(
            'div.el-upload.el-upload--text > button[type="button"]').click()
        sleep(2)
        pyautogui.write(r'C:\autotest.DOCX')
        pyautogui.press('enter', 2)
        # 上传文件时等待时间
        sleep(3)
        docx = wd.find_element_by_xpath("//a[contains(text(), 'autotest.docx')]")
        INFO('印章登记文件为:' + docx.text)
        # .lower()全部转换为小写
        try:
            assert u"autotest.DOCX".lower() in docx.text
            INFO("文件上传成功")
        except:
            INFO("文件上传失败")

        # 向下滑动800个像素
        # wd.execute_script("window.scrollBy(0,500)")
        wd.find_element_by_css_selector(
            'div:nth-child(7) > div > div > textarea').send_keys('自动化测试用印登记')
        wd.implicitly_wait(10)
        # 确定
        wd.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/div/button[1]').click()
        wd.implicitly_wait(10)

        STEP(2, '用印确认')

        # 查询印章并用印确认
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(1) > div > div > input').send_keys(csh)
        sleep(1)
        wd.find_element_by_css_selector(
            'div#app form > div:nth-child(1) > div > div > input').send_keys(Keys.ENTER)
        wd.implicitly_wait(10)
        # 用印确认
        wd.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[10]/div/button').click()
        sleep(2)
        # 模拟键盘回车
        k = PyKeyboard()
        k.tap_key(k.enter_key)
        wd.implicitly_wait(10)

        STEP(3, '检查状态是否已用印')
        wd.implicitly_wait(10)
        tb = wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/div[2]/div[3]/table/tbody/tr/td[8]/div')
        sts = tb.find_element_by_xpath("//div[contains(text(), '已用印')]")
        INFO('用印状态为:' + sts.text)
        # 断言状态是否已用印
        try:
            assert u"已用印" in sts.text
            INFO("用印成功")
        except:
            INFO("用印失败")
        sleep(2)

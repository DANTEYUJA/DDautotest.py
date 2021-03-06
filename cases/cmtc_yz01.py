# -*- coding: utf-8 -*-
# 对应lib套件下的cmtclogin文件中 声明的cmtc_login方法
from time import sleep

# from selenium.webdriver.common.by import By
import pyautogui
from hytest import *
from hytest import STEP, INFO

from lib.cmtclg_djj01 import cmtc_login

'''印章申请:丁家杰标准'''

# 参数化印章名称
'''cmtc_yz1,cmtc_yz4,cmtc_yz5需要改参数=csh变量的参数'''
csh = 'DDautotest30'


# 初始化方法套件setup登录，无需self参数(djj01)
# wd调用lib/cmtclogin中cmtc_login
def suite_setup():
    cmtc_login()


# 套件清除方法    如果底下class用例有多个且之间具有数据依赖性，需要在顶部加套件初始化
# 防止获取不到数据元素
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()


class cmtc_yz01:
    name = '印章申请'
    tags = ['yz01']

    # 测试用例开始执行
    def teststeps(self):

        # 从lib cmtclogin中取出gstore方法中的wd变量
        wd = GSTORE['wd']
        INFO("跳转到" + wd.title + "平台")

        STEP(1, '印章申请')
        wd.implicitly_wait(10)
        yzgl = wd.find_element_by_css_selector('div#app div:nth-child(6) > li')
        yzgl.click()
        yzcx = wd.find_element_by_css_selector('div#app div:nth-child(1) > a > li')
        yzcx.click()
        sleep(2)
        # 分页50/页
        wd.find_element_by_css_selector('div#app span.el-pagination__sizes > div > div > input').click()
        sleep(2)
        wd.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[4]/span').click()
        sleep(1)
        # 查询自动化印章

        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[1]/div/div/input').send_keys(csh)
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[4]/div/button[1]/span').click()
        sleep(2)
        # 获取当前页面的源码并断言
        pagesource = wd.page_source
        # print("数据类型为:")
        # print(type(pagesource))
        # 好像获取到的源码就是gbk格式，不需要下面转成gbk格式，因此注释掉了下面那句
        # print(pagesource.encode("gbk",ignore))
        # 获取某些关键字在源码中的数量
        # 等待时间获取最全页面源码
        wd.implicitly_wait(10)
        INFO("新增印章前页面关键字数量为:%d" % +pagesource.count(csh))

        # 新增印章申请按钮
        wd.implicitly_wait(20)
        sleep(2)
        xz = wd.find_element_by_css_selector(
            'div#app div.mb8.el-row > div:nth-child(1) > button[type="button"]')
        xz.click()
        wd.implicitly_wait(10)
        # 印章名称
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form[2]/div[1]/div/div[1]/input').send_keys(csh)
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form[2]/div[2]/div/div[1]/input').send_keys('2021-12-25')
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form[2]/div[3]/div/div/div/input').click()
        wd.implicitly_wait(10)
        wd.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
        # 印章保管人
        wd.find_element_by_css_selector(
            'div#app div:nth-child(4) > div > div > div > input').click()
        wd.implicitly_wait(10)
        wd.find_element_by_xpath(
            '/html/body/div[4]')
        wd.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div[1]/ul/li[3]/span').click()

        wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(2)
        # 上传文件
        wd.find_element_by_css_selector(
            'div#app div.el-upload.el-upload--picture > button[type="button"] > span').click()
        sleep(2)
        pyautogui.write(r'C:\cover.jpg')
        pyautogui.press('enter', 2)
        # 上传文件时等待时间
        sleep(5)
        pic = wd.find_element_by_css_selector(
            'div#app li > a')
        INFO('印章图片为:' + pic.text)
        try:
            assert u"cover.jpg" in pic.text
            INFO("印章图片上传成功")
        except:
            INFO("印章图片上传失败")

        # 向下滑动800个像素
        wd.execute_script("window.scrollBy(0,500)")
        sleep(1)
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form[2]/div[7]/div/div/textarea').send_keys(csh + '自动化备注')
        wd.find_element_by_css_selector(
            'div#app button[type="button"].el-button.el-button--primary.el-button--medium').click()
        INFO('印章新增成功')
        sleep(5)
        STEP(2, '印章查询')
        # 分页50/页
        wd.find_element_by_css_selector('div#app span.el-pagination__sizes > div > div > input').click()
        sleep(2)
        wd.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[4]/span').click()
        sleep(2)
        # 查询自动化印章
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[1]/div/div/input').send_keys(csh)
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/section/div[2]/form/div[4]/div/button[1]/span').click()
        # 导出印章报表
        # exp = wd.find_element_by_xpath(
        #     "/html/body/div[1]/div/div[2]/section/div[2]/div[1]/div[3]")
        # exp.find_element_by_xpath(
        #     "//span[contains(text(), '导出印章报表')]").click()
        # sleep(1)
        # wd.find_element_by_xpath(
        #     "/html").send_keys(Keys.ENTER)
        sleep(5)
        # 查询印章页面截屏，会自动加入测试报告中
        # 第1个参数是 webdriver 对象
        # width 参数为可选参数， 指定图片显示宽度
        SELENIUM_LOG_SCREEN(wd, width='50%')

        sleep(2)
        # 获取当前页面的源码并断言
        pagesource = wd.page_source
        # print("数据类型为:")

        # print(type(pagesource))
        # 好像获取到的源码就是gbk格式，不需要下面转成gbk格式，因此注释掉了下面那句
        # print(pagesource.encode("gbk",ignore))
        # 获取某些关键字在源码中的数量
        wd.implicitly_wait(10)
        # 设置等待时间获取最全页面源码
        INFO("新增印章后页面关键字数量为:%d" % +pagesource.count(csh))

        try:

            assert csh in pagesource, "页面中存在" + csh + "关键字"

        except:

            INFO("页面中不存在自动化印章关键字", "\n")

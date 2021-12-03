from time import sleep

from hytest import *
from hytest import INFO
from selenium import webdriver
# 我们在创建 WebDriver 对象后，把它存到了 hytest 全局存储对象 GSTORE 中。 方便其他的代码 获取。
# 公共代码‘登录’放入lib库中
# 声明open_browser对象 打开浏览器
from selenium.webdriver.common.by import By
# 键盘操作
from selenium.webdriver.common.keys import Keys


def cmtc_login():
    INFO('初始化登录:dingbiao')
    # 创建浏览器对象wd/调用驱动打开chrome
    wd = webdriver.Chrome(r'c:\webdrivers\chromedriver.exe')
    # 浏览器最大化
    wd.get_window_size()
    wd.maximize_window()
    # 打开CMTC平台
    wd.get('http://192.168.30.76:8081')
    wd.implicitly_wait(10)

    #账号全选退格删除
    wd.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/input").send_keys(Keys.CONTROL,'a')
    sleep(1)
    wd.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/input").send_keys(Keys.BACKSPACE)
    sleep(1)
    wd.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/input").send_keys('dingbiao')
    #密码全选退格删除
    wd.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input").send_keys(Keys.CONTROL,'a')
    sleep(1)
    wd.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input").send_keys(Keys.BACKSPACE)
    sleep(1)
    wd.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input").send_keys('123456')
    sleep(1)
    # 登录
    wd.find_element(By.CSS_SELECTOR, ".el-button > span > span").click()
    wd.implicitly_wait(10)
    # 以下代码表示将上方变量wd存入GSTORE对象中方便调用 存入是GSTORE在前
    GSTORE['wd'] = wd

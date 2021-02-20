#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project: gpTestTool
@file: test_brower
@time: 2021/2/20/020 17:53
@author: Administrator
@desc: 
"""
import os

from selenium.webdriver import Chrome, ChromeOptions

opt = ChromeOptions()            # 创建Chrome参数对象
opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
project_path = os.path.dirname(__file__)
chrome_drive_path = os.path.join(project_path, "plug", "drive", "chromedriver.exe")
driver = Chrome(chrome_drive_path, options=opt)     # 创建Chrome无界面对象

driver.get('http://www.baidu.com')
print(driver.current_window_handle)
print(driver.page_source)
driver.close()
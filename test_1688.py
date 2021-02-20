#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project: python_pachong_jindong_test
@file: test
@time: 2021/2/20/020 12:42
@author: Administrator
@desc: 
"""
import os

'''
爬取1688商品信息:
    请求url:
        https://www.1688.com/
    提取商品信息:
        1.商品详情页
        2.商品名称
        3.商品价格
        4.成交量
        5.图片链接
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.1688.com/"


def get_good(driver):
    try:

        # 通过JS控制滚轮滑动获取所有商品信息
        js_code = '''
            window.scrollTo(0,5000);
        '''
        driver.execute_script(js_code)  # 执行js代码

        # 等待数据加载
        time.sleep(2)

        # 3、查找所有商品div
        # good_div = driver.find_element_by_id('J_goodsList')
        good_list = driver.find_elements_by_id('sm-offer-list')
        i = 1
        for good in good_list:
            if i < 10:
                # 根据属性选择器查找
                # 商品链接
                good_url = good.find_element_by_xpath("//*[@id='sm-offer-list']/div/div/div[1]/div/a").get_attribute(
                    'href')

                # 商品名称
                good_name = good.find_element_by_xpath('//*[@id=\'sm-offer-list\']/div/div/div[2]').text

                # 商品价格
                good_price = good.find_element_by_xpath("//*[@id='sm-offer-list']/div/div/div[4]/div[2]").text

                # 图片链接
                good_img_url = good.find_element_by_xpath(
                    "/div/div/div[1]/div/a/div").get_attribute('style')

                # 成交量
                good_commit = good.find_element_by_xpath(
                    "//*[@id='sm-offer-list']/div/div/div[@class='sale']/div").text

                good_content = f'''
                            商品链接: {good_url}
                            商品名称: {good_name}
                            商品价格: {good_price}
                            图片链接: {good_img_url}
                            成交量: {good_commit}
                            \n
                            '''
                print(good_content)
                with open('jd.txt', 'a', encoding='utf-8') as f:
                    f.write(good_content)
                i = i + 1
            else:
                break

        # next_tag = driver.find_element_by_class_name('pn-next')
        # next_tag.click()

        time.sleep(2)

        # 递归调用函数
        # if num <= n:
        #     num = num + 1
        #     get_good(driver, num, n)
        # time.sleep(10)

    finally:
        driver.close()


if __name__ == '__main__':
    good_name = input('请输入爬取商品信息:').strip()
    chrome_drive_path = os.path.join(os.path.dirname(__file__), "plug", "drive", "chromedriver.exe")
    driver = webdriver.Chrome(chrome_drive_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # 1、往京东主页发送请求
    driver.get(url)

    # 2、输入商品名称，并回车搜索
    input_tag = driver.find_element_by_id('home-header-searchbox')
    input_tag.send_keys(good_name)
    input_tag.send_keys(Keys.ENTER)
    time.sleep(2)

    get_good(driver)

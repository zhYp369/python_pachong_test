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
爬取京东商品信息:
    请求url:
        https://www.jd.com/
    提取商品信息:
        1.商品详情页
        2.商品名称
        3.商品价格
        4.评价人数
        5.商品商家
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from mongodb_test import mongodb_inser_list

url = "https://www.jd.com/"


def get_good(driver):
    product_list = []
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
        good_list = driver.find_elements_by_class_name('gl-item')
        i = 1
        for good in good_list:
            if i < 10:
                # 根据属性选择器查找
                # 商品链接
                good_url = good.find_element_by_css_selector(
                    '.p-img a').get_attribute('href')

                # 商品名称
                good_name = good.find_element_by_css_selector(
                    '.p-name em').text.replace("\n", "--")

                # 商品价格
                good_price = good.find_element_by_class_name(
                    'p-price').text.replace("\n", ":")

                # 图片链接
                good_img_url = good.find_element_by_css_selector(
                    '.p-img img').get_attribute("src")

                # 评价人数
                good_commit = good.find_element_by_class_name(
                    'p-commit').text.replace("\n", " ")

                product_dict = {
                    "_id": i,
                    "product_url": good_url,
                    "product_name": good_name,
                    "product_price": good_price,
                    "product_img_url": good_img_url,
                    "product_evaluate": good_commit,
                    "creat_time": time.time(),
                    "product_category": "化妆品",
                    "product_classify": "面膜",
                    "product_platform": "京东",
                }
                product_list.append(product_dict)
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

    return product_list


if __name__ == '__main__':
    good_name = input('请输入爬取商品信息:').strip()
    project_path = os.path.dirname(__file__)
    chrome_drive_path = os.path.join(project_path, "plug", "drive", "chromedriver.exe")
    driver = webdriver.Chrome(chrome_drive_path)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 1、往京东主页发送请求
    driver.get(url)

    # 2、输入商品名称，并回车搜索
    input_tag = driver.find_element_by_id('key')
    input_tag.send_keys(good_name)
    input_tag.send_keys(Keys.ENTER)
    time.sleep(2)

    pro_list = get_good(driver)
    id_list = mongodb_inser_list(pro_list)
    print(id_list)


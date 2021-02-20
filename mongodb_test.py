#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project: python_pachong_jindong_test
@file: mongodb_test
@time: 2021/2/20/020 17:05
@author: Administrator
@desc: 
"""



import pymongo

myclient = pymongo.MongoClient("mongodb://root:Wxcrab88gdeii@dds-bp1335de0bdf90b41618-pub.mongodb.rds.aliyuncs.com:3717,dds-bp1335de0bdf90b42116-pub.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-41763908")
mydb = myclient["fdl_crawler_v01"]
mycol = mydb["p_primary_test"]


def mongodb_inser_list(mylist):
    x = mycol.insert_many(mylist)
    print(x.inserted_ids)



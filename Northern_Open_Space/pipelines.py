# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql


class NorthernOpenSpacePipeline(object):
    def insertIntoTable(self, sql):
        # 创建连接
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='Admin_1126',
            db='area_database',
            charset='utf8')  # 要指定编码，否则中文可能乱码

        # 创建游标
        cursor = conn.cursor()

        # 执行查询语句
        cursor.execute(sql)

        # 提交，不然无法保存新建或者修改的数据
        conn.commit()

        # 关闭游标
        cursor.close()

        # 关闭连接
        conn.close()

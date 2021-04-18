#!/usr/bin/python

import pandas as pd
import MySQLdb
from sqlalchemy import create_engine

# (1)读取菜品订单信息表meal_order_info.csv 数据
meal_info=pd.read_csv("~/data/meal_order_info.csv",encoding='gbk')
print(">1..读取菜品订单信息表meal_order_info.csv 数据\n",
        meal_info, "\n")

# (1)将读取菜品订单信息meal_order_info.csv文件中的数据,
#      以csv格式存储到tmp文件夹的orderInfo.csv中
DF_meal_info=pd.DataFrame(meal_info)
DF_meal_info.to_csv('./tmp/orderInfo.csv')

# (2)读取客户信息表users.xlsx数据
users=pd.read_excel("~/data/users.xlsx")
print(">2..读取客户信息表users.xlsx数据\n",
        users, "\n")

# (2)读取的客户信息表users.xlsx中的数据写入到tmp文件夹的userInfo.xlsx中
DF_users=pd.DataFrame(users)
DF_users.to_excel('./tmp/userInfo.xlsx')


# (3)读取订单详情数据库meal_order_detail1.sql数据
connection=MySQLdb.connect("localhost","root","14cwang0","cee_info")
data=pd.read_sql("SELECT * FROM meal_order_detail1",con=connection)
print(">3..读取订单详情数据库meal_order_detail1.sql数据\n",
        data, "\n")

# (3)将读取的meal_order_detail1表中的订单详情数据存储到test1数据表中
engine=create_engine('mysql://root:14cwang0@localhost/cee_info')
DF_data=pd.DataFrame(data)
DF_data.to_sql("test1", con=engine, if_exists='replace')

# （1）对菜品销售数据中重复的数据进行去重。
detail=pd.read_csv('~/data/detail.csv')
print("对菜品销售数据中重复的数据进行去重:  \n", detail.drop_duplicates())

# （2）处理订单详情表缺失值(判断是否存在缺失值、
# 展示存在缺失值的列、去除存在缺失值的行、用“#”填补缺失值、用平均值代替缺失值)
print("判断是否存在缺失值:  \n", detail.isnull().any())
print("展示存在缺失值的列:  \n", detail[detail.isnull().values==True])
print("去除存在缺失值的行:  \n", detail.dropna())
print("用“#”填补缺失值:  \n", detail.fillna('#'))
print("用平均值代替缺失值:  \n", detail.fillna(detail.mean()))

# （3）处理菜品销售数据中"销售量counts"、"销售价amounts"异常值
DF_detail=pd.DataFrame(detail)
print("处理前:\n",DF_detail[['counts','amounts']].describe().T)
newdetail1=detail.replace(detail['counts'].max(),detail['counts'].mean())
newdetail1=newdetail1.replace(newdetail1['amounts'].max(),newdetail1['amounts'].mean())
DF_newdetail1=pd.DataFrame(newdetail1)
print("处理后:\n",DF_newdetail1[['counts','amounts']].describe().T)

# -*- coding: utf-8 -*-
"""
绘制散点图
"""
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlsxwriter
from pylab import *
import pandas as pd
from pandas import DataFrame, Series


#style of excl
#style = xlsxwriter.add_format('font: name Times New Roman')
mpl.rcParams['font.sans-serif'] = ['SimHei']
datafile1 = u'E:\\mypython\\xlsx\\itaobao.xlsx'  # 文件所在位置
datafile2 = u'E:\\mypython\\xlsx\\itaobao2.xlsx'  # 文件所在位置

#str to int of sale
def salesToInt(sales):
    i = 0
    while(i < len(sales)):
        print(type(sales[0]),type(sales[1]),type(sales[2]))
        if isinstance(sales[i],(str))and '万' in sales[i]:
             sales[i] = long(float(sales[i][:len(sales[i]) - 1]) * 10000)
        sales[i] = np.int64(sales[i])

        i += 1

    return sales

#create excl
def createExcl(sales, addresses, names):
    # create new excl
    workbook = xlsxwriter.Workbook('xlsx/itaobao2.xlsx')  # 创建excel对象
    bold_format = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', u'名称', bold_format)
    worksheet.write('C1', u'销量', bold_format)
    worksheet.write('B1', u'发货地点', bold_format)
    sales = list(salesToInt(sales))
    print('sales intt=',sales)
    i = 1
    while(i < len(sales)):
        worksheet.write_number(i, 2, sales[i])
        i += 1

    i = 1
    for name in names:
        worksheet.write_string(i, 0, name)
        i += 1

    i = 1
    for address in addresses:
        worksheet.write_string(i, 1, address)
        i += 1

    workbook.close()

def readExcl(path):
    # 读取文件
    data = pd.read_excel(path, encoding_override='utf-8')  # 如果是csv文件则用read_csv
    print("显示缺失值，缺失则显示为TRUE：\n", data.isnull())#是缺失值返回True，否则范围False
    print("------------------\n用均值插补后的数据data：\n", data.fillna((data.mean()).astype(long)))

    examDf = DataFrame(data)

    # 去重
    #print(examDf.duplicated())  # 判断是否有重复行，重复的显示为TRUE，
    #examDf.drop_duplicates()  # 去掉重复行

    # 指定某列判断是否有重复值
    #print(examDf.duplicated('销量'))  # 判断name列是否有重复行，重复的显示为TRUE，
    examDf.drop_duplicates('销量')  # 去掉重复行
    #data.dropna()

    # if(path == datafile2):
    #    examDf.drop_duplicates(['名称', '发货地点', '销量'])  # 去掉重复行

    # 根据多列判断是否有重复值
    #print(examDf.duplicated(['name', 'sex', 'birthday']))  # 判断name,sex,birthday列是否有重复行，重复的显示为TRUE，
    #examDf.drop_duplicates(['name', 'sex', 'birthday'])  # 去掉重复行

    worksheet = xlrd.open_workbook(path, encoding_override='utf-8')   #打开excel文件
    #sheet_names = worksheet.sheet_names()    #获取excel中所有工作表名
    sheet1 = worksheet.sheet_by_index(0)     #根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
    #rows = sheet1.row_values(3)   #表示获取Sheet2中第4行数据
    if(path == datafile1):
        names = sheet1.col_values(1)   #表示获取Sheet2中第4行数据
        addresses = sheet1.col_values(4)   #表示获取Sheet2中第10列数据（数据保存为list）
        sales = sheet1.col_values(5)   #表示获取Sheet2中第10列数据（数据保存为list）

    if(path == datafile2):
        names = sheet1.col_values(0)   #表示获取Sheet2中第4行数据
        addresses = sheet1.col_values(1)   #表示获取Sheet2中第10列数据（数据保存为list）
        sales = sheet1.col_values(2)   #表示获取Sheet2中第10列数据（数据保存为list）

    # 根据多列判断是否有重复值
    # print(examDf.duplicated(['商品标题', '地址', '销量']))  # 判断name,sex,birthday列是否有重复行，重复的显示为TRUE，
    #examDf.drop_duplicates(['销量'])  # 去掉重复行
    print(examDf.describe())
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    #sales = list(salesToInt(sales[1:]))
   #while(i < len(sales)):
    #    if(sales[i] < 10):
    #        sales[i] = data.median()
      #  i += 1

    #print(sales)
    #print(sales[i])
    return (sales, addresses, names)

def dealData(datafile):
    tu = readExcl(datafile)
    addresses = tu[1][1:]
    sales = tu[0][1:]
    names = tu[2][1:]
    print("what")
    print(names)
    print(addresses)
    print(sales)
    print(sales[0],type(sales[0]))
    #if (datafile == datafile1):
    sales = list(salesToInt(sales))
    print(sales)

    xadd = list(set(addresses))
    xadd.sort(key = addresses.index)

    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率

    plt.tick_params(labelsize=8)
    # 绘制散点图
    plt.title("位置与销售量的关系")
    plt.ylabel("销售量", fontproperties="SimHei")
    plt.xlabel("发货地点", fontproperties="SimHei")
    plt.xticks(range(len(xadd)), xadd, rotation=270)
    # plt.scatter(xadd_len, xadd)
    print(len(addresses))
    print(len(sales),'----------',type(sales[0]))
    plt.scatter(addresses, sales, c='b')
    # 设置坐标轴范围
    plt.ylim((0, 26000))
    # 不显示坐标轴的值
    # plt.xticks(())
    # plt.yticks(())
    plt.show()
    if(datafile == datafile1):
        createExcl(sales, addresses, names)

if __name__ == '__main__':
    dealData(datafile1)
    #readExcl(datafile2)
    dealData(datafile2)




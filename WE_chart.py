#!/bin/usr/python3
# -*- coding: utf-8 -*-
# 简单柱状图
#文件名:baseHistogram.py

import matplotlib
import matplotlib.pyplot as plt
import time
from pylab import mpl
import pandas as pd

from cnsort import cnsort

path = "xlsx/names.csv"
mpl.rcParams['font.sans-serif'] = ['SimHei']

#设置横纵坐标的名称以及对应字体格式
font2 = {'family' : 'SimHei',
'weight' : 'normal',
'size'   : 15,
}

def opendata(path):
    df = pd.read_csv(path)
    list_label = df.columns.values
    list_data = df.values.tolist()

    names1 = set([])
    names2 = set([])
    counts = []
    for name in list_data:
        counts.append(len(name[1].split(' ')))
        #count.sort(key = count.index)
        names1.add(name[0])
        names2.add(name[0]+str(len(name[1].split(' '))))

    return (cnsort(list(names1)), cnsort(list(names2)), list(counts))

def bar_graph():
    mpl.rcParams['font.sans-serif'] = ['FangSong']              # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False                  # 解决保存图像是负号'-'显示为方块的问题
    data = opendata(path)

    names1 = data[0]
    names2 = data[1]
    counts1 = data[2]

    setcounts = list(set(counts1))
    setcounts.sort(reverse=True)
    print(setcounts)
    counts2 = []
    for name2 in names2:
        for count1 in setcounts:
            print(name2+':'+str(count1))
            if str(count1) in name2:
                counts2.append(count1)
                break

    plt.tick_params(labelsize=8)
    plt.rcParams['savefig.dpi'] = 300                           # 图片像素
    plt.rcParams['figure.dpi'] = 300                            # 分辨率

    plt.bar(names1, counts2)                              # 如果不指定color，所有的柱体都会是一个颜色

    plt.xticks(range(len(names1)), names1, rotation=270)
    plt.xlabel(u"姓名", font2)                 # 指定x轴描述信息
    plt.ylabel(u"联系人数量", font2)           # 指定y轴描述信息
    plt.title("近期微信联系人数量统计表", font2)   # 指定图表描述信息
    plt.ylim(0, 15)
    plt.tight_layout()# 指定Y轴的高度
    plt.savefig('{}.jpg'.format(time.strftime('%Y%m%d%H%M%S')))  # 保存为图片
    plt.show()

if __name__ == '__main__':
    bar_graph()
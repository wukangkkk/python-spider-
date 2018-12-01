#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.style.use('ggplot')
fig=plt.figure(figsize=(8,5))#设置图片的大小
color1='#6D6D6D'
columns=['index','name','star','releasetime','score']
#index_col='index'将表格索引设置为index
df=pd.read_csv('猫眼top100.csv',encoding='utf-8',header=None,names=columns,index_col='index')
#按分数降序排列
df_score=df.sort_values('score',ascending=False)

name1=df_score.name[0:10]#x轴坐标
print(name1)
score1=df_score.score[0:10]#y轴坐标
print(score1)
#绘制条行图,range(10)能保证x轴的正确顺序
plt.bar(range(10),score1,tick_label = name1)
plt.ylim((9,9.8))#设置y轴的范围
plt.title('电影评分最高top10',color=color1)
plt.xlabel('电影名称')
plt.ylabel('评分')
# for x,y in enumerate(list(score1)):
#     plt.text(x,y+0.01,'%s'%round(y,1),ha='center',color=color1)
pl.xticks(rotation=270)
plt.show()













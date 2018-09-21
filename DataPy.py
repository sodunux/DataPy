import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from pandas import Series,DataFrame
from random import randint

class DataPlot:

	def __init__(self):
		plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
		pass
	def Demo(self):
		demo_x=np.arange(100)
		demo_y=demo_x*demo_x
		demo_z=demo_x*2
		demo_r=self.GenRandomInt(0,100,100)
		self.ShowLine(demo_x,demo_r,"随机整数")
		self.ShowPoint(demo_x,demo_r,"随机整数")
		#self.ShowLine(demo_x,demo_y,"X平方")
		#self.ShowPoint(demo_x,demo_y,"X平方散点图")
		#self.MapPosition(2,2,1)
		#self.MapLine(demo_x,demo_y,"X平方线形图")
		#self.MapPosition(2,2,2)
		#self.MapPoint(demo_x,demo_y,"X平方散点图")
		#self.MapPosition(2,2,3)
		#self.MapBar(demo_x,demo_y,"X平方柱状体")
		#self.MapPosition(2,2,4)
		#self.MapPie(demo_x,demo_y)
		#self.MapShow()
		#self.ShowPie(demo_x,demo_y)
		

	def MapPosition(self,row,column,position):
		plt.figure(1)
		plt.subplot(row,column,position)

	def MapLine(self,x,y,linelabel):
		#仅仅设置数据到Axes中
		plt.xlabel("x")
		plt.ylabel("y")
		plt.plot(x,y,label=linelabel)
		plt.legend()
		plt.grid(True)
		#plt.axis([0,10,0,100])	

	def MapPoint(self,x,y,pointlabel):
		#仅仅设置数据到Axes中
		plt.xlabel("x")
		plt.ylabel("y")
		plt.scatter(x,y,label=pointlabel)
		plt.legend()
		plt.grid(True)

	def MapPie(self,x,y):
		#仅仅设置数据到Axes中
		plt.pie(y,labels=x)
		plt.legend()
		plt.grid(True)

	def MapBar(self,x,y,barlabel):
		#仅仅设置数据到Axes中
		plt.bar(x,y,label=barlabel)
		plt.legend()
		plt.grid(True)

	def MapShow(self):
		plt.show()

	def ShowLine(self,x,y,linelabel):
		#简单显示x和y的数据
		plt.xlabel("x")
		plt.ylabel("y")
		plt.plot(x,y,label=linelabel)
		plt.legend()
		plt.grid(True)
		#plt.axis([0,10,0,100])
		plt.show()

	def ShowPoint(self,x,y,pointlabel):
		#显示散点图
		plt.xlabel("x")
		plt.ylabel("y")
		plt.scatter(x,y,label=pointlabel)
		plt.legend()
		plt.grid(True)
		plt.show()

	def ShowPie(self,x,y):
		#显示饼图
		plt.pie(y,labels=x)
		plt.legend()
		plt.grid(True)
		plt.show()

	def ShowBar(self,x,y,barlabel):
		#显示柱状图
		plt.bar(x,y,label=barlabel)
		plt.legend()
		plt.grid(True)
		plt.show()

	def GenRandomInt(self,min,max,len):
		return np.random.randint(min,max,size=len)

class DataNumpy:
	def __init__(self):
		self.dp=DataPlot()
		pass
	def Demo(self):
		self.GenRandomInt()
		pass
	def GenRandomInt(self,rmin,rmax,rsize):
		dy=np.random.randint(rmin,rmax,size=rsize)
		return dy

	def GenRandom(self,rsize):
		dy=np.random.random(size=rsize)
		return dy

	def Base(self):
		data=self.GenRandom((2,3))
		data10=data*10
		dataint=data10.astype(np.int32)
		dat2=self.GenRandomInt(0,100,100)
		dat2.sort()
		#print(dataint)
		#print(dat2)
		np.save('data2',dat2)
		dat3=np.load('data2.npy')
		#print(dat3)
		dat4=self.GenRandomInt(0,10,(2,3))
		dat5=self.GenRandomInt(0,100,(3,2))
		dat6=np.dot(dat4,dat5)
		print(dat4)
		print(dat5)
		print(dat6)
		print(np.trace(dat6))
		#dat6=dat4

		pass

class DataPandas:
	def __init__(self):
		plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
		pass
	def Demo1(self):
		obj=Series(range(1,5))
		print(obj)
		print(obj.values)
		print(obj.index)
		print(type(obj.values))
		print(type(obj.index))
		pass

	def Demo2(self):
		obj=Series([4,7,-5,3],index=['d','b','a','c'])
		print(obj.index)

	def Demo3(self):
		filename=open('601069.csv',encoding='gbk')
		df=pd.read_csv(filename)
		spj=df['收盘价']
		zgj=df['最高价']
		zdj=df['最低价']
		#print(df['收盘价'])
		#print(df['最高价'])
		#print(df['最低价'])
		spj.plot()
		zgj.plot()
		zdj.plot()
		plt.show()




if __name__ == '__main__':
	#dp=DataPlot()
	#dp.Demo()
	#dn=DataNumpy()
	#dn.Base()
	ddp=DataPandas()
	ddp.Demo3()
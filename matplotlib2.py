#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

#绘制散点图
fig = plt.figure()
a = fig.add_subplot(3,3,1)
n=128
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
#plt.axes([0.025,0.025,0.95,0.95])
a.scatter(X,Y,s=75,c = T,alpha=.5)#T控制颜色
plt.xlim(-1.5,1.5)
plt.xticks([])
plt.ylim(-1.5,1.5)
plt.yticks([])
plt.axis()
plt.title("scatter")
plt.xlabel("x")
plt.ylabel("y")

#画柱状图
fig.add_subplot(3, 3, 2)
n = 10
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='red',edgecolor='white')#颜色

for x,y in zip(X,Y1):
    plt.text(x+0.4,y+0.05,'%0.2f'%y,ha='center',va = 'bottom')
for x,y in zip(X,Y2):
    plt.text(x+0.4,-y-0.05,'%0.2f'%y,ha='center',va = 'bottom')
#饼图
fig.add_subplot(333)
n = 20  #20个部分
Z = np.ones(n)
Z[-1]*=2  #最后一个是2
plt.pie(Z,explode=Z*0.05,colors=['%f'%(i/float(n)) for i in range(n)],
        labels=['%.2f'%(i/float(n))for i in range(n)])#把标签打印出来
plt.gca().set_aspect('equal')
plt.xticks([]),plt.yticks([])


#极坐标的图
fig.add_subplot(334,polar = True)
n = 20
theta = np.arange(0.0,2*np.pi,2*np.pi/n)
radii = 15*np.random.rand(n)
plt.plot(theta,radii)


#热力图heat map
fig.add_subplot(335)
from matplotlib import cm
data = np.random.rand(3,3)
cmap = cm.Reds#红色系
map = plt.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=0,vmax=1)
#插值法 最近的
#3D图

from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(336,projection="3d")
ax.scatter(1,1,5,s=100)

#热图 hot map
fig.add_subplot(313)
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)
plt.contourf(X,Y,f(X,Y),8,alpha = 0.5, cmap = plt.cm.hot)
plt.savefig("./fig.png")
plt.show()
#coding=utf-8
#基本的线图绘制
import numpy as np
def main():
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)#定义正弦余弦函数
    plt.figure(1)
    #plt.plot(x, c)
    #plt.plot(x, s)
    plt.plot(x, c, color = "blue",linewidth = 1.5,linestyle="-")
    plt.plot(x, s, color = "green",linewidth = 1.5,linestyle="-")
    plt.title("cos and sin")
    ax = plt.gca()#修改轴
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    #编辑数字
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white", edgecolor="None",alpha = 0.2))
    plt.legend("c",loc="upper left",)#在左上方放标签
    plt.grid()
    plt.axis([-2,2,-0.5,1])#修改显示范围（横纵轴）
    plt.fill_between(x,np.abs(x) < 0.4, c, c > 0.5, color="green",alpha = 0.5)#填充
    t = 1
    plt.plot([t,t],[0,np.cos(t)], "k", linewidth=3, linestyle="--")
    plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),textcoords="offset points",arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3,rad=.2"))
    plt.show()
if __name__=="__main__":
    main()


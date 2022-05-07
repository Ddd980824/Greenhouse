#导入matplotlib的所有内容
from pylab import *
#创建一个10*6点（point）的图，并设置分辨率为80
figure(figsize=(10,6),dpi=80)
#创建一个新的1*1的子图，接下来的图样绘制在其中的第1块（也是唯一的一块）
subplot(1,1,1)
#x是一个numpy数组，包含了从-π到+π等间隔的256个值；c，s则分别是这256个值对应的余弦和正弦函数值组成的numpy数组
x = np.linspace(-np.pi,np.pi,256,endpoint = True)
c,s = np.cos(x),np.sin(x)
#绘制余弦曲线，使用蓝色、连续的、宽度为2.5（像素）的线条
plot(x,c,color="blue",linewidth=2.5,linestyle="-")
#绘制正弦曲线，使用红色色、连续的、宽度为2.5（像素）的线条
plot(x,s,color="red",linewidth=2.5,linestyle="-")
#设置图片边界
xmin,xmax = x.min(),x.max()
ymin,ymax = c.min(),c.max()
dx = (xmax - xmin) * 0.05
dy = (ymax - ymin) * 0.05
xlim(xmin - dx,xmax + dx)
ylim(ymin - dy,ymax + dy)
#设置记号
xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
yticks([-1,0,+1])
#设置记号(标签使用π）
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1,+1],
       [r'$-1$',r'$+1$'])
#移动脊柱
ax  = gca()
#设置右边和顶部轴线的颜色为无色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#通过axes对象设置刻度显示的位置，将x轴的刻度设置在轴线下方
ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom']获取底部的轴，通过set_position方法，设置底部轴的位置
#set_position(('data',0))表示设置底部轴移动到竖轴的0坐标位置
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#添加图例
plot(x,c,color="blue",linewidth=2.5,linestyle="-",label="cosine")
plot(x,s,color="red",linewidth=2.5,linestyle="-",label="sine")
#图例放置在图片的左上角
legend(loc='upper left')
#标注特殊点（2π/3）
t = 2*np.pi/3
#标出特殊点并向横坐标引垂线
plot([t,t],[0,np.cos(t)],
         color ='blue',  linewidth=1.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='blue')
#annotate函数用来添加图形内容细节的指向型注释文本
annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$', #注释内容
             xy=(t, np.cos(t)),  xycoords='data', #xy：被注释图形内容的坐标位置；xycoords：坐标系统，此处与直线图同坐标
             xytext=(-90, -50), textcoords='offset points', fontsize=16, #xytext：注释文本的位置坐标；textcoords：标签系统坐标；此处设置文本偏移标注点
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #arrowstyle：箭头的样式；connectionstyle：用于设置连接方式，可以设置弧度等
plot([t,t],[0,np.sin(t)],
         color ='red',  linewidth=1.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')
annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)),  xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#放大坐标轴刻度标签，并设置白透明白色底色防止图像遮盖
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 )) #bbox：增加边框样式；
    # facecolor：背景颜色；edgecolor：边框线条颜色；edgewidth：边框线条大小。
show()
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rank = ["", "第1名", "第2名", "第3名", "第4名", "第5名", "第6名", "第7名", "第8名", "第9名", "第10名"]
colors = dict(zip(rank, ['', '#abd0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50', '#00BFFF', '#ADD8E6', '#32CD32']))
#df = pd.read_csv('1.csv', encoding='gbk', usecols=['time_stamp', 'rank', 'num', 'title'])
df = pd.read_csv('weibo.csv', usecols=['time_stamp', 'rank', 'num', 'title'])  # usecols相当于给表格的每列数据命名
print(df['time_stamp'])  # 取出内容,结果如下
'''
0      2021/08/11 12:07
1      2021/08/11 12:07
2      2021/08/11 12:07
         ...
677    2021/08/11 13:12
678    2021/08/11 13:12
679    2021/08/11 13:12         
'''
fig, ax = plt.subplots(figsize=(15, 8))
def draw(time_stamp):
    print(time_stamp)
    dff = df[df['time_stamp'].eq(time_stamp)].sort_values(by='num', ascending=True).head(10)
    print(dff)
    ax.clear()
    ax.barh(dff['rank'][::-1], dff['num'], color=[colors[i] for i in dff['rank']])
    # ax.barh(dff['rank'][::-1], dff['num'])  # 根据排名从高到底画横向直方图
    dx = dff['num'].max()/200
    for i, (num, title) in enumerate(zip(dff['num'], dff['title'])):
        print(num, title)
        ax.text(dx, i, title, size=15)         # 把热搜内容按顺序放到直方图中
        ax.text(num+dx, i, num, size=20, color='#444444')   # 把微博热度放到直方图顶端
    numberone= '热搜榜 NO.1'+list(dff['title'])[-1]   # 把热搜第一取出来
    ax.text(0.15, 1.07, numberone, transform=ax.transAxes, color='#444444', size=30)  # 放到图的顶端位置
    ax.text(0.83, 0.1, time_stamp, transform=ax.transAxes, color='#777777', size=30)  # 将时间戳放到右下角
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))  # 给x轴坐标数据科学计数
    ax.xaxis.set_ticks_position('top')  # 将x轴坐标放到上端
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.margins(0, 0.01)  # 缩放坐标轴
    ax.grid(which='major', axis='x', linestyle='-')  # 画网格虚线
    ax.set_axisbelow(True)  # 确保网格虚线在图形后方
    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(rank)))
    ax.set_yticklabels(rank[::-1])


def sortTime(list1):  # 保证时间戳顺序不改变
    list2 = []
    for i in list1:
        if i in list2:
            pass
        else:
            list2.append(i)
    return list2
# draw('2020/2/19 19:29')

animator = animation.FuncAnimation(fig, draw, frames=sortTime(df['time_stamp']), interval=50)
plt.show()
HTML(animator.to_jshtml('1.mp4'))








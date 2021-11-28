import time
import requests
import schedule as schedule
import re
import pandas as pd

url = 'https://s.weibo.com/top/summary'
headers = {
    'Host': 's.weibo.com',
    'Cookie': 'SUB=_2AkMWxH1yf8NxqwJRmfwcz2niaIV-zQ3EieKgmIypJRMxHRl-yT8XqnEYtRB6PURTnQqf3aN1Rt_jgR0k7RAKzLBdG-Vh; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5ifPWQ_C-DRzEdcjCNHT0p; SINAGLOBAL=6930158664156.274.1637413437234; _s_tentry=-; Apache=9348196171204.361.1637420152280; ULV=1637420152291:3:3:3:9348196171204.361.1637420152280:1637419847567',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

titles = re.compile('Refer=top" target="_blank">(.*?)</a>', re.S)
nums = re.compile(r'<span> (\d+)</span>')
df = []
columns = ['time_stamp', 'rank', 'num', 'title']  # excel的标题栏

m = 1
def run():
    global m
    print('第{}次运行'.format(m) + '=' * 50)  # 可以观察到第几次运行
    m += 1
    response = requests.get(url, headers=headers)
    # print(response.text)
    time_stamp = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))  # 时间戳
    for i in range(1, 11):
        rank = '第{}名'.format(i)    # 微博排名
        # print(rank)
        num = re.findall(nums, response.text)[i-1]  # 微博热度
        # print(num)
        title = re.findall(titles, response.text)[i-1]  # 微博内容
        # print(title)
        # 存储数据
        df.append([time_stamp, rank, num, title])
        d = pd.DataFrame(df, columns=columns)
        d.to_excel("微博前十热搜1.xlsx", index=False)

schedule.every(60).seconds.do(run)
while True:
    schedule.run_pending()


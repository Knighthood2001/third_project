import time
import requests
import schedule as schedule
import re
import csv
url = 'https://s.weibo.com/top/summary'
headers = {
    'Host': 's.weibo.com',
    'Cookie': 'SUB=_2AkMWxH1yf8NxqwJRmfwcz2niaIV-zQ3EieKgmIypJRMxHRl-yT8XqnEYtRB6PURTnQqf3aN1Rt_jgR0k7RAKzLBdG-Vh; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5ifPWQ_C-DRzEdcjCNHT0p; SINAGLOBAL=6930158664156.274.1637413437234; _s_tentry=-; Apache=9348196171204.361.1637420152280; ULV=1637420152291:3:3:3:9348196171204.361.1637420152280:1637419847567',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
m = 1
titles = re.compile('Refer=top" target="_blank">(.*?)</a>', re.S)
nums = re.compile(r'<span> (\d+)</span>')
print('time_stamp,rank,num,title')
with open('weibo.csv', 'w') as f:
    f.write('time_stamp,rank,num,title\n')
def run():
    global m
    print('第{}次运行'.format(m) + '=' * 50)
    m += 1
    response = requests.get(url, headers=headers)
    # print(response.text)
    time_stamp = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))  # 时间戳
    # if os.path.exists('weibo1.csv'):  # 如果文件已经存在，则删除文件
    #     os.remove('weibo1.csv')

    with open('weibo.csv', 'a', newline='', encoding='utf-8', errors='ignore') as f:
        w = csv.writer(f)
        for i in range(1, 11):
            rank = '第{}名'.format(i)    # 微博排名
            # print(rank)
            num = re.findall(nums, response.text)[i-1]  # 微博热度
            # print(num)
            title = re.findall(titles, response.text)[i-1]  # 微博内容
            # print(title)
            title_new = str(title).replace(' ', '')

            w.writerow([time_stamp, rank, num, title_new])  # csv 的writerow 函数只能写入一个序列，比如 list 或 array.

schedule.every(60).seconds.do(run)
while True:
    schedule.run_pending()



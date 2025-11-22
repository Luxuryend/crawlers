import csv
import os
import time
from datetime import datetime
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions()
co.headless()

browser = ChromiumPage(co)
browser.listen.start('comment/list')
browser.get('https://www.douyin.com/video/7572943428657483054')

os.remove('douyin.csv')  # 防止文件混乱

with open('douyin.csv', 'a', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['昵称', '地区', '日期', '评论'])
    for p in range(1, 21):
        r = browser.listen.wait()
        json_data = r.response.body
        jobs = json_data['comments']
        for i in jobs:
            name = i['user']['nickname']
            location = i['ip_label']
            date = datetime.fromtimestamp(i['create_time'])
            comments = i['text']
            writer.writerow([name, location, date, comments])
        browser.scroll.to_see('x://*[@id="douyin-right-container"]/div[2]/div/footer')
        print(f'已爬取第{p}页')
        time.sleep(0.3)

print('completed')
browser.close()

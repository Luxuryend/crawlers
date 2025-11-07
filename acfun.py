import requests
import re
import json
import os
from lxml import etree
from tqdm import tqdm

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}


# 读取m3u8列表
def get_m3u8_list(u):
    r = requests.get(u, headers=headers)
    html = etree.HTML(r.text)
    t = html.xpath('//*[@id="main-content"]/div[1]/div[3]/h1/span/text()')[0]
    info = re.findall('"currentVideoInfo":(.*?)"viewCountShow":', r.text, re.S)[0][:-1]
    json_data = json.loads(info)
    m_url = json.loads(json_data['ksPlayJson'])['adaptationSet'][0]['representation'][0]['url']
    return t, m_url


# 提取ts链接
def get_ts_files(u):
    r = requests.get(u, headers=headers)
    ts_l = re.findall(',\n(.*?)\n#EXTINF', r.text)
    return ['https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + i for i in ts_l]


# 下载合并文件
def download_combine(t, tsl):
    print('downloading')
    for i in tqdm(tsl):
        r = requests.get(i, headers=headers)
        with open(f'video/{t}.mp4', 'ab') as f:
            f.write(r.content)


if __name__ == '__main__':
    url = 'https://www.acfun.cn/v/ac47977513'  # 随便挑个视频链接
    if not os.path.exists("video"):
        os.mkdir("video")
    title, m3u8_url = get_m3u8_list(url)
    ts_lists = get_ts_files(m3u8_url)
    download_combine(title, ts_lists)

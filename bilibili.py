import requests
import re
import json
import os
from lxml import etree

url = 'https://www.bilibili.com/video/BV1nV1sBSEQY'

headers = {
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)
title = etree.HTML(r.text).xpath('//*[@id="viewbox_report"]/div[1]/div[1]/h1/text()')[0]

window_js = re.findall('window.__playinfo__=(.*?)</script>', r.text, re.S)[0]
json_data = json.loads(window_js)
video_link = json_data['data']['dash']['video'][0]['baseUrl']
audio_link = json_data['data']['dash']['audio'][0]['baseUrl']

r_video = requests.get(video_link, headers=headers).content
with open(f'video/tem.mp4', 'wb') as f:
    f.write(r_video)
r_audio = requests.get(audio_link, headers=headers).content
with open(f'video/tem.mp3', 'wb') as f:
    f.write(r_audio)

# "D:\ffmpeg-2025-11-06-git-222127418b-full_build\bin\ffmpeg.exe"
cmd = fr'D:\ffmpeg-2025-11-06-git-222127418b-full_build\bin\ffmpeg.exe -i video/tem.mp4 -i video/tem.mp3 -c:v copy -c:a aac -strict experimental video/temp.mp4'
os.system(cmd)
os.rename('video/temp.mp4', f'video/{title}.mp4')

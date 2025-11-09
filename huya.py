import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}


def download_file(vid):
    params = {
        'videoId': vid,
        'uid': '',
        '_': '1762582674441',
    }
    u = 'https://liveapi.huya.com/moment/getMomentContent'
    r = requests.get(u, params=params, headers=headers)
    j = r.json()['data']['moment']
    title = j['title']
    video_url = j['videoInfo']['definitions'][0]['url']
    content = requests.get(video_url, headers=headers).content
    with open(f'video/{title}.mp4', 'wb') as f:
        f.write(content)
        print('downloaded', title)


if __name__ == '__main__':
    url = 'https://www.huya.com/video/play/1083581586.html'
    videoId = re.findall(r'\d+', url)[0]
    download_file(videoId)

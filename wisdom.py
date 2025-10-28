import requests
from lxml import etree

url = 'http://mingyan.hanyupinyin.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}


def get_article(u):
    r = requests.get(u, headers=headers)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    t = html.xpath('/html/body/div[2]/div[1]/p/text()')
    text = ''.join(t)
    title = html.xpath('/html/body/div[2]/div[1]/h1/text()')[0]
    return title, text


def get_links():
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    div = html.xpath('/html/body/div[2]/ul[3]')[0]
    links = div.xpath('.//a/@href')
    return links


sub_links = get_links()

for li in sub_links:
    title, text = get_article('http://mingyan.hanyupinyin.cn' + li)
    with open('./saying/' + title + '.txt', 'w', encoding='utf-8') as f:
        f.write(text)

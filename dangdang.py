import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}


def getData(k: str, p: str):
    url = f'https://search.dangdang.com/?key={k}&act=input&page_index={p}'
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    lst = html.xpath('//ul[@class="bigimg"]/li')
    for i in lst:
        n = i.xpath('./p[@class="name"]/a/@title')[0]
        p = i.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')[0]
        print(f'商品名称:{n} \n价格:{p}')


if __name__ == '__main__':
    key = input('请输入内容关键字:')
    page = input('请输入页数:')
    getData(key, page)

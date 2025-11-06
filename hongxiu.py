import os
import shutil
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service(r'D:\A-PyCharm\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(service=service, options=opt)


def reset_folder():
    if os.path.exists('novel'):
        shutil.rmtree('novel')
        os.mkdir('novel')
    else:
        os.mkdir('novel')


def get_content(u):
    browser.get(u)
    page = browser.page_source
    html = etree.HTML(page)
    filename = html.xpath('//h1[@class="j_chapterName"]/text()')[0]
    con = html.xpath('//div[@class="ywskythunderfont"]/p/text()')
    content = ''
    for i in con:
        i = i[2:]
        content += i + '\n'
    content = content.strip()
    print(f'downloading {filename}')
    with open(f'novel/{filename}.txt', 'w+', encoding='utf-8') as f:
        f.write(content)


def get_links(u):
    browser.get(u)
    page = browser.page_source
    html = etree.HTML(page)
    sub_links = html.xpath('//*[@id="jsVolumeCont"]/div[1]/ul/li/a/@href')
    return sub_links


if __name__ == '__main__':
    restriction = 10
    reset_folder()
    # url为目录页
    url = 'https://www.hongxiu.com/chapterlist/8263527304935303'
    links = get_links(url)
    for i in links:
        if restriction == 0:
            break
        get_content('https://www.hongxiu.com' + i)
        restriction -= 1
    print('over')

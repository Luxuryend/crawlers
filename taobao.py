import time
import csv
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_page_info():
    u = 'https://www.taobao.com/'
    browser.get(u)
    browser.implicitly_wait(2)
    time.sleep(1)
    browser.find_element(By.ID, 'q').send_keys(search_keyword, Keys.ENTER)

    # 显示等待
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[-1])
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content_items_wrapper"]')))
    return browser.page_source


def get_product_info(c):
    html = etree.HTML(c)
    items = html.xpath('//*[@id="content_items_wrapper"]/div')
    with open(f'taobao_csv/{search_keyword}.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for i in items:
            try:
                title = i.xpath('.//div[contains(@class, "title")]/@title')[0]
                price = i.xpath('.//div[contains(@class, "price")]/text()')[0]
                sale = i.xpath('.//span[contains(@class, "realSales")]/text()')[0]
                city = i.xpath('.//div[contains(@class, "procity")]/span/text()')[0]
                link = i.xpath('.//a/@href')[0]
                info = [title, price, sale, city, link]
                writer.writerow(info)
            except:
                print('缺失一行')
                writer.writerow([])


if __name__ == '__main__':
    service = Service(r'E:\chromedriver-win64\chromedriver.exe')
    opt = Options()
    opt.debugger_address = '127.0.0.1:8888'
    opt.add_argument('--disable-blink-features=AutomationControlled')
    # opt.add_argument("--headless=new")
    browser = webdriver.Chrome(service=service, options=opt)

    search_keyword = '苹果手机'     # 可修改变量

    content = get_page_info()
    get_product_info(content)
    browser.close()

    print('over')

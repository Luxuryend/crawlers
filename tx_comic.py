import os
import shutil
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(r'E:\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument("--headless=new")
browser = webdriver.Chrome(service=service, options=opt)


def download_img(u):
    browser.get(u)

    time.sleep(0.5)
    filename = browser.find_element(By.XPATH, '//*[@id="comicTitle"]/span[@class="title-comicHeading"]').text
    pic_list = browser.find_elements(By.XPATH, '//*[@id="comicContain"]/li/img')
    for num, pic in enumerate(pic_list):
        time.sleep(0.3)
        # 页面滚动
        ActionChains(browser).scroll_to_element(pic).perform()
        link = pic.get_attribute('src')
        pic_content = requests.get(link).content
        if not os.path.exists(f'comics/{filename}'):
            os.mkdir(f'comics/{filename}')
        with open(f'comics/{filename}/{num}.jpg', 'wb') as f:
            f.write(pic_content)
            print('downloading', filename, num)
    return browser.find_element(By.XPATH, '//*[@id="mainControlNext"]').get_attribute('href')


if __name__ == '__main__':
    shutil.rmtree('comics')
    os.makedirs('comics')
    url = 'https://ac.qq.com/ComicView/index/id/651757/cid/808'
    while url:
        url = download_img(url)
        print('completed a chapter')

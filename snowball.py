import pandas as pd
import random
from lxml import etree
from DrissionPage import Chromium, ChromiumOptions

co = ChromiumOptions()
co.headless()
browser = Chromium(addr_or_opts=co)
tab = browser.latest_tab

tab.get('https://xueqiu.com/hq/detail?market=CN&first_name=0&second_name=0&type=sh_sz')
browser.wait(random.uniform(3, 6))

x1 = '//*[@id="app"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/table/tbody/tr/'
x2 = '//*[@id="app"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/'

page = 15

for i in range(15):
    html = etree.HTML(tab.html)

    c1 = html.xpath(x1 + 'td[1]/span/a/text()')
    c2 = html.xpath(x1 + 'td[2]/span/a/text()')
    c3 = html.xpath(x2 + 'td[1]/span/text()')
    c4 = html.xpath(x2 + 'td[2]/span/text()')
    c5 = html.xpath(x2 + 'td[3]/span/text()')
    c6 = html.xpath(x2 + 'td[4]/span/text()')
    c7 = html.xpath(x2 + 'td[5]/span/text()')
    c8 = html.xpath(x2 + 'td[6]/span/text()')
    c9 = html.xpath(x2 + 'td[7]/span/text()')
    c10 = html.xpath(x2 + 'td[8]/span/text()')
    c11 = html.xpath(x2 + 'td[9]/span/text()')
    c12 = html.xpath(x2 + 'td[10]/span/text()')

    df = pd.DataFrame({
        "股票代码": c1,
        "股票名称": c2,
        "当日价": c3,
        "涨跌额": c4,
        "涨跌幅": c5,
        "年初至今": c6,
        "成交量": c7,
        "成交额": c8,
        "换手率": c9,
        "市盈率(TTM)": c10,
        "股息率": c11,
        "市值": c12
    })

    df.to_csv(
        'snowball.csv',
        mode='a',
        index=False,
        header=not bool(i)
    )
    tab.ele('x://*[@id="app"]/div/div[2]/div/div/ul/li[10]/button').click()
    print(f'已采集第{i + 1}页')
    browser.wait(random.uniform(3, 6))

tab.close()
browser.quit()

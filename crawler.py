from threading import Thread
import requests
from lxml import etree
import time

def getDate(num):
    url=f'https://word.iciba.com/?action=words&class=12&course={num}'
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }
    r=requests.get(url, headers=headers)

    data=r.content.decode()
    html=etree.HTML(data)
    words1=html.xpath('//*[@id="word_list_1"]/li/div[1]/span/text()')
    words2=html.xpath('//*[@id="word_list_2"]/li/div[1]/span/text()')
    meaning1=html.xpath('//*[@id="word_list_1"]/li/div[3]/span/text()')
    meaning2=html.xpath('//*[@id="word_list_2"]/li/div[3]/span/text()')
    del html

    word_list=[]
    for word in words1+words2:
        word_list.append(str(word).strip())
    translate=[]
    for m in meaning1+meaning2:
        translate.append(str(m).strip())

    with open('words.txt','a',encoding='utf-8') as f:
        for i,j in zip(word_list,translate):
            f.write(f"{i:20}{j}\n")

with open('words.txt','w',encoding='utf-8') as f:
    f.truncate(0)

def t(start,end):
    for i in range(start,end+1):
        getDate(i)
        print(f'成功爬取第{i}页')

thread1=Thread(target=t,args=(1,21))
thread2=Thread(target=t,args=(22,42))
thread3=Thread(target=t,args=(43,63))
thread4=Thread(target=t,args=(64,84))
thread5=Thread(target=t,args=(85,105))

if __name__=='__main__':
    start_time=time.time()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    end_time=time.time()

    print(f"完成,共耗时{(end_time-start_time):.2f}秒")
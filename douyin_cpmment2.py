import pandas as pd
import jieba
from wordcloud import WordCloud

df = pd.read_csv('douyin.csv')
content = ''.join([i for i in df['评论']])
strings = ' '.join(jieba.lcut(content))

wc = WordCloud(
    background_color='white',
    height=700,
    width=1000,
    font_path='msyh.ttc',
    stopwords={'我', '的', '是', '了', '这个', '有', '也', '都', '一个'}
)
wc.generate(strings)
wc.to_file('cy.png')

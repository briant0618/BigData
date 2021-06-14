"""
날짜 : 2021/06/11
이름 : 김동현
내용 : RealTimeSearch Test
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime


# Page 요청하기!
response = req.get('https://issue.zum.com/')

# Parsing 하기!

dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div.cont')

# Directory 만들기!
Directory = './RealtimeSearch_Test/{:%Y-%m-%d}'.format(datetime.now())

if not os.path.exists(Directory):
    os.makedirs(Directory)

# File 생성하기!
FileName = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
File = open(Directory + '/' + FileName, mode='w', encoding='utf-8')

# File 저장하기!
for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text
    File.write('%s, %s\n' % (rank[:-1], word))

File.close()

print('실시간 검색어 수집 완료')

"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python 실시간 검색어 수집

"""
#
import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

response = req.get('https://issue.zum.com/')

# Page Parsing

dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div.cont')

# Directory 생성
dir = './keyword/{:%Y-%m-%d}'.format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# File 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir + '/' + fname, mode='w', encoding='utf-8')

# File 저장
for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text
    file.write('%s, %s\n' % (rank[:-1], word)) # 문자열 짜르기

file.close()

print('실시간 검색어 수집 완료')


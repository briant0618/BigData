"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python HTML Page Parsing

Parsing
- 문서 해독을 의미한다.
- Markup 문서(html/xml)에서 특정 태그의 데이터를 추출하는 처리과정.
"""

import requests as req
from bs4 import BeautifulSoup as bs

# Request Page -> 에러 뜨는 이유 = AntiCrawling 때문에 불가능! -> Header 정보 들고가자.
response = req.get('https://news.naver.com/',
                   headers={'user-Agent': 'Mozilla/5.0'})
print(response.text)  # <- Crawling 결과
# Page Parsing
dom = bs(response.text, 'html.parser')  # dom = document object model
titles = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')
print(titles)  # <- Parsing 결과.

# 개별 출력하기.
for tit in titles:
    print(tit.text.strip())  # strip = 공백제거.

# 다음 뉴스 랭킹 1 ~ 10위 도전
resp = req.get('https://news.daum.net/ranking/popular')

dom = bs(resp.text, 'html.parser')
news_tits = dom.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')

for i in range(10):
    print(news_tits[i].text)

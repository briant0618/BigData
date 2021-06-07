"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python Weather data 수집

"""

import requests as req
from bs4 import BeautifulSoup as bs

response = req.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
# print(response.text)

# 데이터 출력
dom = bs(response.text, 'html.parser')
titles = dom.select('#weather_table > tbody > tr:nth-child(1)')
for tit in titles:
    print(tit.text.strip())
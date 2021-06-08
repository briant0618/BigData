"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python 가상 브러우저를 활용한  Weather data 수집

"""

from selenium import webdriver

# 가상 브러우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# Page Parsing

trs = browser.find_elements_by_css_selector('#weather_table > tbody > tr')
for tr in trs:
    local = tr.find_element_by_css_selector('td:nth-child(1) > a').text
    temp = tr.find_element_by_css_selector('td:nth-child(6').text

    print('{},{}'.format(local, temp))

browser.close()
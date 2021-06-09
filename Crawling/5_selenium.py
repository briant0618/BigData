"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python 가상 브라우저 Crawling
"""
# Chrome 가상 브라우저 실행
from selenium import webdriver

browser = webdriver.Chrome('./Chromedriver.exe')

# 네이버로 이동
browser.get('https://naver.com')

# 로그인 입력 버튼 클릭
btn_login = browser.find_element_by_css_selector('#account > a')
btn_login.click()

# ID / PW 입력하기

input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')

input_id.send_keys('abcdef')
input_pw.send_keys('123456')

# 로그인 접속 버튼 클릭
btn_submit = browser.find_element_by_css_selector('#log\.login')
btn_submit.click()

# 가상 브러우저 종료
browser.close()

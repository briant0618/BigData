"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python 영화 평점리뷰 Crawling

"""

from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
print('1')

# 페이지 이동
browser.get('https://movie.naver.com/')
print('2')

# 영화 랭킹 클릭
btn_rank = browser.find_element_by_css_selector('#scrollbar > div.scrollbar-box > div > div > ul > li:nth-child(3) > a')
btn_rank.click()
print('3')

# 평점순 클릭

btn_score = browser.find_element_by_css_selector('#old_content > div.tab_type_6 > ul > li:nth-child(3) > a')
btn_score.click()
print('4')

# 순위별 영화 클릭

titles = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
titles[0].click()
print('5')

# 영화 평점 클릭

menu_score = browser.find_element_by_css_selector('#movieEndTabMenu > li:nth-child(5) > a')
menu_score.click()
print('6')

# 현재 가상 브라우저를 영화리뷰가 있는 iframe 으로 전환하기
browser.switch_to.frame('pointAfterListIframe')

while True:

    # 영화 리뷰 출력하기
    lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')

    for li in lis:
        score = li.find_element_by_css_selector('div.star_score > em').text
        review = li.find_element_by_css_selector('div.score_reple > p > span:last-child').text

        print('{},{}'.format(score, review))

    # 다음 page 넘어가기
    btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child')
    btn_next.click()


print('영화 리뷰 수집 완료')

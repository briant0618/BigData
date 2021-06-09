"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python 영화 평점리뷰 Crawling

"""

from selenium import webdriver
import logging

# 로거생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

# 로그 포멧 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 핸들러 생성
fileHandler = logging.FileHandler('./review.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

# 가상 브라우저 실행(headless 모드로 실행)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
logger.info('가상 브라우저 실행...')

page = 1
rank = 0

while True:
    # 현재 브라우저를 전환
    browser.switch_to.default_content()

    # 페이지 이동
    if page > 40:
        break

    browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&page=%d' % page)
    logger.info('%d 페이지 이동' % page)
    browser.switch_to.alert.accept()

    if rank > 49:
        rank = 0
        page += 1

    # 순위별 영화 클릭
    titles = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
    titles[rank].click()
    rank += 1

    # 영화 제목
    movie_title = browser.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
    logger.info('%d위 %s 영화 클릭...' % (rank, movie_title))

    # 영화 평점 클릭
    menu_score = browser.find_element_by_css_selector('#movieEndTabMenu > li > a.tab05')
    menu_score.click()

    # 현재 가상 브라우저를 영화리뷰가 있는 iframe으로 전환
    browser.switch_to.frame('pointAfterListIframe')

    while True:
        # 영화 리뷰 출력
        lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')

        for li in lis:
            score = li.find_element_by_css_selector('div.star_score > em').text
            reple = li.find_element_by_css_selector('div.score_reple > p > span:last-child').text

            print('{},{}'.format(score, reple))

        # 다음 페이지 클릭
        try:
            btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child > em')
            btn_next.click()
            logger.info('다음 페이지 클릭...')
        except:
            break

    logger.info('%s 영화 리뷰 수집완료...' % movie_title)
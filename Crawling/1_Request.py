"""
날짜 : 2021/06/07
이름 : 김동현
내용 : Python Web Request
"""

import requests as req

# 네이버 페이지 요청
response = req.get('https://naver.com')
print(response.text)  # 네이버 페이지 텍스트 코드뜸

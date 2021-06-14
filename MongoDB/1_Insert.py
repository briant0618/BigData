"""
날짜 : 2021/06/14
이름 : 김동현
내용 : Python MongoDB Insert
"""
from datetime import datetime

from pymongo import MongoClient as mongo

# 1단계 [접속]
conn = mongo('mongodb://admin:1234@192.168.153.102:27017')

# 2단계 [DB 선택]
db = conn.get_database('test')

# 3단계 [Collection 선택]
collection = db.get_collection('Member')

# 4단계 [Query 실행]
collection.insert_one({'uid': 'a101', 'name': '김유신', 'hp': '010-1212-1010'})
collection.insert_one(
    {'uid': 'a101', 'name': '김유신', 'hp': '010-1212-1010', 'pos': '대리', 'dep': 101, 'rdate': datetime.now})

# 5단계 [ mongoDB 종료]
conn.close()

print('insert 완료')

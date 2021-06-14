"""
날짜 : 2021/06/14
이름 : 김동현
내용 : Python MongoDB Find(select)
"""

from pymongo import MongoClient as mongo

# 1단계 [접속]
conn = mongo('mongodb://admin:1234@192.168.153.102:27017')

# 2단계 [DB 선택]
db = conn.get_database('test')

# 3단계 [Collection 선택]
collection = db.get_collection('Member')

# 4단계 [ Query 실행 ]
rs = collection.find()

for row in rs:
    print('-------------')
    print('%s, %s' % (row['uid'], row['name']))

# 5단계 [DB 종료]
conn.close()

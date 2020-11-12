import pymongo

if __name__ == '__main__':
    # client = pymongo.MongoClient(host='39.96.204.153', port=27017)
    client = pymongo.MongoClient('mongodb://admin:123456@39.96.204.153:27017')
    db = client.spider
    print(db)
    collection = db.students
    print(collection)
    student = {
        'id': 1,
        'name': '张三',
        'age': 20,
        'gender': 1
    }
    student1 = {
        'id': 2,
        'name': '张三1',
        'age': 21,
        'gender': 0
    }
    # DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
    # result = collection.insert_one(student)

    result = collection.insert_many([student, student1])
    print(result.inserted_ids)
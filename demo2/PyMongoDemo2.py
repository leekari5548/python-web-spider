import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://admin:123456@39.96.204.153:27017')
    db = client.spider
    collection = db.students

    # 查找年龄等于20岁
    # result = collection.find({'age': 20})

    # 查找年龄大于20岁
    # $lt 小于
    # $gt 大于
    # $lte 小于等于
    # $gte 大于等于
    # $ne 不等于
    # $in 包含
    # $nin 不包含
    # result = collection.find({'age': {'$gt': 20}})

    # 正则表达式匹配
    # result = collection.find({'name': {'$regex': '[1]+'}})

    # print(result)
    # for res in result:
    #     print(res)

    # DeprecationWarning: count is deprecated. Use Collection.count_documents instead.
    # result = collection.find({'name': {'$regex': '[1]+'}}).count()
    #
    # print(result)

    # 在数据量非常庞大的时候，比如在查询千万、亿级别的数据库时，最好不要使用大的偏移量，因为这样很可能导致内存溢出
    # result = collection.find().sort('age', pymongo.ASCENDING).skip(2).limit(2)
    #
    # print(result)
    # for res in result:
    #     print(res)

    # 修改
    # result = collection.find_one({'name': '张三1'})
    # print(result)
    # result['age'] = 100

    # DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
    # update_result = collection.update({'name': '张三1'}, result)
    # print(update_result)

    # DeprecationWarning: remove is deprecated. Use delete_one or delete_many instead.
    result = collection.remove({'name': '张三1'})
    print(result)
import requests
import pymongo
from pyquery import PyQuery as pq
import multiprocessing as mp

def getMongoConnection():
    client = pymongo.MongoClient('mongodb://admin:123456@localhost')
    db = client.spider
    collection = db.test
    return collection
def detailInfo(baseUrl, detailUrl):

    url = baseUrl + detailUrl
    resource = requests.get(url)
    document = pq(resource.text)
    score = document('.score.m-t-md').text()
    drama = document('.drama p').text()
    director = document('#detail div:nth-child(2) div div div div div p').text()
    actorsElement = document('.actors.el-row').children()
    actors = ''
    for a in actorsElement.items():
        actors += '[' + a('.actor div div p').text() + ']' + ' '
    detail = {
        'score': score,
        'detail': drama,
        'director': director,
        'actors': actors
    }
    return detail

def processHandler(baseurl, targetUrl):
    url = baseurl + targetUrl
    print(f'start handler {url} resource.....')
    resource = requests.get(url)
    collection = getMongoConnection()
    document = pq(resource.text)
    saveList = []
    lis = document('#index .el-row .el-col').children().children('.el-card__body')
    for item in lis.items():
        detailUrl = str(item('.el-row .el-col a').attr('href'))
        imageUrl = item('.el-row .el-col a img').attr('src')
        detail = detailInfo(baseUrl, detailUrl)
        name = item('.el-row .p-h a h2').text()
        categories = item('.categories').children()
        categoriesName = ''
        for category in categories.items():
            categoriesName += category('button span').text() + ' '
        placeInfo = item('.p-h.el-col')
        placeInfo1 = placeInfo('div:nth-child(3)')
        fromPlace = placeInfo1('span:first-child').text()
        timeLong = placeInfo1('span:last-child').text()
        createTime = placeInfo('div:nth-child(4) span').text()
        itemInfo = {
            'name': name,
            'categoriesName': categoriesName,
            'imageUrl': imageUrl,
            'from': fromPlace,
            'timeLong': timeLong,
            'date': createTime
        }
        itemInfo.update(detail)
        saveList.append(itemInfo)
    collection.insert_many(saveList)


if __name__ == '__main__':

    baseUrl = "https://static1.scrape.cuiqingcai.com"
    r = requests.get(baseUrl)
    html = r.text
    doc = pq(html)
    page_a_list = doc('.el-pager').children()
    for i in page_a_list.items():
        targetUrl = str(i('li a').attr.href)
        p = mp.Process(target=processHandler, args=(baseUrl, targetUrl,))
        p.start()

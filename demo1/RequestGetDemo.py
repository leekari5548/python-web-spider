import requests
import re

if __name__ == '__main__':
    data = {
        'name': 'leekari',
        'age': 12
    }
    r = requests.get('http://localhost:8080/get/')
    # 正则表达式匹配html页面中的标题
    # pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
    # titles = re.findall(pattern, r.text)
    # print(titles)

    print(r.text)
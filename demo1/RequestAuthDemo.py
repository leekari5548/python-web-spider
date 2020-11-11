import requests

if __name__ == '__main__':
    # r = requests.get("https://static3.scrape.cuiqingcai.com/", auth=HTTPBasicAuth("admin", "admin"))

    # requests 提供了一个更简单的写法，可以直接传一个元组，它会默认使用 HTTPBasicAuth 这个类来认证
    r = requests.get("https://static3.scrape.cuiqingcai.com/", auth=("admin", "admin"))
    print(r.status_code)
    
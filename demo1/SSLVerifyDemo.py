#! ssl验证
import requests
from requests.packages import urllib3
import logging

if __name__ == '__main__':
    # 忽略证书,取消警号
    # urllib3.disable_warnings()

    logging.captureWarnings(True)

    # 忽略证书 verify=False
    r = requests.get('https://static2.scrape.cuiqingcai.com/', verify=False)

    # 指定本地证书,key需要是解密状态的
    r = requests.get("url", cert=('server.crt', 'server.key'))
    print(r.text)

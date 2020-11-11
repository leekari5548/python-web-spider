import requests

if __name__ == '__main__':
    # 普通代理
    proxies = {
        'http': 'http://1.1.1.1',
        'https': 'https://1.1.1.1'
    }
    # 包含身份认证的代理
    # proxies = {
    #     'http': 'http://username:password@1.1.1.1',
    #     'https': 'https://username:password@1.1.1.1'
    # }
    
    # socks 代理
    # pip3 install "requests[socks]"
    # proxies = {
    #     'http': 'socks5://user:password@1.1.1.1'
    # }
    r = requests.get("https://www.baidu.com", proxies=proxies)
    print(r.status_code)
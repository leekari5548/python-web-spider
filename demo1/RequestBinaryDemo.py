import requests
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
if __name__ == '__main__':
    headers = {
        'User-Agent': USER_AGENT
    }
    r = requests.get("https://github.com/favicon.ico", headers=headers)
    print(r.text)
    print(r.content)

    with open('favicon.ico', 'wb') as f:
        f.write(r.content)
import requests

COOKIES = "_octo=GH1.1.1832984338.1604902650; _ga=GA1.2.1015758335.1604902662; tz=Asia%2FShanghai; _device_id=9da859b8311d2495895b45bff0faa2a4; has_recent_activity=1; user_session=tIDM73TNi8WrC4Iucevz4y2o4cQ9tMp43AX72kETmVmrZ2Wy; __Host-user_session_same_site=tIDM73TNi8WrC4Iucevz4y2o4cQ9tMp43AX72kETmVmrZ2Wy; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=leekari5548; _gh_sess=pteHlMN21kBC8%2BaQUBOBHDLgwN7d%2BVcK23g8CJbSaqmd4SIrJYILH1dNlK9K9a4YV4IIuUODAVywyP0lf8sNDhjuceRw84sEju%2BwaEzzmeWz%2B5GKUrASHxyolG0j3slti6TiDtlZJPjQsN8IpZQ9CxPEFa8TojJ3rX9AXnXfBjpTgrUZK2yjQfVBySj7dkse9b4pmlBG1vhUOZKC%2BEZeHfSrxY1%2Bo3J1OSE8VtZ6bm18jIMkaAxAkdPGkSZGzuWiwpcobdQQsLNHv7HB84yuFkYC%2Fhb02cm07x1kjGZQrPT9dab8aGYSFsCTkYEkcJqcQhKZoWJVVJZsEBNLkcDkt6wVKBzu5QWxQlOF5nlo9fIoU7HFkEpmYNWElTHqlsAfEOZOA0HubGSDTKhrfWU%2BG68y9PpX0P9NU2GRlfDnQjpLXJTbtDwr4ml%2Fzg5tB05jSolI%2BzciNhcC7K1nPFb2kMAVxoJnSjiQ4PvDJrzSvXXqQIPFP%2FVcE3AH3BIWqywOsEWd%2FBRF19EOYfFQBvdxUU4mn88b8CoKGu0H3hw0Pn73tma0kc5qA%2FZCI1IBE%2F3ZkIIBkCZHPvDGQ6vT%2FHz6yp1aZVBzC5fbJV2KDjLJP2HfzF201hZAmJmfSvV1dT2l%2BZMjqGzHJLz1owByBy%2FFGEnZOG3R4jm4SNVwrtUQaOmi5HrrFg6bH4d019SpDQ5xGllsMxKiL%2BbV3VZhyze9PTSTImeQNd0i4wXc1QwfsK9s7%2BGQlLhGlj0J6f4j9iP8kx7YNI5RIVr6qTjAqJMOtowx9Juyu%2FhyTpM2V0qguGzElvaxAfN0rYfHVMbY26Qp4gGAwHtCZT2sV%2BKUfEi6bfLBAAvfaeHRREkrhOBeW3%2FSmjPxiTh2PPmKqF2ivC6yVYacA0G0pVFYHFkQztlPbOX%2F9kt8hMoo--vJS0ceodf%2BwzAzp2--r0IiAJ5TmGhMMYQ42Kxy3w%3D%3D"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

if __name__ == '__main__':
    # 利用登陆获取到的Cookie和User-Agent，模拟浏览器登陆github
    headers = {
        # 'Cookie': COOKIES,
        'User-Agent': USER_AGENT
    }
    # 构造一个 RequestsCookieJar 对象
    jar = requests.cookies.RequestsCookieJar()

    # 然后把刚才复制的 Cookie 处理下并赋值
    for cookie in COOKIES.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get("https://github.com", headers=headers, cookies=jar)
    print(r.text)
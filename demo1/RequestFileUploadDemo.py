import requests

if __name__ == '__main__':
    file = {
        'file': open('favicon.ico', 'rb')
    }
    r = requests.post("http://httpbin.org/post", files=file)
    print(r.text)
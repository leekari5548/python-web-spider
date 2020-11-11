import requests
import time

if __name__ == '__main__':
    data = {
        'id': 100000,
        'user_name': '10000',
        'create_time': time.time()
    }
    r = requests.post("http://localhost:8080/test", data=data, timeout=(5, 20))
    print(r.text)
    # print(f'status_code:{r.status_code};type => {type(r.status_code)}')
    # print(f'headers:{r.headers};type => {type(r.headers)}')
    # print(f'cookies:{r.cookies};type => {type(r.cookies)}')
    # print(f'url:{r.url};type => {type(r.url)}')
    # print(f'history:{r.history};type => {type(r.history)}')
from pyquery import PyQuery as pq

if __name__ == '__main__':
    doc = pq("https://cuiqingcai.com")
    print(doc('title'))
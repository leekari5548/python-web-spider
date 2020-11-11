from pyquery import PyQuery as pq

if __name__ == '__main__':
    html = '''
    <div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
    '''
    doc = pq(html)
    # 基于css选择器获取数据
    print(doc('#container .list li'))
    print(type(doc('#container .list li')))
    item = doc('#container .list li')
    for i in item.items():
        print(i.text())
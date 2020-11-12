from pyquery import PyQuery as pq

if __name__ == '__main__':
    html = '''
        <div id="grandfather">
        <div id="father">
        <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
     </div>
     </div>
        '''
    doc = pq(html)
    l = doc('#container .list .item-0 a span')
    print(l)

    # 获取标签上的属性
    print(l.attr('class'))

    l1 = doc('.item-0.active').children()
    print(l1)
    print(l1.attr.href)

    # 多个元素时，attr只获取第一个元素上的属性
    lis = doc('ul li')
    print(lis)
    print(lis.attr('class'))
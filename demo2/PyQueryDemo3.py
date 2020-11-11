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
    items = doc('.list')
    print(f'items => {items}, itemsType => {type(items)}')
    # find
    # 的查找范围是节点的所有子孙节点，而如果我们只想查找子节点，那可以用
    # children
    # 方法：
    lis = items.find('li')
    print(f'list => {lis}, listType => {type(lis)}')

    print('---------------------------')

    # 返回子节点，通过css选择器选择需要的项
    lis_child = items.children('.item-0')
    print(f'list_child => {lis_child}, type => {type(lis_child)}')

    print('---------------------------')

    # 返回父节点
    parent = items.parent()
    print(f'parent => {parent}, type => {type(parent)}')

    print('---------------------------')

    # 返回全部父节点，或者添加参数进行css选择
    parents = items.parents('#father')
    print(f'parents => {parents}, type => {type(parents)}')

    print('---------------------------')

    # 获取兄弟节点，也可以通过css选择器选择
    li = doc('.list .item-0.active')
    print(li.siblings())
    # 转换为字符串
    print(str(li.text()))
    # 遍历获取items
    for item in li.siblings().items():
        print(item)

    # 获取方法属性

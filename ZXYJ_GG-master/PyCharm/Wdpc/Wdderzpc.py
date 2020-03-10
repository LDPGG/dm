import urllib
import urllib.request
import re


def get_ima(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)  # 获取网页
    response = urllib.request.urlopen(request)  # 获取服务器响应
    get_img = response.read()  # 读取图片
    return get_img


def get_imas(html):
    # 正则是硬伤
    rege = 'http://[\S]*\.jpg'
    # 如果用标签的话就要这么拿，但是我换了好几次，其他网站的网站随便拿，就是取不到百度的地址，只能用正则了
    # imgs = soup.select('标签名')
    # imgs.get('src')
#   print(rege)  测试
    pattern = re.compile(rege)  # 将地址编译成字节
    get_img = re.findall(pattern, repr(html))  # 用findall查询出所有与字节匹配的地址  用repr用来转换表达式类型字符串
    num = 1
    for aa in get_img:
        image = get_ima(aa)  # 将每个aa链接重新解析
        # wb 是用二进制将图片写入本地（具体我也不太清楚https://www.imooc.com/qadetail/190225自己去看，多百度）  as 是取个变量名
        with open('%s.jpg' % num, 'wb') as fp:
            fp.write(image)  # 把你爬到的图片存到本地
            num += 1
            print('正在下载第%s张图片' % num)
    return


if __name__ == '__main__':
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=python&ct=201326592&lm=-1&v=flip'
    html = get_ima(url)
    get_imas(html)

#  Python小白的挣扎
#  大神轻锤
#  小白的第一个爬虫
# 这里导入要先导入BeautifulSoup和requests
from bs4 import BeautifulSoup
import requests

# 这里是你要爬取的网页路径，我这里爬的是糗事百科
url = 'https://www.qiushibaike.com/pic/'
# 用requests.get方法获得网页，并把它存储
we_data = requests.get(url)
# 用BeautifulSoup 解析网页，用.text方法使得网页可读
soup = BeautifulSoup(we_data.text, 'html.parser')
# 爬取的元素标签，（看其标签中共有属性）
titles = soup.select('div.content span')
# 爬取想要图片的链接（在图片路径没有设置宽度的情况下）
# 不要听信百度用煞笔正则，我研究了一上午正则，一直报错说正则不是str类型，我又研究怎么加转型
imgs = soup.select('div.thumb a img')
# 对比上面的，爬取想要的图片的链接（在图片路径有设置宽度的情况下）
# imgs = soup.select('img[width="200"]')
# 用循环输出结果
for title, imgs in zip(titles, imgs):
    # 设置字典存放你爬取到的内容
    data = {
            # 用户输入的内容
            '内容': title.get_text('span'),
            # 用户上传的图片路径
            '图片路径': imgs.get('src')
    }
    # 输出你爬到的东西
    print(data)


import uuid
import requests
from lxml import etree


def gethtml(url):
    """获取html文件"""
    html = requests.get(url)
    html = html.content
    return html


def parse_src(html):
    """解析html文件"""
    html = etree.HTML(html)
    url_list = html.xpath("/html/body/p/img/@src")
    return url_list


def down_img(img_url):
    """下载指定url所指向的图像"""
    r = requests.get(img_url)
    with open(f'{uuid.uuid4()}.jpg', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    url = "www.baidu.com"
    html = gethtml(url)
    img_url = parse_src(html)
    down_img(img_url)
import os
import re
import time
from PIL import Image
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # 下载对应chrome驱动

"""
# 环境安装
pip install tqdm
pip install pillow
pip install selenium
pip install webdriver_manager
"""


class SeleniumExample:
    def __init__(self, down_img_path="down"):
        if not os.path.exists(down_img_path):
            os.mkdir(down_img_path)
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 配置无头访问
        chrome_options.add_argument('window-size=1920x1080')  # 配置访问的分辨率
        chrome_options.add_argument('--disable-gpu')  # Google推荐 防bug
        self.brower = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.down_img_path = down_img_path

    def brower_screeshot(self, url, page="1"):
        self.brower.get(url)
        self.brower.maximize_window()
        # time.sleep(3)  # 如果网页未加载完全并截图, 暂停程序
        # self.brower.save_screenshot(f"{self.save_path}/{str(page)}.png")
        self.brower.get_screenshot_as_file(f"{self.down_img_path}/{str(page)}.png")

    def off_selenium(self):
        self.brower.quit()


class PngToPdf:
    def __init__(self):
        self.corp_point = (290, 70, 1630, 1030)  # x1, y1, x2, y2

    @staticmethod
    def sort_key(s):
        # 获取图片名称
        tail = s.split('\\')[-1]
        # 匹配开头数字序号
        c = re.findall('\d+', tail)[0]
        return int(c)

    @staticmethod
    def strsort(alist):
        alist.sort(key=PngToPdf.sort_key)
        return alist

    def imgs2pdf(self, input_img_dir, out_pdf_path, corp=False):
        files = os.listdir(input_img_dir)
        pngFiles = []
        sources = []
        for file in files:
            if 'png' in file:
                pngFiles.append(os.path.join(input_img_dir, file))
        pngFiles = PngToPdf.strsort(pngFiles)
        output = Image.open(pngFiles[0]).convert("RGB")
        if corp:
            output = output.crop(self.corp_point)
        pngFiles.pop(0)
        for file in tqdm(pngFiles):
            img = Image.open(file).convert("RGB")
            if corp:
                img = img.crop(self.corp_point)
            sources.append(img)
        output.save(out_pdf_path, "pdf", save_all=True, append_images=sources)
        print("save imgs to pdf success...")


if __name__ == '__main__':
    # 下载截图
    down_img_path = "down"
    se = SeleniumExample(down_img_path)
    se.brower_screeshot("https://www.baidu.com", )
    se.off_selenium()
    # 拼接截图到pdf
    ptp = PngToPdf()
    ptp.imgs2pdf(down_img_path, out_pdf_path="test.pdf", corp=True)
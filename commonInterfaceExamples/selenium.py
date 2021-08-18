from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

"""python
# 环境安装
pip install selenium
需下载当前安装的Chrome浏览器对应的webdriver文件放到当下目录供以使用
"""

chrome_options = Options()
chrome_options.add_argument("--headless")  # 配置无头访问
chrome_options.add_argument('window-size=1920x1080')  # 配置访问的分辨率
chrome_options.add_argument('--disable-gpu')  # Google推荐 防bug
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)  # 创建一个浏览器对象

driver.get("http://www.baidu.com/")  # 获取一个页面
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))  # 找到搜索窗口 输入关键词 提交表单
element.send_keys("机器之心")
element.submit()
element = driver.find_element_by_tag_name('a').click()  # 点击tag为a的按钮
# driver.quit()
# exit()

print(driver.title)
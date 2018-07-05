#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午3:37
# @Author  : Aries (i@iw3c.com)
# @Site    : http://iw3c.com
# @File    : chrome.py
# @Software: PyCharm


'''
pip3 install beautifulsoup4
pip3 install -U selenium
下载 chromedriver  http://npm.taobao.org/mirrors/chromedriver/ or http://chromedriver.storage.googleapis.com/index.html 查看下载目录中的notes.txt中driver对应的chrome的版本
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless') # 无头浏览器
chrome_options.add_argument('--disable-gpu')
#设置匿名代理
PROXY = "61.168.162.32:80"
chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
#需要验证的代理请参考：https://vimmaniac.com/blog/bangal/selenium-chrome-driver-proxy-with-authentication
driver = webdriver.Chrome(executable_path='/Volumes/HDD/workshop/phantomjs/bin/chromedriver', chrome_options=chrome_options)
#driver = webdriver.Chrome(chrome_options=chrome_options)  #如果把chromedriver加入了环境变量，就可以不加executable_path
driver.get('https://qinhuangdao.anjuke.com/prop/view/A1305238435?from=filter&spread=commsearch_t&position=1&kwtype=filter&now_time=1530673385')
page_source = driver.page_source
#载入soup
soup = BeautifulSoup(page_source, 'lxml')
reference_monthpay = soup.find('span', id='reference_monthpay')
print(reference_monthpay.text)
# 查看页面快照
#driver.save_screenshot('baidu.com.png')
# 向下滚动10000像素
#driver.execute_script("document.body.scrollTop=10000")
time.sleep(3)
driver.quit()
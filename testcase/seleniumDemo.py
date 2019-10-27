# coding=utf-8
from selenium import webdriver
browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get('http://www.baidu.com/')
browser.close()
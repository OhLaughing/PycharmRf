# coding=utf-8
from selenium import webdriver
browser = webdriver.Chrome()
browser.set_window_size(480, 800)
first_url = 'http://www.baidu.com'
print('now access: ' + first_url)
browser.get(first_url)
browser.implicitly_wait(2)
second_url = 'http://news.baidu.com'
print('now access: ' + second_url)
browser.get(second_url)
browser.implicitly_wait(2)
print('back to ' + first_url)
browser.back();
browser.implicitly_wait(2)
print('forward to ' + second_url)
browser.forward();

browser.quit()



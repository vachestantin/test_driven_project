from selenium import webdriver

browser = sebdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

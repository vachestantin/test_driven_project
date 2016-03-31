
from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# assert 에러가 발생한다면 콘솔에 브라우저 타이틀을 출력할 것이다.
assert 'Django' in browser.title, "Browser title was: " + browser.title

browser.quit()

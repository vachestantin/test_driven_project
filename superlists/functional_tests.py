
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self): #각각의 테스트를 수행하지 전에 브라우저를 실행한다
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) #그냥 3초간 기다리는 것

    def tearDown(self): #테스트를 통과하지 못해도 브라우저는 닫는다
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #테스트 내용을 알 수 있는 명칭으로 정하는 것이 좋다
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!') #강제적으로 테스트 실패를 밣생시켜 에러 메시지를 출력한다

        if __name__ == '__main__':
            unittest.main(warnings='ignore')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self): #각각의 테스트를 수행하지 전에 브라우저를 실행한다
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) #그냥 3초간 기다리는 것

    def tearDown(self): #테스트를 통과하지 못해도 브라우저는 닫는다
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #테스트 내용을 알 수 있는 명칭으로 정하는 것이 좋다
        # 에디스는 멋진 온라인 앱이 나왔다는 소식을 듣고 해당 웹 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        #웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_elements_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        inputbox.send_keys('공작깃털 사기')

        inputbox.send_keys('Keys.ENTER')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
        )

        #강제적으로 테스트 실패를 밣생시켜 에러 메시지를 출력한다
        self.fail('Finish the test!')

        if __name__ == '__main__':
            unittest.main(warnings='ignore')

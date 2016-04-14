
import sys, time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls): #각각의 테스트를 수행하지 전에 브라우저를 실행한다
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self): #각각의 테스트를 수행하지 전에 브라우저를 실행한다
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) #그냥 3초간 기다리는 것

    def tearDown(self): #테스트를 통과하지 못해도 브라우저는 닫는다
        self.browser.refresh()
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

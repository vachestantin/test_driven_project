
from .base import FunctionalTest

# from selenium.webdriver.common.keys import Keys

from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 입력 상자가 비어 있는 상테에서 엔터키를 누른다
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # 에러 메시지가 표시된다
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 다른 아이템을 입력하고 이번에는 정상 처리된다
        self.get_item_input_box().send_keys('우유 사기\n')
        self.check_for_row_in_list_table('1: 우유 사기')

        # 그녀는 고의적으로 다시 빈 아이템을 등록한다
        self.get_item_input_box().send_keys('\n')

        # 리스트 페이지에 다시 에러 메시지가 표시된다
        self.check_for_row_in_list_table('1: 우유 사기')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 아이템을 입력하면 정상동작한다
        self.get_item_input_box().send_keys('차 만들기\n')
        self.check_for_row_in_list_table('1: 우유 사기')
        self.check_for_row_in_list_table('2: 차 만들기')


        self.browser.refresh()

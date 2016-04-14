
import time

from .base import FunctionalTest

from selenium.webdriver.support.ui import WebDriverWait


class LoginTest(FunctionalTest):

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('창을 찾을 수 없습니다')

    def test_login_with_persona(self):
        # 에디스는 superlists 사이트에 접속한다
        # 그리고 회원가입 링크를 발견한다
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('login').click()

        # 개인 로그인 박스가 표시된다
        self.switch_to_new_window('Mozilla Persona')

        # 에디스는 이메일 주소를 이용해서 로그인한다
        ## 테스트 이메일로 mockmyid.com 사용 #
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # 개인 창을 닫는다
        self.switch_to_new_window('To-Do')

        # 로그인된 것을 알 수 있다
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)


from .base import FunctionalTest

from unittest import skip


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # 입력 상자가 비어 있는 상테에서 엔터키를 누른다

        # 에러 메시지가 표시된다

        # 다른 아이템을 입력하고 이번에는 정상 처리된다

        # 그녀는 고의적으로 다시 빈 아이템을 등록한다

        # 리스트 페이지에 다시 에러 메시지가 표시된다

        # 아이템을 입력하면 정상동작한다
        self.fail('wirte me!')

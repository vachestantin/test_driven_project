
import requests
import sys

from accounts.models import ListUser

class PersonaAuthenticationBackend(object):

    def authenticate(self):
        # 어선셜을 모질라의 증명 서비스로 전송
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to mozilla', data, file=sys.stderr)
        resp = requests.post('https://verifier.login.persona.org/verify', data=data)
        print('got', resp.content, file=sys.stderr)

        # 증명자가 응답했는가?
        if resp.ok:
            # 응답 반환
            verification_data = resp.json()

            # 어설션이 유효한지 확인
            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self):
        return ListUser.objects.get(email=email)

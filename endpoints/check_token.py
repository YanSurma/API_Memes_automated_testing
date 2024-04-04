import allure
import requests

from endpoints.endpoint import Endpoint


class CheckToken(Endpoint):
    text = None

    @allure.step('Check that token is valid')
    def check_token_is_valid(self, token):
        self.response = requests.get(
            f'{self.url}/authorize/{token}'
        )
        self.text = self.response.text
        print(self.text)
        return self.text

    @allure.step('Check response text is "token is alive"')
    def check_success_response_text(self):
        assert 'Token is alive' in self.response.text

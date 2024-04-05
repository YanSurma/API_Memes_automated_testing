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

    @allure.step('Check that token is valid')
    def check_token_with_invalid_token(self):
        invalid_input = '123@#$%^&*'
        self.response = requests.get(
            f'{self.url}/authorize/{invalid_input}'
        )
        self.text = self.response.text
        print(self.text)
        return self.text

    def check_html_error_404(self):
        assert '<title>404 Not Found</title>' in self.text
        assert '<h1>Not Found</h1>' in self.text
        assert '<p>Token not found</p>' in self.text

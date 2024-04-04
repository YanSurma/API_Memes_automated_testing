import allure
import requests

from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    json = None
    token = None
    html_response = None

    @allure.step('Authorize user')
    def authorize_user(self, body):
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=body)
        self.json = self.response.json()
        self.token = self.json["token"]
        print(self.json)
        return self.token

    @allure.step('Check that user name value same as sent')
    def check_response_user_name(self):
        assert self.json["user"] == "Yan"

    @allure.step('Authorize user with empty json')
    def authorize_user_with_empty_json(self):
        body = {}
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=body)
        self.html_response = self.response.text
        print(self.html_response)
        return self.html_response

    @allure.step('Authorize user with integer name')
    def authorize_user_with_integer_name(self):
        body = {
            "name": 1
        }
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=body)
        self.html_response = self.response.text
        print(self.html_response)
        return self.html_response

    @allure.step('Check html error 400 Bad Request')
    def check_html_error_400(self):
        assert '<title>400 Bad Request</title>' in self.html_response
        assert '<h1>Bad Request</h1>' in self.html_response
        assert '<p>Invalid parameters</p>' in self.html_response


test = Authorization()
test.authorize_user_with_integer_name()

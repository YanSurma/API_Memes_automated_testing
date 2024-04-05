import allure
import requests
from endpoints.endpoint import Endpoint


class CreateMem(Endpoint):
    json = None
    mem_id = None
    html_response = None

    @allure.step('Create mem')
    def create_new_mem(self, body, token):
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={"Authorization": token})
        self.json = self.response.json()
        self.mem_id = self.json["id"]
        return self.json

    @allure.step('Check response text same as sent')
    def check_response_text_same_as_sent(self, text):
        assert self.json["text"] == text

    @allure.step('Check response url same as sent')
    def check_response_url_same_as_sent(self, url):
        assert self.json["url"] == url

    @allure.step('Check response tags same as sent')
    def check_response_tags_same_as_sent(self, tags):
        assert self.json["tags"] == tags

    @allure.step('Check response info same as sent')
    def check_response_info_same_as_sent(self, info):
        assert self.json["info"] == info

    @allure.step('Create mem')
    def create_new_mem_with_invalid_data(self, body, token):
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={"Authorization": token})
        self.html_response = self.response.text
        print(self.html_response)
        return self.html_response

    @allure.step('Check html error 400 Bad Request')
    def check_html_error_400(self):
        assert '<title>400 Bad Request</title>' in self.html_response
        assert '<h1>Bad Request</h1>' in self.html_response
        assert '<p>Invalid parameters</p>' in self.html_response

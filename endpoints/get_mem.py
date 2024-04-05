import token

import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneMem(Endpoint):
    json = None
    html_response = None

    @allure.step('Get one meme by id')
    def get_mem_by_id(self, token, mem_id):
        self.response = requests.get(
            f'{self.url}/meme/{mem_id}',
            headers={"Authorization": token}
        )
        self.json = self.response.json()
        print(self.json)
        return self.json

    @allure.step('Check that mem id same as sent')
    def check_that_mem_id_same_as_sent(self, mem_id):
        assert self.json["id"] == mem_id, 'Invalid mem id'

    @allure.step('Check that deleted mem not found in DB')
    def get_deleted_mem(self, token, mem_id):
        self.response = requests.get(
            f'{self.url}/meme/{mem_id}',
            headers={"Authorization": token}
        )
        self.html_response = self.response.text
        return self.html_response

    @allure.step('Check html error 404 Not Found')
    def check_html_error_404(self):
        assert '<title>404 Not Found</title>' in self.html_response
        assert '<h1>Not Found</h1>' in self.html_response

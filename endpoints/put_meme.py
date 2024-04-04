import allure
import requests
from endpoints.endpoint import Endpoint


class PutMem(Endpoint):
    json = None

    @allure.step('Put meme data')
    def put_new_mem(self, token, mem_id):
        body = {
            "id": mem_id,
            "text": "Puted",
            "url": "Puted",
            "tags": [
                "Puted",
                "Puted"
            ],
            "info": {
                "coloros": [
                    "Puted",
                    "Puted"
                ]
            }
        }
        headers = {"Authorization": token}
        self.response = requests.put(url=f"{self.url}/meme/{mem_id}",
                                     json=body,
                                     headers=headers)
        self.json = self.response.json()
        return self.json

    @allure.step('Check response text changed')
    def check_response_text_changed(self):
        assert self.json["text"] == "Puted"

    @allure.step('Check response url changed')
    def check_response_url_changed(self):
        assert self.json["url"] == "Puted"

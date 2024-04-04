import allure
import requests

from endpoints.endpoint import Endpoint


class GetAllMems(Endpoint):
    json = None

    @allure.step('Gel all memes list')
    def get_all_mems(self, token):
        self.response = requests.get(
            url=f'{Endpoint.url}/meme',
            headers={"Authorization": f'{token}'}
        )
        self.json = self.response.json()
        print(self.json)
        return self.json

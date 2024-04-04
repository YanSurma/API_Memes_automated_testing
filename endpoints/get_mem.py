import allure
import requests

from endpoints.endpoint import Endpoint


class GetOneMem(Endpoint):
    json = None

    @allure.step('Gel one meme by id')
    def get_mem_by_id(self, token, mem_id):
        self.response = requests.get(
            f'{self.url}/meme/{mem_id}',
            headers={"Authorization": token}
        )
        self.json = self.response.json()
        print(self.json)
        return self.json

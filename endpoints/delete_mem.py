import allure
import requests

from data import CREATE_BODY
from endpoints.endpoint import Endpoint


class DeleteMem(Endpoint):
    text = None

    @allure.step('Delete mem')
    def delete_mem_by_id(self, token, mem_id):
        self.response = requests.delete(
            f'{self.url}/meme/{mem_id}',
            headers={"Authorization": token}
        )
        self.text = self.response.text
        print(f'Delete mem with id {mem_id}')
        print(self.text)
        return self.text

    @allure.step('Check response that deleted meme with same id as sent')
    def check_success_delete_text(self, mem_id):
        assert f"Meme with id {mem_id} successfully deleted" in self.response.text

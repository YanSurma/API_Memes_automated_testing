import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None

    @allure.step('Check status code 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

    @allure.step('Check status code 400')
    def check_status_code_400(self):
        assert self.response.status_code == 400, 'Status code is not 400'

    @allure.step('Check status code 404')
    def check_status_code_404(self):
        assert self.response.status_code == 404, 'Status code is not 404'

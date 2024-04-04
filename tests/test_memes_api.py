import allure
import pytest
import requests

from data import AUTH_BODY, CREATE_BODY


@allure.feature('Smoke test')
def test_authorize(authorize_endpoint):
    authorize_endpoint.authorize_user(body=AUTH_BODY)
    authorize_endpoint.check_status_code_200()
    authorize_endpoint.check_response_user_name()


def test_authorize_user_with_empty_json(authorize_endpoint):
    authorize_endpoint.authorize_user_with_empty_json()
    authorize_endpoint.check_status_code_400()


def test_authorize_user_with_integer_name(authorize_endpoint):
    authorize_endpoint.authorize_user_with_integer_name()
    authorize_endpoint.check_status_code_400()


@allure.feature('Smoke test')
def test_token_is_valid(check_token_endpoint, session_token):
    check_token_endpoint.check_token_is_valid(token=session_token)
    check_token_endpoint.check_status_code_200()
    check_token_endpoint.check_success_response_text()


@allure.feature('Smoke test')
def test_get_all_mems(all_memes_endpoint, session_token):
    all_memes_endpoint.get_all_mems(session_token)
    all_memes_endpoint.check_status_code_200()


@pytest.mark.parametrize('data', CREATE_BODY)
@allure.feature('Smoke test')
def test_create_mem(create_mem_endpoint, session_token, data):
    create_mem_endpoint.create_new_mem(body=data, token=session_token)
    create_mem_endpoint.check_status_code_200()
    create_mem_endpoint.check_response_text_same_as_sent(data["text"])
    create_mem_endpoint.check_response_url_same_as_sent(data["url"])
    create_mem_endpoint.check_response_tags_same_as_sent(data["tags"])
    create_mem_endpoint.check_response_info_same_as_sent(data["info"])


@allure.feature('Smoke test')
def test_put_mem(session_token, put_meme_endpoint, create_set_id):
    put_meme_endpoint.put_new_mem(token=session_token, mem_id=create_set_id)
    put_meme_endpoint.check_status_code_200()
    put_meme_endpoint.check_response_text_changed()
    put_meme_endpoint.check_response_url_changed()


@allure.feature('Smoke test')
def test_get_mem_by_id(one_meme_endpoint, session_token, create_set_delete_id):
    one_meme_endpoint.get_mem_by_id(session_token, mem_id=create_set_delete_id)
    one_meme_endpoint.check_status_code_200()


@allure.feature('Smoke test')
def test_delete_mem(delete_meme_endpoint, session_token, create_set_id):
    delete_meme_endpoint.delete_mem_by_id(token=session_token, mem_id=create_set_id)
    delete_meme_endpoint.check_status_code_200()
    delete_meme_endpoint.check_success_delete_text(mem_id=create_set_id)
import allure
import pytest

from json_bodies import AUTH_BODY, CREATE_BODY, NEGATIVE_CREATE_BODY


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


def test_token_with_invalid_token(check_token_endpoint):
    check_token_endpoint.check_token_with_invalid_token()
    check_token_endpoint.check_status_code_404()
    check_token_endpoint.check_html_error_404()


@allure.feature('Smoke test')
def test_get_all_mems(get_all_mems_endpoint, session_token):
    get_all_mems_endpoint.get_all_mems(session_token)
    get_all_mems_endpoint.check_status_code_200()


@pytest.mark.parametrize('data', CREATE_BODY)
@allure.feature('Smoke test')
def test_create_mem(create_mem_endpoint, session_token, data, get_mem_endpoint):
    create_mem_endpoint.create_new_mem(body=data, token=session_token)
    create_mem_endpoint.check_status_code_200()
    create_mem_endpoint.check_response_text_same_as_sent(data["text"])
    create_mem_endpoint.check_response_url_same_as_sent(data["url"])
    create_mem_endpoint.check_response_tags_same_as_sent(data["tags"])
    create_mem_endpoint.check_response_info_same_as_sent(data["info"])
    with allure.step('Check that mem successfully added to DB'):
        get_mem_endpoint.get_mem_by_id(session_token, create_mem_endpoint.mem_id)
        get_response = get_mem_endpoint.json
        create_response = create_mem_endpoint.json
        assert get_response == create_response, 'Get response not equal to create'


@pytest.mark.parametrize('negative_data', NEGATIVE_CREATE_BODY)
@allure.feature('Smoke test')
@allure.title('BUG:The integer value created for "tags" and "colorors" key, but only strings supports')
def test_create_new_mem_with_invalid_data(create_mem_endpoint, session_token, negative_data):
    create_mem_endpoint.create_new_mem_with_invalid_data(body=negative_data, token=session_token)
    create_mem_endpoint.check_status_code_400()
    create_mem_endpoint.check_html_error_400()


@allure.feature('Smoke test')
def test_get_mem_by_id(get_mem_endpoint, session_token, create_set_delete_id):
    get_mem_endpoint.get_mem_by_id(session_token, mem_id=create_set_delete_id)
    get_mem_endpoint.check_status_code_200()
    get_mem_endpoint.check_that_mem_id_same_as_sent(create_set_delete_id)


@allure.feature('Smoke test')
def test_put_mem(session_token, put_mem_endpoint, create_set_id, get_mem_endpoint):
    put_mem_endpoint.put_new_mem(token=session_token, mem_id=create_set_id)
    put_mem_endpoint.check_status_code_200()
    put_mem_endpoint.check_response_text_changed()
    put_mem_endpoint.check_response_url_changed()
    with allure.step('Check that mem successfully changed'):
        get_mem_endpoint.get_mem_by_id(token=session_token, mem_id=create_set_id)
        put_response = put_mem_endpoint.json
        get_response = get_mem_endpoint.json
        assert put_response == get_response, 'Get response not equal to put'


@allure.feature('Smoke test')
def test_delete_mem(delete_mem_endpoint, session_token, create_set_id, get_mem_endpoint):
    delete_mem_endpoint.delete_mem_by_id(token=session_token, mem_id=create_set_id)
    delete_mem_endpoint.check_status_code_200()
    delete_mem_endpoint.check_success_delete_text(mem_id=create_set_id)
    get_mem_endpoint.get_deleted_mem(session_token, create_set_id)
    get_mem_endpoint.check_status_code_404()
    get_mem_endpoint.check_html_error_404()

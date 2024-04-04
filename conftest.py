import allure
import pytest

from data import CREATE_BODY, AUTH_BODY
from endpoints.authorization import Authorization
from endpoints.check_token import CheckToken
from endpoints.create_mem import CreateMem
from endpoints.delete_mem import DeleteMem
from endpoints.get_all_memes import GetAllMems
from endpoints.get_mem import GetOneMem
from endpoints.put_meme import PutMem


@pytest.fixture(scope='session')
def authorize_endpoint():
    return Authorization()


@pytest.fixture(scope='session')
def check_token_endpoint():
    return CheckToken()


@pytest.fixture(scope='session')
def all_memes_endpoint():
    return GetAllMems()


@pytest.fixture(scope='session')
def one_meme_endpoint():
    return GetOneMem()


@pytest.fixture(scope='session')
def create_mem_endpoint():
    return CreateMem()


@pytest.fixture(scope='session')
def delete_meme_endpoint():
    return DeleteMem()


@pytest.fixture(scope='session')
def put_meme_endpoint():
    return PutMem()


@allure.step('Prepare token for test session')
@pytest.fixture(scope='session')
def session_token(authorize_endpoint, check_token_endpoint):
    authorize_endpoint.authorize_user(body=AUTH_BODY)
    session_token = authorize_endpoint.token
    check_token_endpoint.check_token_is_valid(session_token)
    return session_token


@allure.step('Create mem, set id and delete after test')
@pytest.fixture()
def create_set_delete_id(create_mem_endpoint, delete_meme_endpoint, session_token):
    print('create mem')
    create_mem_endpoint.create_new_mem(body=CREATE_BODY[0], token=session_token)
    mem_id = create_mem_endpoint.mem_id
    print('Set mem id')
    yield mem_id
    delete_meme_endpoint.delete_mem_by_id(mem_id=mem_id, token=session_token)
    print('Delete id')


@allure.step('Create mem and set id')
@pytest.fixture()
def create_set_id(create_mem_endpoint, session_token):
    print('create mem')
    create_mem_endpoint.create_new_mem(body=CREATE_BODY[1], token=session_token)
    print('Set mem id')
    mem_id = create_mem_endpoint.mem_id
    return mem_id

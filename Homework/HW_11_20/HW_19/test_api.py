import requests
import pytest

base_url = 'https://jsonplaceholder.typicode.com/posts'
body = {
  "title": "foo",
  "body": "bar",
  "userId": 1
}

@pytest.fixture
def fixture_add():
    responce_post = requests.post(f'{base_url}', json=body)
    new_id = responce_post.json()['id']
    yield new_id

@pytest.fixture
def fixture_add_del():
    responce_post = requests.post(f'{base_url}', json=body)
    new_id = responce_post.json()['id']
    yield new_id
    requests.delete(f'{base_url}/{new_id}')

@pytest.mark.smoke
def test_get_post(fixture_add_del):
    respons_get = requests.get(f'{base_url}/{fixture_add_del}')
    assert respons_get.json()['id'] == fixture_add_del

@pytest.mark.regression
def test_create_post():
    respons_post = requests.post(f'{base_url}', json=body)
    new_post_id = respons_post.json()['id']
    assert 'id' in respons_post.json()
    requests.delete(f'{base_url}/{respons_post.json()["id"]}')

@pytest.mark.regression
def test_delete_post(fixture_add):
    respons_del = requests.delete(f'{base_url}/{fixture_add}')
    assert respons_del.status_code == 200


@pytest.mark.smoke
def test_get_all_posts():
    response_get_all = requests.get(base_url)
    assert len(response_get_all.json()) == 100

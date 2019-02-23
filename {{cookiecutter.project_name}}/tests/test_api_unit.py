import json

from {{ cookiecutter.app_name }}.app import create_app

app = create_app(testing=True)


def post_json(url, data, headers):
    data = json.dumps(data)
    response = app.test_client().post(url, headers=headers, data=data)
    return response


def get_json(url, headers):
    response = app.test_client().get(url, headers=headers)
    return response


def put_json(url, data, headers):
    data = json.dumps(data)
    response = app.test_client().put(url, headers=headers, data=data)
    return response


def delete_json(url, headers):
    response = app.test_client().delete(url, headers=headers)
    return response


def test_app():
    headers = {'Content-Type': 'application/json'}
    response = get_json('/', headers)
    assert response.status_code == 404

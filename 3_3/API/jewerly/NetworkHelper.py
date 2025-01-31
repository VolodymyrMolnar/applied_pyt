import requests

class NetworkHelper:
    BASE_URL = 'http://127.0.0.1:7000/api/'
    HEADERS = {'Authorization': 'Bearer 5c1b63a7becd660106c92c95d40be427f6b3e3ca'}  #

    @staticmethod
    def get_list(resource):
        response = requests.get(f"{NetworkHelper.BASE_URL}{resource}/", headers=NetworkHelper.HEADERS)
        return response.json()

    @staticmethod
    def get_item(resource, item_id):
        response = requests.get(f"{NetworkHelper.BASE_URL}{resource}/{item_id}/", headers=NetworkHelper.HEADERS)
        return response.json()

    @staticmethod
    def create_item(resource, data):
        response = requests.post(f"{NetworkHelper.BASE_URL}{resource}/", headers=NetworkHelper.HEADERS, json=data)
        return response.json()

    @staticmethod
    def update_item(resource, item_id, data):
        response = requests.put(f"{NetworkHelper.BASE_URL}{resource}/{item_id}/", headers=NetworkHelper.HEADERS, json=data)
        return response.json()

    @staticmethod
    def delete_item(resource, item_id):
        response = requests.delete(f"{NetworkHelper.BASE_URL}{resource}/{item_id}/", headers=NetworkHelper.HEADERS)
        return response.status_code

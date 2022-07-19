import requests

import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        header = self.get_headers()
        params = {'path': full_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=header, params=params)
        response_href = response.json()
        href = response_href.get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    full_path = os.path.join('test for task 2.txt')
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(file_path='test for task 2')

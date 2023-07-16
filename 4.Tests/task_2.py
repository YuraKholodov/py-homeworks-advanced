import unittest
import requests


class TestYandexDiskAPI(unittest.TestCase):

    def setUp(self):
        self.token = ''
        self.folder_name = 'Test Folder'
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def test_create_folder_success(self):
        params = {'path': f'/{self.folder_name}'}
        response = requests.put(f'{self.url}/', headers=self.headers, params=params)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

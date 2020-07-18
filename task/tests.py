import requests

class TestTasks:
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk1MTAxOTE2LCJqdGkiOiIxZmZhNDhmYjg2Nzc0NjQwOTc0ZTY0MWI4MzkyYWE5OSIsInVzZXJfaWQiOjJ9.me_aZ4dKVuBAKZfjDuWBdfkccWHOt-987_vkpTVhs24'}
    url_base_tasks = 'http://localhost:8000/api/tasks/'

    def test_get_tasks(self):
        resposta = requests.get(url=self.url_base_tasks, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_task(self):
        resposta = requests.get(
            url=f'{self.url_base_tasks}21/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_task(self):
        task = {
            'name': 'Teste1',
            'deadline': '2020-07-17T21:37:50.907312-03:00',
            'priority': 'Alta',
            'description': 'test',
        }
        resposta = requests.post(
            url=self.url_base_tasks, headers=self.headers, json=task)
        assert resposta.status_code == 201
        assert resposta.json()['name'] == task['name']

    def test_put_task(self):
        task = {
            'name': 'Teste 2',
            'deadline': '2020-07-17T21:37:50.907312-03:00',
            'priority': 'Alta',
            'description': 'test',
        }

        resposta = requests.put(
            url=f'{self.url_base_tasks}21/', headers=self.headers, json=task)

        assert resposta.status_code == 200

    def test_delete_task(self):
        resposta = requests.delete(
            url=f'{self.url_base_tasks}25/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0

import requests


class CC:
    def __init__(self, email, secret):
        self.endpoint = 'https://cloudns.ru/api/v1'
        self.email = email
        self.secret = secret

    def api_get(self, endpoint, params=None):
        try:
            a = requests.get(
                self.endpoint + endpoint,
                auth=(self.email, self.secret),
                params=params)
        except Exception as e:
            raise e
        else:
            if a.status_code == 200:
                return a.json()
            else:
                raise ValueError('Unexpected response code %s' % a.status_code)

    def api_post(self, endpoint, data=None):
        try:
            a = requests.post(
                self.endpoint + endpoint,
                auth=(self.email, self.secret), data=data)
        except Exception as e:
            raise e
        else:
            if a.status_code == 200:
                return a.json()
            else:
                raise ValueError('Unexpected response code %s' % a.status_code)

    def api_put(self, endpoint, data=None):
        try:
            a = requests.put(
                self.endpoint + endpoint,
                auth=(self.email, self.secret), data=data)
        except Exception as e:
            raise e
        else:
            if a.status_code == 200:
                return a.json()
            else:
                raise ValueError('Unexpected response code %s' % a.status_code)

    def api_delete(self, endpoint, data=None):
        try:
            a = requests.delete(
                self.endpoint + endpoint,
                auth=(self.email, self.secret),
                data=data)
        except Exception as e:
            raise e
        else:
            if a.status_code == 200:
                return a.json()
            else:
                raise ValueError('Unexpected response code %s' % a.status_code)

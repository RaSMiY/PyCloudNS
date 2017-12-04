import json
import requests


class Req(object):
    def __init__(self, **params):
        self.params = params

    def do_get(self, endpoint, params=None):
        url = "{}{}".format(self.params['url'], endpoint)
        auth = (self.params['email'], self.params['secret'])
        headers = {
            "Content-Type": "application/json"
        }
        try:
            a = requests.get(url, auth=auth, params=params, headers=headers)
        except Exception as e:
            raise e
        else:
            if a.status_code == 200:
                return a.json()
            else:
                raise ValueError(
                    'Unexpected response code {}'.format(a.status_code)
                )

    def do_post(self, endpoint, data=None):
        url = "{}{}".format(self.params['url'], endpoint)
        auth = (self.params['email'], self.params['secret'])
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, auth=auth, data=json.dumps(data), headers=headers)
        return response.json()

    def do_delete(self, endpoint, data=None):
        url = "{}{}".format(self.params['url'], endpoint)
        auth = (self.params['email'], self.params['secret'])
        headers = {
            "content-type": "application/json"
        }
        return requests.delete(url, auth=auth, json=data, headers=headers).json()

    def do_put(self, endpoint, data=None):
        url = "{}{}".format(self.params['url'], endpoint)
        auth = (self.params['email'], self.params['secret'])
        headers = {
            "Content-Type": "application/json"
        }
        return requests.put(url, auth=auth, json=data, headers=headers).json()

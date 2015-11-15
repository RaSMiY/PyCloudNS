import requests

"""
Author: Vyacheslav Anzhiganov
Email: vanzhiganov@ya.ru
Date: 2014-12-01
Version: 1.0
"""


class CloudnsClient:
    def __init__(self, email, secret):
        self.cloudns_api_url = 'http://api.cloudns.ru/api.php'
        self.email = email
        self.secret = secret

    def request(self, data):
        return requests.post(self.cloudns_api_url, data=data)

    def domain_record_get_items(self, domain):
        data = {
            "email": self.email,
            "secret": self.secret,
            'method': "domain_record_get_items",
            "domain": domain
        }
        return self.request(data)

    def domain_record_delete(self, domain, record_id):
        data = {
            "email": self.email,
            "secret": self.secret,
            'method': "domain_record_delete",
            "domain": domain,
            "record_id": record_id
        }
        return self.request(data)

    def domain_record_delete_by_host(self, domain, host, rtype):
        data = {
            "email": self.email,
            "secret": self.secret,
            'method': "domain_record_delete_by_host",
            "domain": domain,
            "host": host,
            "type": rtype
        }
        return self.request(data)

    def domain_record_add(self, domain, host, rtype, destination, priority=0):
        data = {
            "email": self.email,
            "secret": self.secret,
            'method': "domain_record_add",
            "domain": domain,
            "host": host,
            "type": rtype,
            "destination": destination,
            "priority": priority,
        }
        return self.request(data)

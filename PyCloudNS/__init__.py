import requests


class CC:
    def __init__(self, email, secret):
        self.endpoint = 'http://api.cloudns.ru/api'
        self.email = email
        self.secret = secret


class CloudNSZones(CC):
    def add(self, zone_name):
        return requests.post(
            self.endpoint + "/zones/",
            auth=(self.email, self.secret),
            data={"zone": zone_name},
        ).json()

    def get(self):
        return requests.get(
            self.endpoint + "/zones/",
            auth=(self.email, self.secret)
        ).json()

    def delete(self, zone_id):
        return requests.delete(
            self.endpoint + '/zones/',
            auth=(self.email, self.secret),
            data={"zone_id": zone_id}
        ).json()

    # TODO: create method `update()`
    def update(self):
        return None


class CloudNSLayers(CC):
    def get(self, zone_id):
        return requests.get(
            "%s/zones/%s/layers/" % (self.endpoint, zone_id),
            auth=(self.email, self.secret)
        ).json()

    def create(self):
        return None

    def delete(self):
        return None

    def update(self):
        return None

class CloudNSRecords(CC):
    def get(self, zone_id, layer='default'):
        return requests.get(
            "%s/zones/%s/records/?layer=%s" % (self.endpoint, zone_id, layer),
            auth=(self.email, self.secret)
        ).json()

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

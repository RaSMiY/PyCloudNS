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

    def add(self, zone_id, layer, name, ttl, rtype, data, priority=0):
        return requests.post(
            "%s/zones/%s/records/" % (self.endpoint, zone_id),
            auth=(self.email, self.secret),
            data={'layer': layer, 'name': name, 'ttl': ttl, 'type': rtype, 'data': data, 'priority': priority},
        ).json()

    def delete(self, zone_id, layer, record_id):
        return requests.delete(
            "%s/zones/%s/records/" % (self.endpoint, zone_id),
            auth=(self.email, self.secret),
            data={'layer': layer, 'record_id': record_id}
        ).json()

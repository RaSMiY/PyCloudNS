from .common import CC
import requests


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

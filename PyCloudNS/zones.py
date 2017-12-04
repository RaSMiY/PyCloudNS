# coding: utf-8

from .req import Req


class Zones(Req):
    def __init__(self, url, email, secret):
        super().__init__(url=url, email=email, secret=secret)

    def get(self):
        """Get list domains"""
        return self.do_get("/zones/")

    def create(self, **zone_details):
        """Create a new zone"""
        return self.do_post("/zones/", data=zone_details)

    def delete(self, zone_name):
        """Delete specified zone by ID"""
        return self.do_delete('/zones/{}'.format(zone_name))

    def update(self):
        """Update zone"""
        # TODO: create method `update()`

        return None

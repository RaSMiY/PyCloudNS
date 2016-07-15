# coding: utf-8

import requests
from .common import CC


class CloudNSZones(CC):
    def get(self, zone_name=None, zone_id=None):
        """Get list domains
        """
        if zone_name:
            return self.api_get("/zones/", {"zone_name": zone_name})
        elif zone_id:
            return self.api_get("/zones/", {"zone_id": zone_id})
        else:
            return self.api_get("/zones/")

    def add(self, zone_name):
        """Create a new zone
        """
        return self.api_post("/zones/", data={"zone": zone_name})

    def delete(self, zone_id):
        """Delete specified zone by ID
        """
        return self.api_delete('/zones/', data={"zone_id": zone_id})

    def update(self):
        """Update zone
        TODO: create method `update()`
        """
        return None

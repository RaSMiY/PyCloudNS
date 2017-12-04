from .req import Req


class Records(Req):
    def __init__(self, url, email, secret):
        super().__init__(url=url, email=email, secret=secret)

    def get(self, zone_id, layer='default'):
        return self.do_get("/zones/{}/{}/records".format(zone_id, layer))

    def create(self, zone, layer, name, ttl, rtype, data, priority=0):
        url = "/zones/{}/{}/records".format(zone, layer)
        data = {
            'layer': layer,
            'name': name,
            'ttl': ttl,
            'record_type': rtype,
            'value': data,
            'priority': priority
        }
        return self.do_post(url, data=data)

    def delete(self, zone, layer, record_id):
        url = "/zones/{}/{}/records/{}".format(zone, layer, record_id)
        return self.do_delete(url)

    def update(self, zone, layer, record_id, **params):
        url = "/zones/{}/{}/records/{}".format(zone, layer, record_id)
        return self.do_put(url, data=params)

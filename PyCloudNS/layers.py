from .req import Req


class Layers(Req):
    def __init__(self, url, email, secret):
        super().__init__(url=url, email=email, secret=secret)

    def get(self, zone):
        return self.do_get("/zones/{}".format(zone))

    def create(self, zone, regions):
        return self.do_post("/zones/{}".format(zone), data={'regions': regions})

    def delete(self, zone, layer):
        return self.do_delete("/zones/{}/{}".format(zone, layer))

    def update(self):
        return None

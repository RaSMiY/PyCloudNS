
from .zones import Zones
from .layers import Layers
from .records import Records
from .regions import Regions


class CloudNS(object):
    def __init__(self):
        self.url = 'https://zettadns.com/api/dns/0.1'
        self.email = ''
        self.secret = ''

    def regions(self):
        return Regions(url=self.url, email=self.email, secret=self.secret)

    def zones(self):
        return Zones(url=self.url, email=self.email, secret=self.secret)

    def layers(self):
        return Layers(url=self.url, email=self.email, secret=self.secret)

    def records(self):
        return Records(url=self.url, email=self.email, secret=self.secret)

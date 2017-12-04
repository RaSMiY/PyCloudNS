# coding: utf-8

from .req import Req


class Regions(Req):
    def __init__(self, url, email, secret):
        super().__init__(url=url, email=email, secret=secret)

    def get(self):
        """Get list domains"""
        return self.do_get("/regions/")

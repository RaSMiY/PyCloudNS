# PyCloudNS

Python ZettaDNS API Client library

Package on PyPi: https://pypi.python.org/pypi/PyCloudNS

## How to use

Import & define auth parameters

    from PyCloudNS import CloudNS

    ns = CloudNS()
    ns.email = 'email@gmail.com'
    ns.secret = 'mySecretAPIKEY123'

### Zones

Get list all zones

    ns.zones().get()

Add new DNS zone

    ns.zones().create('mydomain.com', zone_type='master', geo=False)

Delete zone

    ns.zones().delete("mydomain.com")

### Layers

Get layers

    ns.layers().get("mydomain.com")

Response

    {"items": ["default"], "status": 0, "total": 1}

Delete layer

    ns.layers().delete("mydomain.com", "qwerrty")

### Records

Get records

    ns.records().get("mydomain.com", "default")

Create new record

    ns.records().create("mydomain.com", "default", name="test1", ttl=12345, rtype="A", data="1.2.3.4"))

Update record

    ns.records().update("mydomain.com", "default", 4, )

Delete record

    ns.records().delete("mydomain.com", "default", 4)

### Regions

    ns.regions().get()

Response

    {'items': ['polinesia'], 'status': 0, 'total': 23}
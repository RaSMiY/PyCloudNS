# PyCloudNS

Python CloudNS API Client library

## How to use

Import & define auth parameters

```
from PyCloudNS import CloudNSZones, CloudNSLayers, CloudNSRecords

email = dev@gmail.com
secret = mySecretAPIKEY123
```

Get list all zones

`CloudNSZones(email, secret).get()`

Get zone by ID
`CloudNSZones(email, secret).get(zone_id=10)`

Get zone by name

`CloudNSZones(email, secret).get(zone_name='test5.com')`

Add new DNS zone

```
CloudNSZones(email, secret).add('mydomain.com')
```

Delete zone

```
CloudNSZones(email, secret).delete(1)
```

# print cz.delete('test1.com')

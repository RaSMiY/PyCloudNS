from .common import CC


class CloudNSRecords(CC):
    def get(self, zone_id, layer='default'):
        return self.api_get("/zones/%s/records/" % zone_id, {"layer": layer})

    def add(self, zone_id, layer, name, ttl, rtype, data, priority=0):
        return self.api_post(
            "/zones/%s/records/" % zone_id,
            data={
                'layer': layer,
                'name': name,
                'ttl': ttl,
                'type': rtype,
                'data': data,
                'priority': priority})

    def delete(self, zone_id, layer, record_id):
        return self.api_delete(
            "/zones/%s/records/" % zone_id,
            data={'layer': layer, 'record_id': record_id}
        )

    def update(self, zone_id, layer, record_id, name, ttl, rtype, data, priority=0):
        return self.api_put(
            "/zones/%s/records/" % zone_id,
            data={
                'layer': layer,
                'record_id': record_id,
                'name': name,
                'ttl': ttl,
                'type': rtype,
                'data': data,
                'priority': priority})

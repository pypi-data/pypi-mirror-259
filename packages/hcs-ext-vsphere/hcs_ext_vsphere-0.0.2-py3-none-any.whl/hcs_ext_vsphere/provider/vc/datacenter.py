from . import govc


def find_moid_by_name(name: str) -> str:
    ret = govc.get(f"datacenter.info -json /{name}")
    if ret:
        return ret["datacenters"][0]["self"]["value"]

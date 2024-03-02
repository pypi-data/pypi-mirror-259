import logging
from typing import Any, Optional

from pydantic import BaseModel

from ipfabric import models

logger = logging.getLogger("ipfabric")


class Addressing(BaseModel):
    client: Any = None
    sn: Optional[str] = None

    @property
    def arp_table(self):
        return models.Table(client=self.client, endpoint="tables/addressing/arp", sn=self.sn)

    @property
    def mac_table(self):
        return models.Table(client=self.client, endpoint="tables/addressing/mac", sn=self.sn)

    @property
    def managed_ip_ipv4(self):
        return models.Table(client=self.client, endpoint="tables/addressing/managed-devs", sn=self.sn)

    @property
    def managed_ip_ipv6(self):
        return models.Table(client=self.client, endpoint="tables/addressing/ipv6-managed-devs", sn=self.sn)

    @property
    def managed_duplicate_ip(self):
        return models.Table(client=self.client, endpoint="tables/addressing/duplicate-ip", sn=self.sn)

    @property
    def nat44(self):
        return models.Table(client=self.client, endpoint="tables/security/nat44", sn=self.sn)

    @property
    def ipv6_neighbor_discovery(self):
        return models.Table(client=self.client, endpoint="tables/addressing/ipv6-neighbors", sn=self.sn)

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .account_whitelist import *
from .api_key import *
from .application import *
from .data_feed import *
from .data_source import *
from .dnsview import *
from .get_dns_sec import *
from .get_networks import *
from .get_record import *
from .get_zone import *
from .monitoring_job import *
from .notify_list import *
from .provider import *
from .pulsar_job import *
from .record import *
from .subnet import *
from .team import *
from .tsigkey import *
from .user import *
from .zone import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_ns1.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_ns1.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "ns1",
  "mod": "index/aPIKey",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/aPIKey:APIKey": "APIKey"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/accountWhitelist",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/accountWhitelist:AccountWhitelist": "AccountWhitelist"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/application",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/application:Application": "Application"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/dataFeed",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/dataFeed:DataFeed": "DataFeed"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/dataSource",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/dataSource:DataSource": "DataSource"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/dnsview",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/dnsview:Dnsview": "Dnsview"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/monitoringJob",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/monitoringJob:MonitoringJob": "MonitoringJob"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/notifyList",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/notifyList:NotifyList": "NotifyList"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/pulsarJob",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/pulsarJob:PulsarJob": "PulsarJob"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/record",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/record:Record": "Record"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/subnet",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/subnet:Subnet": "Subnet"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/team",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/team:Team": "Team"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/tsigkey",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/tsigkey:Tsigkey": "Tsigkey"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/user",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/user:User": "User"
  }
 },
 {
  "pkg": "ns1",
  "mod": "index/zone",
  "fqn": "pulumi_ns1",
  "classes": {
   "ns1:index/zone:Zone": "Zone"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "ns1",
  "token": "pulumi:providers:ns1",
  "fqn": "pulumi_ns1",
  "class": "Provider"
 }
]
"""
)

import global_setting
from conf import hosts
import redis_connector as redis

for h in hosts.monitored_hosts:
    print(h.hostname,h.ip_address)
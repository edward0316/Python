import global_setting
from conf import hosts
import redis_connector as redis
import json

def push_configure_data_to_redis():

    for h in hosts.monitored_hosts:
        config_dic = {}

        for k,v in h.services.items():
            config_dic[k] = [v.interval, v.plugin_name]
        print config_dic

        redis.r['configuration::%s' % h.hostname] = json.dumps(config_dic)

push_configure_data_to_redis()
#!/usr/bin/env python

import threading
import global_setting
import json
import time, sys
import plugin_api
import redis_connector as redis

hostname = 'edward_server'


def pull_config_from_redis():
    config_data = redis.r.get("configuration::%s" % hostname)
    if config_data is not None:
        config_data = json.loads(config_data)
    else:
        sys.exit('Error:could not found any configuration data on monitor server!')
    return config_data

def run(service_config):
    service_name, interval, plugin_name = service_config
    #print(interval, plugin_name)

    plugin_func = getattr(plugin_api, plugin_name)
    res = plugin_func()
    print res
    return res


host_config = pull_config_from_redis()

#for k,v in host_config.items():
#    print k,v
#    t = threading.Thread(target=run, args=((k,v[0],v[1]),))
#    t.start()
#print(host_config)

while True:
    for service_name, v in host_config.items():
        interval, plugin_name, last_run = v
        if (time.time() - last_run) >= interval: #time to run monitor
            t = threading.Thread(target=run, args=((service_name, interval, plugin_name),))
            t.start()
            #update time stamp
            host_config[service_name][2] = time.time()
        else:
            next_run_time = interval - (time.time() - last_run)
            print "\033[32;1mService %s will run in next %s ...\033[0m" % (service_name, next_run_time)

    time.sleep(1)

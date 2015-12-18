import global_setting
from conf import hosts
import redis_connector as redis
import json
import time

def push_configure_data_to_redis():

    for h in hosts.monitored_hosts:
        config_dic = {}

        for k,v in h.services.items():
            config_dic[k] = [v.interval, v.plugin_name, 0] #0 means the first time stamp
        print config_dic

        redis.r['configuration::%s' % h.hostname] = json.dumps(config_dic)

push_configure_data_to_redis()


#receive data

channel = 'fm_103'
msg_queue = redis.r.pubsub()#bind listen instance
msg_queue.subscribe(channel)
msg_queue.parse_response()

count = 0
while True:
    data = msg_queue.parse_response()
    print data
    print 'round %s :: ' % count
    client_data = json.loads(data[2])
    client_data['recv_time'] = time.time()
    redis_key = '%s::%s' % (client_data['hostname'], client_data['service_name'])

#   dump client service data into redis
    redis.r[redis_key] = json.dumps(client_data)

    for k, v in client_data.items():
        print(k, '----->', v)

    count += 1
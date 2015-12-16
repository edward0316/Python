import redis_connector as redis
import pickle

channel = 'monitor_queue'

msg_queue = redis.r.pubsub() #bind listen instance
msg_queue.subscribe(channel)
msg_queue.parse_response()

count = 0

while True:
    data = msg_queue.parse_response()

    print('round %s :: ' % count,pickle.loads(data[2]))

    count += 1
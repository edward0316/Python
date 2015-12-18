#!/usr/bin/env python
import global_setting
from conf import hosts
import redis_connector as redis
import json
import time


def fetch_monitored_list():
    for h in hosts.monitored_hosts:
        print h.hostname
        for service_name, v in h.services.items(): #loop all the monitored services in this host
            print(service_name, v.interval)
            service_key = '%s::%s' % (h.hostname, service_name)
            service_data = redis.r.get(service_key)
            if service_data is not None:
                service_data = json.loads(service_data)
                print(service_data['recv_time'])
                time_pass_since_last_recv = time.time() - service_data['recv_time']
                print('time pass', time_pass_since_last_recv)
                if time_pass_since_last_recv >= v.interval + 10: #haven't receive any data from this service more than the interval time
                    print("\033[41;1mService %s has no data for %s\033[0m" % (service_name, time_pass_since_last_recv ))
                else:#data sent from client on time
                    if service_data['data']['status'] == 0: #valid data
                        for index, val in v.triggers.items(): #loop all the indexes in the loop
                            print '====>', index, val
                            data_type, warning, critical =val
                            index_val = service_data['data'][index]
                            if data_type == 'percentage' or data_type is int:
                                index_val = float(index_val)

                            #compare part
                            if index in v.lt_operator:#use < operator calculation
                                if index_val < critical:
                                    print " \033[31;1mService %s crossed critical line %s, current val is %s\033[0m" % (index, critical, index_val)
                                elif index_val < warning:
                                   print " \033[33;1mService %s crossed warning line %s, current val is %s\033[0m" % (index, critical, index_val)

                            else:
                                if index_val > critical:
                                    print " \033[31;1mService %s crossed critical line %s, current val is %s\033[0m" % (index, critical, index_val)
                                elif index_val > warning:
                                    print " \033[33;1mService %s crossed warning line %s, current val is %s\033[0m" % (index, critical, index_val)

                            print index, val

            else:
                pass



if __name__ == '__main__':
    fetch_monitored_list()
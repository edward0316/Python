#!/usr/bin/env python

from generic import DefaultService

class cpu(DefaultService):
    name = 'cpu'
    interval = 60
    plugin_name = 'cpu_info'
    triggers = {
        'iowait':['percentage',5.5,90],
        'system':['percentage',5,90],
        'idle':['percentage',20,10],
        'user':['percentage',80,90],
        'steal':['percentage',80,90],
        'nice':[None,80,90],
    }
    data_from = 'agent'
    graph_index = {
        'index':[],
        'title':name,
    }
    lt_operator = []

class load(DefaultService):
        name = 'load'
        interval = 120
        plugin_name = 'load_info'
        triggers = {
                #'uptime': ['string', 'd',90],
                #'ptime': ['string', 'd',90],
                'load1': [int, 4,9],
                'load5': [int, 3,7],
                'load15': [int, 3,9],
        }
    #    graph_index = {
    #   'index':['load1', 'load5', 'load15'],
     #    'title': 'Load status' ,
   # }
class memory(DefaultService):
    name = 'memory'
    plugin_name = 'mem_info'
    triggers = {
        'SwapUsage_p':['percentage', 66, 91],
        'MemUsage_p': ['percentage', 68, 92],
        'MemUsage': [None, 60, 65],
    }
    #graph_index = {
    #    'index': ['MemUsage','SwapUsage'],

    #}

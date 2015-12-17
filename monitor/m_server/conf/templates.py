#!/usr/bin/env python
from services import linux

class BaseTemplate:
    name = None
    services = None
    hostname = None
    ip_address = None
    port = None
    os = None

class LinuxGeneralServices(BaseTemplate):
    def __init__(self):
        self.name = 'Linux General Services'
        self.services = {
            'cpu':linux.cpu(),
            'memory': linux.memory(),
            'load': linux.load(),
        }

class WindowsGeneralService(BaseTemplate):
    name='Windows General Services'
    hosts=['localhost','www.baidu.com']
    services = {
        'load': linux.load(),
        'memory': linux.memory(),
        'cpu': linux.cpu(),
    }
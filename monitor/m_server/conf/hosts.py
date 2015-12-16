import templates
import copy

# for host edward_server
h1 = templates.LinuxGeneralServices()
h1.services = copy.deepcopy(h1.services)
#we have to use deepcopy to make sure that we only change the attribute of one object.
#if not using deepcopy, one change will enfluence all objects.
h1.hostname = 'edward_server'
h1.ip_address = '192.168.73.11'
h1.port = 22
h1.os = 'CentOS 7'
h1.services['cpu'].interval = 38
print h1.services['cpu'].interval

#print h1.services

h2 = templates.LinuxGeneralServices()
h2.services = copy.deepcopy(h2.services)
h2.hostname = 'kathy_server'
h2.ip_address = '192.168.73.12'
h2.port = 22
h2.os = 'ubuntu'
h2.services['cpu'].interval = 40
print h2.services['cpu'].interval

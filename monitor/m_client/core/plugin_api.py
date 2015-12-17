import global_setting
from plugins import cpu, load, memory




def cpu_info():
    data = cpu.monitor()
    #print data
    return data

cpu_info()

def load_info():
    data = load.monitor()
    #print data
    return data

def mem_info():

    return memory.monitor()


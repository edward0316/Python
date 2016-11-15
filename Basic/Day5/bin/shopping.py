import GeneralSetting
import sys
try:
    cmd = sys.argv[1]
    if cmd == "start":
        import conf.menu
    else:
        print("Please add 'start' as the parameter")
except:
    print("Please add 'start' as the parameter")


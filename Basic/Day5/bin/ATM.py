import GeneralSetting
import sys
try:
    cmd = sys.argv[1]
    if cmd == "start":
        import modules.core.ATM
    else:
        print("Please add 'start' as the first parameter")
except:
    print("Please add 'start' as the first parameter 1")
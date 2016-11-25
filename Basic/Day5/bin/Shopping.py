import GeneralSetting
import sys
try:
    cmd = sys.argv[1]
except:
    print("Please add 'start' as the first parameter.")
if cmd == "start":
    import modules.core.Shopping
else:
    print("Please add 'start' as the first parameter.")





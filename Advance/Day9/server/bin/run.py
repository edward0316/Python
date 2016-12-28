import GeneralSetting
import sys
import socketserver


try:
    cmd = sys.argv[1]
except:
    print("Please add 'start' as the first parameter.")
if cmd == "start":
    import module.ftp_server
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), module.ftp_server.FTPserver)
    server.serve_forever()
else:
    print("Please add 'start' as the first parameter.")





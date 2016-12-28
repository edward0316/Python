#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import os
import socket
import json
import sys

ip_port = ('127.0.0.1', 9999)

class MyFTP:
    def __init__(self):
        self.s = socket.socket()
        self.s.connect(ip_port)
        welcome_msg = self.s.recv(1024)#receiving welcome text
        print(welcome_msg.decode())
        while True:
            username = input("Please input your username: ").strip()
            password = input("Please input your password: ").strip()
            send_data = "%s|%s" % (username, password)
            self.s.send(bytes(send_data, encoding="utf8")) #send username and password
            identify = self.s.recv(1024).decode()#receiving the result of login check
            identify_msg, flag = identify.split("|")
            if flag == "0":#pass
                print(identify_msg)
            else:#deny
                print(identify_msg)
                continue
            while True:
                cmd = input("Please input the command (put, get, list or chdir): ").strip()
                #send cmd
                self.s.send(bytes(cmd, encoding="utf8"))
                #recieve result of cmd check
                back = self.s.recv(1024).decode()
                #print(back)
                msg, flag = back.split("|")
                #print(flag)
                if flag == "1":
                    print(msg)
                    continue
                #run function
                fun = getattr(self, cmd)
                f = fun()


    def put(self):
        path = input("Please input the path: ")
        #judge that does the file exist.
        if os.path.isfile(path):
            #find out size of the file
            file_size = os.stat(path).st_size
            #isolate the file name from the path
            filename = path.split("/")[-1]
            #create a dic for sending to the server
            msg_data = {'filename': filename, 'file_size': file_size}
            #send the dic to server
            self.s.send(bytes(json.dumps(msg_data), encoding="utf8"))
            #receive start flag
            start_flag = self.s.recv(1024).decode()
            if start_flag == "start":
                #open the file and send it
                f = open(path, "rb")
                i = 0
                for line in f:
                    self.s.send(line)
                    i+=len(line)
                    #print the process bar
                    self.view_bar(i, file_size)
                f.close()
            print("\nsuccessfully")

    def get(self):
        pass

    def list(self):
        #send start flag
        self.s.send(bytes("start", encoding="utf8"))
        #receive the length of output
        output_len = int(self.s.recv(1024).decode())
        #send start flag
        self.s.send(bytes("start", encoding="utf8"))
        recv_len = 0
        msg = b""
        #receive output
        while recv_len < output_len:
            recv_data = self.s.recv(1024)
            msg += recv_data
            recv_len += len(recv_data)
        msg = msg.decode()
        print(msg)



    def chdir(self):
        while True:
            path = input('Please input the path: ').strip().split('\\')
            #send path to server
            self.s.send(bytes(json.dumps(path), encoding="utf8"))
            #receive the result of the function.
            res = self.s.recv(1024).decode()
            #identify whether the function running successful or failed
            if res == "1":#fail
                print("The route does not exist.")
                continue
            else:#successfully
                print("The route has been change successfully.")
                break



    #process bar
    def view_bar(self, num, total):
        rate = num / total
        rate_num = int(rate * 100)
        r = '\r[%s%s]%d%%' % ("=" * rate_num, " " * (100 - rate_num), rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush()


if __name__ == "__main__":
    start = MyFTP()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Edward
import os
import socketserver
import json

class FTPserver(socketserver.BaseRequestHandler):
    def handle(self):
        # welcome text
        self.request.sendall(bytes("Welcome to the FTP server!".center(40,"*"), encoding='utf8'))
        while True:
            try:
                data = self.request.recv(1024)#receiving username and password
                self.username, password = data.decode().split("|")
                #load the xml file, and identify the user
                res = self.identify(self.username, password)
                #send the result back to client
                if res == 1:# Login successfully. 1 is a tag for client to identify whether the loging process successful or fail.
                    msg = "Your password or username is not correct.|1"
                    self.request.sendall(bytes(msg, encoding="utf8"))
                    continue
                else:#login faild.
                    msg = "welcome %s|0" % self.username
                    self.request.sendall(bytes(msg, encoding="utf8"))
                    self.working_fold = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", self.username)
                    #change the working fold to the home of user.
                    os.chdir(self.working_fold)
                while True:
                    #receiving the cmd
                    cmd = self.request.recv(1024).decode()
                    #check cmd
                    if hasattr(self, cmd):
                        ret = getattr(self, cmd)
                        print(hasattr(self, cmd))
                        #run function
                        t = ret()
                    else:
                        #send fail informtaion
                        self.request.sendall(bytes("Please input the correct cmd.|1", encoding="utf8"))

            except Exception:
                break

    def identify(self, username, password):
        from xml.etree import ElementTree as ET
        tree = ET.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "profile.xml"))
        root = tree.getroot()
        try:
            p = root.find("%s/password" % username)
            passwd = str(p.text)
        except Exception:
            return 1
        if password == passwd:
            return 0
        else:#log information can be added in here
            return 1

    def put(self):
        msg = "Please input the path: |0"
        #send cmd check successful information
        self.request.sendall(bytes(msg,encoding="utf8"))
        #receive the file name and file size
        recv = self.request.recv(1024)
        recv = json.loads(recv.decode())
        #print(recv)
        max_size = recv["file_size"]
        print(max_size)
        recv_size = 0
        filename = recv["filename"]
        #send start flag
        self.request.sendall(bytes("start", encoding="utf8"))
        f = open(filename, "wb")
        #recive file
        while recv_size < max_size:
            recv_data = self.request.recv(4096)
            f.write(recv_data)
            recv_size+=len(recv_data)
            #print("recv_data:%d | max_data:%s" % (recv_size, max_size))
        print("successfully")
        f.close()

    def get(self):
        """
        This function is used to download a file from the server.
        It is very similar with function put. Therefore, it gets passed.
        :return:
        """
        pass

    def list(self):
        import subprocess
        #send the cmd check successful information
        self.request.sendall(bytes("cmd correct |0", encoding="utf8"))
        #receive a start flag
        recv = self.request.recv(1024).decode()
        if recv == "start":
            obj = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)
            cmd_out = obj.stdout.read()
            obj.stdout.close()
            cmd_len = len(cmd_out)
            #send the length of the output to client to avoid a stick package
            self.request.sendall(bytes(str(cmd_len), encoding="utf8"))
            #receive a start flag
            back = self.request.recv(1024).decode()
            if back == "start":
                #send output
                self.request.sendall(cmd_out)


    def chdir(self):
        msg = "Please input the path: |0"
        #send the information of cmd check successfully
        self.request.sendall(bytes(msg, encoding="utf8"))
        while True:
            #receive the path
            path = json.loads(self.request.recv(1024).decode())
            #judge that is there any .. in the path to go back to the parent fold
            if ".." in path:
                level = path.count("..")
                #go to the parent fold
                for i in range(0,level):
                    self.working_fold = os.path.dirname(self.working_fold)
                    os.chdir(self.working_fold)
                    path.remove("..")
                #create a new path
                for i in path:
                    self.working_fold = os.path.join(self.working_fold, i)
                #try to change to the new path
                try:
                    os.chdir(self.working_fold)
                    self.request.sendall(bytes("0",encoding="utf8"))
                    break
                except:
                    self.request.sendall(bytes("1",encoding="utf8"))
            else:
                for i in path:
                    self.working_fold = os.path.join(self.working_fold, i)
                print(self.working_fold)
                try:
                    os.chdir(self.working_fold)
                    self.request.sendall(bytes("0",encoding="utf8"))
                    break
                except:
                    self.request.sendall(bytes("1",encoding="utf8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), FTPserver)
    server.serve_forever()
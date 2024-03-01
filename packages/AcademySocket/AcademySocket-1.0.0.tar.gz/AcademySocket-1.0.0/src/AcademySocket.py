# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:19:15 2024

@author: גלעד
"""

import socket
class Server():
    def __init__(self, port = 12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address =('0.0.0.0', port)
        self.server_socket.bind(self.server_address)
        self.client_socket = None
    
    def listen(self , number):
        self.server_socket.listen(number)
        print("Waiting for connection...")
        self.client_socket, client_address = self.server_socket.accept()
        print("Connected:", client_address)
    
    def sendString(self , string):
        while not(string.strip()):
            print("String was empty on sendString function")
            string = input("Enter new string for sendString : ")
        self.client_socket.send(string.encode())
        
    def recieveString(self):
        data = self.client_socket.recv(1024)
        data_decoded = data.decode()
        return data_decoded
                
    def receiveFile(self, file_name):
        with open(file_name, "wb") as file:
            while True:
                data_decoded = None
                data = self.client_socket.recv(1024)
                try:
                    data_decoded = data.decode()
                except:
                    pass
                if (data_decoded == 'exit'):
                    break
                else:
                    file.write(data)
            file.close()
    
    def sendFile(self, file_name):
        with open(file_name, "rb") as file:
            data = file.read(1024)
            while data:
                self.client_socket.send(data)
                data = file.read(1024)
        file.close()
        self.sendString('exit')
        
    
    def sendList(self, my_list):
        list_string = '\n'.join(map(str, my_list))
        self.sendString(list_string)
        
    
    def close(self):
        self.client_socket.close()
        self.server_socket.close()



class Client():
    def __init__(self, ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address =(ip, port)

    
    def connect(self):
        self.client_socket.connect(self.server_address)

    
    def sendString(self , string):
        self.client_socket.send(string.encode())
        
    def recieveString(self):
        data = self.client_socket.recv(1024)
        data_decoded = data.decode()
        return data_decoded
    
    def receiveFile(self, file_name):
        with open(file_name, "wb") as file:
            while True:
                data_decoded = None
                data = self.client_socket.recv(1024)
                try:
                    data_decoded = data.decode()
                except:
                    pass
                if (data_decoded == 'exit'):
                    break
                else:
                    file.write(data)
            file.close()
    
    def sendFile(self, file_name):
        print(file_name)
        with open(file_name, "rb") as file:
            data = file.read(1024)
            while data:
                self.client_socket.send(data)
                data = file.read(1024)
        file.close()
        self.sendString('exit')
    
    def sendList(self, my_list):
        list_string = '\n'.join(map(str, my_list))
        self.sendString(list_string)
        
    
    def close(self):
        self.client_socket.close()
    
    
    
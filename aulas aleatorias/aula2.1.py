from socket import *
servidor="127.0.0.1"
porta=8080
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen
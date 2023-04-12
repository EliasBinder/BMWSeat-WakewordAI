import socket

from src.udpServer.inputHandler import handle

def createServer(port):
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server.bind(('127.0.0.1', port))
    while True:
        bytesAddressPair = server.recvfrom(1024)
        message = bytesAddressPair[0]
        handle(message)

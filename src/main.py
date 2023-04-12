from src.tcpClient.client import setupConnection
from src.udpServer.server import createServer

PORT = 5001
PORT_MAINAPPLICATION = 5000

if __name__ == '__main__':
    print('Initializing AI model...')
    # TODO: Initialize AI model
    print('🚀 Starting TCP client on port ' + str(PORT_MAINAPPLICATION) + '...')
    setupConnection(PORT_MAINAPPLICATION)
    print('📡 Starting UDP server on port ' + str(PORT) + '...')
    createServer(PORT)


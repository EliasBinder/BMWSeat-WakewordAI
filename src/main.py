from src.udpServer.server import createServer

PORT = 5001

if __name__ == '__main__':
    print('Starting UDP server on port ' + str(PORT) + '...')
    createServer(PORT)


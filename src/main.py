import threading

from src.ai.model_runtime import start_prediction
from src.tcpClient.client import setup_connection

PORT = 5001
PORT_MAINAPPLICATION = 5000

if __name__ == '__main__':

    event = threading.Event()

    print('🚀 Starting TCP client on port ' + str(PORT_MAINAPPLICATION) + '...')
    setup_connection(PORT_MAINAPPLICATION, event)
    print('Initializing AI model...')
    start_prediction(event)


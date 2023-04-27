from socket import socket
import json
import _thread as thread

from src.tcpClient.router import handleAction

clientSocket = socket()


def setup_connection(serverPort=5000, event=None):
    serverProps = ('127.0.0.1', serverPort)
    try:
        clientSocket.connect(serverProps)
        print(f"[TCPClient] TCP Connection with main application established: {serverProps}")
        handshake = {
            "type": "handshake",
            "role": "WakewordAI"
        }
        clientSocket.send(json.dumps(handshake).encode())
        print("[TCPClient] Handshake sent.")
        thread.start_new_thread(startListening, (event,))
    except Exception as error:
        print(f"[TCPClient] Something went wrong: \n{error}")


def startListening(event):
    while True:
        data = clientSocket.recv(1024)
        data = json.loads(data)
        if data["type"] == "action":
            action = data["action"]
            handleAction(action, event, data["data"])


def sendWakeCommand():
    clientSocket.send("{"
                      "    \"type\": \"action\","
                      "    \"action\": \"wake\""
                      "}".encode())
    print("[TCPClient] WAKE command sent.")

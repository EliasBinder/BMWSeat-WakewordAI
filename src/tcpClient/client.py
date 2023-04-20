from socket import socket
import json
import _thread as thread

from src.tcpClient.router import handleAction

clientSocket = socket()


def setupConnection(serverPort=5000):
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
        thread.start_new_thread(startListening, ())
    except Exception as error:
        print(f"[TCPClient] Something went wrong: \n{error}")


def startListening():
    while True:
        data = clientSocket.recv(1024)
        data = json.loads(data)
        if data["type"] == "action":
            action = data["action"]
            handleAction(action)


def sendWakeCommand():
    clientSocket.send("{"
                      "    \"action\": \"wake\","
                      "}".encode())
    print("[TCPClient] WAKE command sent.")

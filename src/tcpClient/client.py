from socket import socket

clientSocket = socket()


def setupConnection(serverPort=5000):
    serverProps = ('127.0.0.1', serverPort)
    try:
        clientSocket.connect(serverProps)
        print(f"[TCPClient] TCP Connection with main application established: {serverProps}")
    except Exception as errore:
        print(f"[TCPClient] Something went wrong: \n{errore}")


def sendWakeCommand():
    clientSocket.send("{"
                      "    \"action\": \"wake\","
                      "}".encode())
    print("[TCPClient] WAKE command sent.")

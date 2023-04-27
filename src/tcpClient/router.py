from src.tcpClient.handlers.listen import handleListen


def handleAction(action, event, data):
    if action == "listen":
        handleListen(event, data)
    else:
        print(f"[TCPClient] Unknown action: {action}")

from src.tcpClient.handlers.listen import handleListen


def handleAction(action):
    match action:
        case "listen":
            handleListen()
        case _:  # default
            print(f"[TCPClient] Unknown action: {action}")

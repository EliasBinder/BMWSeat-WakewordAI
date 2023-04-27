def handleListen(event, data):
    flag = data["flag"]
    print(f"[TCPClient] Received listen flag: {flag}")
    if flag:
        event.set()
    else:
        event.clear()


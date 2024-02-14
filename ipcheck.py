import socket
import re


def check(address: str) -> str:
    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

    ip = str()

    if not re.match(regex, address):
            try:
                ip = socket.gethostbyname(address)
            except Exception as e:
                print("Invalid Input for Target Address")
                print(e)
                ip = ""
    else:
        ip = address

    return ip

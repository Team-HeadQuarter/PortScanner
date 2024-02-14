from constant import SERVICE, data


# OS Detection
def osScan(target):
    pass


def insertInfo(target):
    ports = data["ports"]

    for port_number in target.oport.keys():
        description = ""
        port_strnum = str(port_number)

        if isinstance(ports[port_strnum], dict):
            description = ports[port_strnum]["description"]
        elif isinstance(ports[port_strnum], list):
            # If there is list at description(multiple items exist), take first one.
            description = ports[port_strnum][0]["description"]

        target.status[port_number][SERVICE] = description
        target.oport[port_number][SERVICE] = description

    return target


# Scanning by using OS Fingerprint DB
def activeScan(target):
    pass

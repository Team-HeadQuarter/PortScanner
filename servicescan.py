from constant import SERVICE, db, fingerprint


# Insert Service Info
def insertInfo(target):
    ports = db["ports"]

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


# OS Fingerprinting
# Could be more precise with quality information
def fgprt(target):
    os_info = fingerprint["OS_info"]
    unix_info = os_info["Linux/Unix"]
    win_info = os_info["Windows"]
    if target.ttl < unix_info["TTL_range"]["max"] and target.window < unix_info["Window_size_range"]["max"]:
        target.os = "Linux/Unix"
    elif target.ttl < win_info["TTL_range"]["max"] and target.window < win_info["Window_size_range"]["max"]:
        target.os = "Windows"
    else:
        target.os = "Unknown(Insufficient information for OS Detection)"

    return target

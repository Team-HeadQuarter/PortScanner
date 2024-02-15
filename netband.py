import ipaddress


def getiplist(ip: str, maskbit: int) -> list:
    try:
        network = ipaddress.IPv4Network(f"{ip}/{maskbit}", strict=False)
        iplist = [str(bandip) for bandip in network.hosts()]
    except ValueError as e:
        print(e)
        iplist = []
    
    return iplist
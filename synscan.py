from scapy.sendrecv import sr
from scapy.layers.inet import IP, TCP


def startScan(target):
    return setTarget(target)


def setTarget(target):
    packetDes = IP(dst=target.ip)
    packetDes /= TCP(dport=range(0, 65536), flags="S")
    
    return recScan(target, packetDes)


def recScan(target, packetDes):
    answered, unanswered = sr(packetDes, timeout=1)

    # filtering unanswered packet
    for packetDes in unanswered:
        target.status[packetDes.dport] = ["Filtered", None]

    # recording answered packet
    for (send, recv) in answered:

        # catch ICMP error message
        if recv.getlayer("ICMP"):

            eType = recv.getlayer("ICMP").eType
            eCode = recv.getlayer("ICMP").eCode

            if eCode == 3 and eType == 3:
                target.status[send.dport] = ["Closed", None]
            else:
                target.status[send.dport] = ["Exception", "Got ICMP with eType " + str(eType) + " and eCode " + str(eCode)]

        else:
            flags = recv.getlayer("TCP").sprintf("%flags%")

            # open port recv SYN/ACK
            if flags == "SA":
                target.status[send.dport] = ["Open", None]
                target.oport[send.dport] = ["Open", None]

                # send RST for half scan
                # sr(IP(dst=target.ip)/TCP(dport=send.dport, flags="R"))

            # close port recv RES
            elif flags == "R" or flags == "RA":
                target.status[send.dport] = ["Closed", None]

            # catch something else
            else:
                target.status[send.dport] = ["Exception", "Got packets with flags " + str(flags)]

    return target
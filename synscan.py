import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import AsyncSniffer
import socket
import tqdm
import time

from constant import SYN, RST, ACK
from randdist import randomize


def startScan(target):
    snf = AsyncSniffer(store=True, filter=f"ip src {target.ip}")
    snf.start()

    portlist = randomize(list(range(target.start_port, target.end_port+1)))

    for port in tqdm.tqdm(portlist):
        packet = IP(dst=target.ip) / TCP(dport=port, flags="S")
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.sendto(bytes(packet[TCP]), (target.ip, 0))
        s.close()

    time.sleep(1)
    snf.stop()

    target = parsePacket(target, snf.results)
    target = organizeTarget(target)
    target = fillFiltered(target)
    
    return target


def parsePacket(target, packets):
    for packet in packets:
        if packet.haslayer(ICMP):
            eType = packet.getlayer("ICMP").eType
            eCode = packet.getlayer("ICMP").eCode
            if eCode == 3 and eType == 3:
                target.status[packet[TCP].sport] = ["Closed", None]
            else:
                target.status[packet[TCP].sport] = ["Exception", "Got ICMP with eType " + str(eType) + " and eCode " + str(eCode)]
        elif packet.haslayer(TCP):
            ipdata = packet[IP]
            tcpdata = packet[TCP]
            if tcpdata.flags == (SYN | ACK):
                # RST Packet should be send to target. Fortunately, OS is handle the things.
                target.status[tcpdata.sport] = ["Open", None]
                target.oport[tcpdata.sport] = ["Open", None]
                target.ttl += ipdata.ttl
                target.window += tcpdata.window
            elif tcpdata.flags == RST or tcpdata.flags == (RST | ACK):
                target.status[tcpdata.sport] = ["Closed", None]
            else:
                target.status[tcpdata.sport] = ["Exception", "Got packets with flags code" + str(tcpdata.flags)]
    
    return target


def organizeTarget(target):
    if target.oport:
        # Set avg value in ttl, window
        target.ttl //= len(target.oport)
        target.window //= len(target.oport)
        target.oport = dict(sorted(target.oport.items()))

    target.status = dict(sorted(target.status.items()))

    return target


def fillFiltered(target):
    for port in range(target.start_port, target.end_port+1):
        if port not in target.status.keys():
            target.status[port] = ["Filtered", None]

    return target

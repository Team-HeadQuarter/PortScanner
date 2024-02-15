__author__ = "TeamHeadQuarter (ymiwm0322@kakao.com)"
__version__ = "3.00"
__last_modification__ = "2024.02.15"


import argparse
import time

from targetclass import Target
from ipcheck import ipcheck
import synscan
import servicescan
import netband
from constant import BITMASK
from printer import printintro, printtarget


def main():
    starttime = time.time()
    address = str()

    # Get Option
    parser = argparse.ArgumentParser(description="Service Port Scanner")
    parser.add_argument("target", metavar="127.0.0.1", type=str, help="Type Target IP Address.")
    parser.add_argument("-p", "--port", type=str, help="Port Range For Scan")
    parser.add_argument("-s", "--service", action="store_true", help="Service Port Scan(Protocol)")
    parser.add_argument("-b", "--band", type=int, help="IP/Bitmask Bandwidth Scan")
    parser.add_argument("-d", "--dist", action="store_true", help="Distributed Server Scan")
    args = parser.parse_args()

    # IP Validation Check
    address = args.target
    ip = ipcheck(address)
    if ip == "":
        print(parser.print_help())
        return -1
    
    # Create Target Object
    target = Target(ip)

    # Set Port Range(-p option)
    if args.port:
        portrange = args.port
        seport = portrange.split('-', 1)
        try:
            target.start_port = int(seport[0])
            target.end_port = int(seport[1])
            if target.start_port > target.end_port:
                print(parser.print_help())
                print("Start port number must be smaller than end port number.")
                return -1
        except Exception as e:
            print(parser.print_help())
            print(e)
            print("Invalid arguments in -p option.")
            print("{0 <= (Start Port)}-{(End Port) <= 65535}")
            return -1
    
    printintro(target, ip, address)

    # Call Scan Functions
    
    # Start distscan

    # Check band option
    if args.band:
        if args.band in BITMASK:
            # Start netbandscan
            for sub_ip in netband.getiplist(target.ip, args.band):
                subtarget = Target(sub_ip)
                subtarget.start_port = target.start_port
                subtarget.end_port = target.end_port
                print(f"Target IP: {subtarget.ip}")
                subtarget = synscan.startScan(subtarget)
                # Start Service Scan(-s option)
                if args.service:
                    # Add Port Information
                    subtarget = servicescan.insertInfo(subtarget)
                    # OS Detection (Linux / Windows)
                    subtarget = servicescan.fgprt(subtarget)

                printtarget(subtarget)
        else:
            print("-b argument is out of bitmask range.(8-32)")
            return -1

    else:
        # Start SYN Scan(default)
        target = synscan.startScan(target)

        # Start Service Scan(-s option)
        if args.service:
            # Add Port Information
            target = servicescan.insertInfo(target)
            # OS Detection (Linux / Windows)
            target = servicescan.fgprt(target)

        printtarget(target)
    
    endtime = time.time()
    duration = endtime - starttime
    print(f"Duration:\t{duration}")


if __name__ == "__main__":
    main()

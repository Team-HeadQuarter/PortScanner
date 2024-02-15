__author__ = "TeamHeadQuarter (ymiwm0322@kakao.com)"
__version__ = "1.90"
__last_modification__ = "2024.02.13"


import argparse
import time
import datetime
import pyfiglet

import targetclass
import ipcheck
import synscan
import servicescan


def main():
    starttime = time.time()
    address = str()

    # Get Option
    parser = argparse.ArgumentParser(description="Service Port Scanner")
    parser.add_argument("target", metavar="127.0.0.1", type=str, help="Type Target IP Address.")
    parser.add_argument("-p", "--port", type=str ,default="1-65535", help="Port Range For Scan")
    parser.add_argument("-s", "--service", action="store_true", help="Service Port Scan(Protocol)")
    parser.add_argument("-b", "--band", type=int, default=24, help="IP/Bitmask Bandwidth Scan")
    parser.add_argument("-d", "--dist", action="store_true", help="Distributed Server Scan")
    args = parser.parse_args()

    # IP Validation Check
    address = args.target
    ip = ipcheck.check(address)
    if ip == "":
        print(parser.print_help())
        return -1
    
    # Create Target Object
    target = targetclass.Target(ip)

    # Set Port Range(-p option)
    if args.port != "":
        portrange = args.port
        seport = portrange.split('-', 1)
        try:
            target.start_port = int(seport[0])
            target.end_port = int(seport[1])
        except Exception as e:
            print(e)
            print("Invalid arguments in port option.")
            print("{0 <= (Start Port)}-{(End Port) <= 65535}")
            return -1
    
    print()
    print('='*64)
    print()
    ascii_banner = pyfiglet.figlet_format("Team HeadQuarter")
    print(ascii_banner)
    print('='*64)
    print()
    print("Port Scanner v1.90")
    print(f"Start Port Scan\t{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")
    print()
    print(f"Target Address:\t{address}")
    print(f"Target IP:\t{ip}")
    print(f"Port Range:\t{target.start_port}-{target.end_port}")
    print()
    
    # Call Scan Functions
    
    # netbandscan

    # distscan
    
    # Start SYN Scan(default)
    target = synscan.startScan(target)

    # Start Service Scan(-s option)
    if args.service:
        # Add Port Information
        target = servicescan.insertInfo(target)
        # OS Detection (Linux / Windows)
        target = servicescan.fgprt(target)

    print()
    print('='*64)

    target.printres()
    target.savefile()

    print('='*64)
    endtime = time.time()
    duration = endtime - starttime
    print(f"Duration:\t{duration}")


if __name__ == "__main__":
    main()

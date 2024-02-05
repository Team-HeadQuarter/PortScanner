import argparse
import datetime
import time

import targetclass
import ipcheck
import synscan


def main():
    starttime = time.time()
    print("""
        ################################
        #       Team HeadQuarter       #
        ################################
        """)
    print(f"Start Port Scan\t{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")

    address = str()

    # Get Option
    parser = argparse.ArgumentParser(description="Service Port Scanner")
    parser.add_argument("target", metavar="127.0.0.1", type=str, help="Type Target IP Address.")
    parser.add_argument("-s", "--service", action="store_true", help="Service Port Scan(Protocol)")
    parser.add_argument("-b", "--band", type=int, default=24, help="IP/Bitmask Bandwidth Scan")
    parser.add_argument("-d", "--dist", action="store_true", help="Distributed Server Scan")
    args = parser.parse_args()

    # IP Validation Check
    address = args.target
    print("Target Address:\t", address)
    ip = ipcheck.check(address)
    if ip == "":
        print(parser.print_help())
        return -1
    print("Target IP:\t", ip)

    # Create Target Object
    target = targetclass.Target(ip)
    
    # Call Scan Functions
    # netbandscan
    # distscan
    # synscan
    target = synscan.startScan(target)
    # servicescan

    target.printport('o')
    target.savefile()

    endtime = time.time()
    duration = endtime - starttime
    print("Duration:\t", duration)


if __name__ == "__main__":
    main()
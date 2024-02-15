import datetime
import pyfiglet

def printintro(target, ip, address):
    print()
    print('='*64)
    print()
    ascii_banner = pyfiglet.figlet_format("Team HeadQuarter")
    print(ascii_banner)
    print('='*64)
    print()
    print("Port Scanner v2.00")
    print(f"Start Port Scan\t{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")
    print()
    print(f"Target Address:\t{address}")
    print(f"Target IP:\t{ip}")
    print(f"Port Range:\t{target.start_port}-{target.end_port}")
    print()


def printtarget(target):
    print()
    print('='*64)

    target.printres()
    target.savefile()

    print('='*64)
    print()
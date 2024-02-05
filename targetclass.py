import json

from constant import STATUS, SERVICE


class Target:
    def __init__(self, ip: str):
        self.ip = ip
        self.status = dict()
        self.oport = dict()


    def printport(self, opt):
        print(f"IP Address: {self.ip}")
        print("{0:<16}{1:<16}{2:<16}".format("Port", "Status", "Service"))
        if opt == 'a':
            for key, value in self.status.items():
                print("{0:<16}{1:<16}{2:<16}".format(key, value[STATUS], str(value[SERVICE])))
        elif opt == 'o':
            if len(self.oport) == 0:
                print("NO OPEN PORTS EXISTS!")
                return
            for key, value in self.oport.items():
                print("{0:<16}{1:<16}{2:<16}".format(key, value[STATUS], str(value[SERVICE])))
        else:
            print("Invalid Option")
            print("-a\tPrint All")
            print("-o\tPrint Open Ports Only")


    def savefile(self):
        with open("result_" + self.ip + ".json", 'w') as f:
            f.write(json.dumps(self.status, indent=4))
        with open("open_" + self.ip + ".json", 'w') as f:
            f.write(json.dumps(self.oport, indent=4))
import json

from constant import STATUS, SERVICE


class Target:
    def __init__(self, ip: str):
        self.ip = ip
        self.os = ""
        self.status = dict()
        self.oport = dict()
        self.ttl = int
        self.window = int


    def printres(self, opt):
        print("{0:<16}{1:<16}{2:<16}".format("Port", "Status", "Service"))
        print('-'*64)
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
        with open("result_" + self.ip + '_' + self.os + ".json", 'w') as f:
            json.dump(self.status, f, indent=4)
        with open("open_" + self.ip + '_' + self.os + ".json", 'w') as f:
            json.dump(self.oport, f, indent=4)
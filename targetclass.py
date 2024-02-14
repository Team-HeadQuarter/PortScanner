import json

from constant import STATUS, SERVICE


class Target:
    def __init__(self, ip: str):
        self.ip = ip
        self.status = {}
        self.oport = {}
        self.ttl = 0
        self.window = 0
        self.os = "No Option Provided"
        self.start_port = 1
        self.end_port = 65535


    def printres(self):
        if len(self.oport) == 0:
            print("NO OPEN PORTS EXISTS!")
            return

        print("OS Prediction: {}".format(self.os))
        print('-'*64)
        print("{0:<16}{1:<16}{2:<16}".format("PORT", "STATE", "SERVICE"))
        print('-'*64)

        for key, value in self.oport.items():
            print("{0:<16}{1:<16}{2:<16}".format(key, value[STATUS], str(value[SERVICE])))


    def savefile(self):
        with open("result_" + self.ip + ".json", 'w') as f:
            json.dump(self.status, f, indent=4)
        with open("open_" + self.ip + ".json", 'w') as f:
            json.dump(self.oport, f, indent=4)

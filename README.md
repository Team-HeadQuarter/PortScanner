# PortScanner(v2.0)

### Made by TeamHeadquarter

Baek YeonJu  
Jeon DoHyeong  
Lee GyeoRe  
Lee JinSu  
Lee MyungIn

---

### Overview

SYN, Service Scanning with additional functions.

---


### ⚠️ CAUTION ⚠️
1. ***Legality***:  
Port scanning can be either legal or illegal depending on the purpose. It is legitimate when performed by system administrators to assess their own network or by security professionals with proper consent. However, scanning someone else's network requires clear and explicit permission.

2. ***Avoid Service Disruption***:  
Port scanning can impose a load on the target system. Therefore, efforts should be made to minimize the impact on the performance of the target system. Consider the operational hours of the target system and be mindful of network traffic.

3. ***Legal Compliance***:  
When conducting port scans, it is essential to comply with relevant laws and regulations in the respective country or region. Illegal port scanning can result in criminal penalties.

4. ***Logging and Tracking***:  
Port scanning may leave logs on the target system. Even when scanning for legitimate purposes, it is advisable to check for logs and inform administrators to ensure transparency and cooperation.

5. ***Caution in Disclosing Security Vulnerabilities***:  
If security vulnerabilities are discovered, they should be reported to the organization in a responsible manner following the appropriate reporting process. Exercise discretion before publicly disclosing security vulnerabilities.

When performing port scans, always act ethically, responsibly, and in compliance with legal and ethical guidelines.

![정보통신망 이용촉진 및 정보보호 등에 관한 법률 제48조](./img/IS-law.png)

---

### Requirements

1. OS: Linux(Unix), Mac OS X  
2. Language: Python
3. Modules: [requirements](https://github.com/Team-HeadQuarter/PortScanner/blob/main/requirements)

---

### Usage

**Make sure all requirements are set.**

1. Open terminal
2. Go to directory that the files exist
3. Write command(Default)  
`sudo python main.py {Target IP or Domain Name}`  
4. Scan will start soon. Here is default configuration info.
    - Port range: 1-65535
    - Service scan: Not Set
    - OS Detection: Not Set
5. Result will shown in terminal, and also two files are saved in the directory named  
`result_{Target_ip}.json` and `open_{Target_ip}.json`
6. To scan specific port range, use -p(--port) option  
(ex) `sudo python main.py -p 1-6666 {Target IP or Domain Name}`
7. To do service scan, use -s(--service) option  
(ex) `sudo python main.py -s {Target IP or Domain Name}`
8. To do network band scan, use -b(--band) option  
(ex) `sudo python main.py -b 24 {Target IP or Domain Name}`
(Caution! If target is cloud infra, you could scan unexpected target in physical subnet. I recommend not to try on cloud infra.)

More information would be provide by write command  
`sudo python main.py -h` or `sudo python main.py --help`

[Check demo images](https://github.com/Team-HeadQuarter/PortScanner/tree/main/img/demo)

---

### WIP

- Run in exe file(Performance is not guaranteed with `Pyinstaller`)
- Run in Windows OS(OS is block to send with raw socket)
- Generate packet without `scapy`
- Sniff without `scapy`
- Add scan speed option

---
[_Go to top_ ↑](#portscannerv20)
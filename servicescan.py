from constant import SERVICE
from portservicelist import data


# OS 판별
def osScan(target):
    pass


def insertInfo(target):
    ports = data["ports"]

    for port_number in target.oport.keys():
        description = ""
        port_strnum = str(port_number)

        if isinstance(ports[port_strnum], dict):
            description = ports[port_strnum]["description"]
        elif isinstance(ports[port_strnum], list):
            # 원소가 여러개 있는 경우 제일 첫번째 설명을 입력 - 보완 방법 찾기
            description = ports[port_strnum][0]["description"]

        target.status[port_number][SERVICE] = description
        target.oport[port_number][SERVICE] = description

    return target


# 서비스 판별법 - nmap의 DB의 fingerprint로 유사도 비교 후 출력
def activeScan(target):
    pass
import re

# Định dạng có thể có: 'chuỗi'
pattern = r"^'.*'$"

def get_port(ports: str):
    if re.match(pattern, ports):
        ports = ports[1:-1]
    ports = ports.replace(" ", "")
    try:
        ans = []
        if ports.find(",") != -1:
            ans = [int(number) for number in ports.split(",")]
        elif ports.find("-") != -1:
            ranges = ports.split("-")
            begin = int(ranges[0])
            end = int(ranges[1])
            ans = [*range(begin, end + 1)]
        else:
            ans = [int(ports)]
        return ans
    except:
        return None
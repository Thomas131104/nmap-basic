import socket
import threading
import scapy.all as scapy


lock = threading.Lock()


### Hàm chính xử lí quét TCP hoặc UDP
def __nmap(ip : str, port : int, connecting_type : str, ans : list) -> bool:
    try:
        server = None
        if connecting_type == "TCP":
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif connecting_type == "UDP":
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            return False
        server.connect((ip, port))
        with lock:
            ans.append(port)
            print(port)
        return True
    except:
        return False


# Xử lí TCP / UDP
def nmap(IP : str, PORT : list, connecting_type : str) -> list:
    ans = []
    threads = []
    for p in PORT:
        thread = threading.Thread(target=__nmap, args=(IP, p, connecting_type, ans))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    return ans



# Xử lí quét SYN
def __syn(ip : str, port : int, open_port : list) -> None:
    syn_packet = scapy.IP(dst=ip) / scapy.TCP(dport=port, flags="S") 
    response = scapy.sr1(syn_packet, timeout=5, verbose=False)
    if response:
        try:
            if response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 18: 
                with lock:
                    open_port.append(port)
        except scapy.error as e:
            print(f"Scapy error: {e}")
    else:
        print(f"No response for port {port}")


def SYN(IP : str, PORT : list) -> list:
    open_port = []
    threads = []
    for port in PORT:
        thread = threading.Thread(target=__syn, args=(IP, port, open_port))
        threads.append(thread)
        thread.start() 
    
    for thread in threads:
        thread.join() 

    return open_port
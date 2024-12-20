import argparse
import isIpAddress
import port_list
import network_process


nmap = argparse.ArgumentParser(description="Network mapping bằng Python")
nmap.add_argument('ip', type=str, help="Địa chỉ IP")
nmap.add_argument('-p', type=str, default="1-1000", help="Cổng (1 hoặc nhiều cổng)")
nmap.add_argument('-p-', action='store_true', help="Quét toàn bộ 65536 cổng")
nmap.add_argument('-sS', action='store_true', help="Quét SYN (Theo mặc định)")
nmap.add_argument('-sT', action='store_true', help="Quét TCP")
nmap.add_argument('-sU', action='store_true', help="Quét UDP")


args = nmap.parse_args()


def main():
    try:
        # Check địa chỉ IP
        ip = args.ip
        if not isIpAddress.is_valid_ip(ip):
            raise ValueError("Địa chỉ IP bị lỗi")

        # Check cổng vào
        port = []
        if args.p_:
            port = [*range(65536)]
        elif args.p:
            port = port_list.get_port(args.p)
        else:
            raise ValueError("Thiếu IP")

        print(f"Địa chỉ IP: {ip}")

        # Chọn mô hình
        ans = None
        if args.sT:
            ans = network_process.nmap(ip, port, "TCP")
        elif args.sU:
            ans = network_process.nmap(ip, port, "UDP")
        else:
            ans = network_process.SYN(ip, port)
        print("Các cổng đang mở: ", ans)


    except TypeError as TE:
        print("Lỗi đối số:", TE)
    except ValueError as VE:
        print("Lỗi giá trị cổng:", VE)



if __name__ == "__main__":
    main()
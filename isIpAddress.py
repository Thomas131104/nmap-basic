import re

def is_valid_ip(ip):
    # Biểu thức chính quy cho địa chỉ IPv4 hợp lệ
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    # Kiểm tra khớp với biểu thức chính quy
    if re.match(pattern, ip):
        return True
    else:
        return False
    

### Cách ngắn gọn hơn
# import ipaddress

# def is_valid_ip(ip):
#     try:
#         ipaddress.ip_address(ip)
#         return True
#     except ValueError:
#         return False



### Cách ngắn gọn hơn (Cách 2):
# def is_valid_ip(ip: str) -> bool:
#     try:
#         socket.inet_aton(ip)  # Kiểm tra IP hợp lệ
#         return True
#     except socket.error:
#         return False


#!/usr/bin/env python3
import socket
import requests
import time
import sys
from urllib.parse import urlparse

try:
    import colorama
    colorama.init()
except ImportError:
    pass

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def ip_to_number(ip_str):
    try:
        packed_ip = socket.inet_aton(ip_str)  
        num = int.from_bytes(packed_ip, byteorder='big')
        return num
    except Exception:
        return None

def get_ip(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except Exception:
        return None

def tcp_port_check(ip, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        start = time.time()
        sock.connect((ip, port))
        latency = (time.time() - start) * 1000
        sock.close()
        return True, latency
    except Exception:
        return False, None

def udp_port_check(ip, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        message = b'\x00'
        sock.sendto(message, (ip, port))
        sock.recvfrom(1024)
        sock.close()
        return True
    except socket.timeout:
        return True
    except Exception:
        return False

def http_check(url, timeout=5):
    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        latency = (time.time() - start) * 1000
        code = r.status_code
        reason = r.reason
        if 200 <= code < 400:
            return True, code, reason, None, latency
        else:
            return False, code, reason, None, latency
    except requests.exceptions.Timeout:
        return False, None, None, "Timeout", None
    except requests.exceptions.ConnectionError as e:
        return False, None, None, f"ConnectionError: {e}", None
    except requests.exceptions.RequestException as e:
        return False, None, None, f"RequestException: {e}", None

def normalize_url(user_input):
    u = user_input.strip()
    if u.startswith("http://") or u.startswith("https://"):
        return u
    return "http://" + u

def main():
    try:
        user_input = input("Enter IP or URL: ").strip()
    except Exception:
        print("Input error. Exiting.")
        sys.exit(1)

    if not user_input:
        print("No input provided. Exiting.")
        sys.exit(0)

    url = normalize_url(user_input)
    parsed = urlparse(url)
    host = parsed.hostname
    ip = get_ip(host)
    if not ip:
        print(f"{RED}Could not resolve IP for {host}{RESET}")
        sys.exit(1)

    ip_num = ip_to_number(ip)
    if ip_num is None:
        ip_num_str = "-"
    else:
        ip_num_str = str(ip_num)

    tcp_port = parsed.port if parsed.port else (443 if parsed.scheme == "https" else 80)
    udp_port = 53  

    print(f"{CYAN}Starting checks for {user_input}{RESET}")
    attempt = 0

    while True:
        attempt += 1

        ok_http, code, reason, error, latency_http = http_check(url)
        ok_tcp, latency_tcp = tcp_port_check(ip, tcp_port)
        ok_udp = udp_port_check(ip, udp_port)

        connection_status = f"{GREEN}ok{RESET}" if ok_http else f"{RED}error{RESET}"

        if not ok_http:
            if error:
                error_msg = error
            elif code:
                error_msg = f"{code} {reason}"
            else:
                error_msg = "-"
        else:
            error_msg = "-"

        print(f"""
{YELLOW}Attempt: {attempt}{RESET}
ip : {ip}
url : {url}
number ip : {ip_num_str}
ping: {f'{latency_http:.1f} ms' if latency_http else '-'}
connection: {connection_status}
error: {error_msg}
port tcp : {tcp_port} ({'open' if ok_tcp else 'closed'})
port udp : {udp_port} ({'open or filtered' if ok_udp else 'closed'})
----------------------------
""")

        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Interrupted by user. Exiting...{RESET}")
            break

if __name__ == "__main__":
    main()

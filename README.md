# Deltahash Auto Bot

Automated mining bot for Deltahash platform with proxy support and continuous operation.

## 🌟 Features

- ✅ Automatic mining connection
- ✅ Periodic heartbeat system
- ✅ Multi-account support
- ✅ Proxy support (optional)
- ✅ Balance tracking
- ✅ Colorful console logging
- ✅ Auto-retry mechanism
- ✅ WIB timezone support

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/febriyan9346/Deltahash-Auto-Bot.git
cd Deltahash-Auto-Bot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📝 Configuration

### 1. Create accounts.txt

Create a file named `accounts.txt` in the root directory and add your account cookies (one per line):

```
your_cookie_1
your_cookie_2
your_cookie_3
```

**How to get your cookie:**
1. Login to [Deltahash Portal](https://portal.deltahash.ai?ref=DELTA-3021AA)
2. Open browser DevTools (F12)
3. Go to Network tab
4. Refresh the page
5. Click any request to `portal.deltahash.ai`
6. Copy the entire `Cookie` header value
7. Paste it into `accounts.txt`

### 2. Create proxy.txt (Optional)

If you want to use proxies, create `proxy.txt` and add your proxies (one per line):

```
http://username:password@proxy1:port
http://username:password@proxy2:port
socks5://username:password@proxy3:port
```

**Proxy format examples:**
- `http://user:pass@ip:port`
- `socks5://user:pass@ip:port`
- `http://ip:port` (if no authentication)

## 🎮 Usage

Run the bot:
```bash
python bot.py
```

You'll be prompted to choose:
- **Option 1**: Run with proxy (requires `proxy.txt`)
- **Option 2**: Run without proxy

The bot will:
1. Login to all accounts
2. Connect to mining
3. Send heartbeat signals
4. Display earnings and balance
5. Repeat every 30 seconds

## 📊 Output Example

```
============================================================
DELTAHASH AUTO BOT
By: FEBRIYAN
============================================================
[12:34:56] [INFO] Loaded 3 accounts
============================================================
[12:34:56] [CYCLE] Cycle #1 Started
------------------------------------------------------------
[12:34:57] [INFO] Account #1/3
[12:34:57] [INFO] Proxy: http://proxy1:8080
[12:34:58] [SUCCESS] User: example_user | Balance: 1500
[12:34:59] [SUCCESS] Mining Connected | Epoch: 42
[12:35:00] [SUCCESS] Heartbeat Success | Earned: 10 | New Balance: 1510
............................................................
[12:35:02] [INFO] Account #2/3
...
------------------------------------------------------------
[12:35:30] [CYCLE] Cycle #1 Complete
============================================================

[COUNTDOWN] Next cycle in: 00:00:30
```

## 🛠️ Troubleshooting

### "File accounts.txt not found"
- Make sure `accounts.txt` exists in the same directory as `bot.py`
- Check the file has at least one cookie

### "Login Failed / Invalid Cookie"
- Your cookie may have expired
- Get a fresh cookie from the browser
- Make sure you copied the entire cookie string

### "Mining Connection Failed"
- Check your internet connection
- Verify the Deltahash portal is accessible
- Try using a different proxy (if enabled)

### Proxy Issues
- Verify proxy format is correct
- Test proxy connection separately
- Some proxies may be blocked by Deltahash

## ⚠️ Disclaimer

This bot is for educational purposes only. Use at your own risk. The author is not responsible for any account bans or issues that may arise from using this bot.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/febriyan9346/Deltahash-Auto-Bot/issues).

## 📧 Contact

- GitHub: [@febriyan9346](https://github.com/febriyan9346)
- Deltahash Referral: [https://portal.deltahash.ai?ref=DELTA-3021AA](https://portal.deltahash.ai?ref=DELTA-3021AA)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

## 💰 Support Us with Cryptocurrency

You can make a contribution using any of the following blockchain networks:

| Network | Wallet Address |
|---------|---------------|
| **EVM** | `0x216e9b3a5428543c31e659eb8fea3b4bf770bdfd` |
| **TON** | `UQCEzXLDalfKKySAHuCtBZBARCYnMc0QsTYwN4qda3fE6tto` |
| **SOL** | `9XgbPg8fndBquuYXkGpNYKHHhymdmVhmF6nMkPxhXTki` |
| **SUI** | `0x8c3632ddd46c984571bf28f784f7c7aeca3b8371f146c4024f01add025f993bf` |

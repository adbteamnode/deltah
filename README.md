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
git clone https://github.com/adbteamnode/deltah.git && cd deltah
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
5. Repeat every 60 seconds

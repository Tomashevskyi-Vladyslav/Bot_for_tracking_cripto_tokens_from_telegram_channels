# Comprehensive Documentation for Telegram Forwarding Bot

## 1. Introduction

This documentation covers a sophisticated Telegram bot designed for:
- Automated message forwarding between channels/users
- Cryptocurrency wallet address detection (BTC, ETH, SOL)
- Rule-based content management with persistent state
- Automatic monitoring and restart capabilities

The system consists of two main components:
- `main.py`: The core bot application with forwarding logic
- `rebooter.py`: A watchdog service that ensures continuous operation

Key benefits:
- 20 configurable forwarding rules with comments
- Address deduplication to prevent spam
- Cross-platform support (Linux/Windows)
- Simple text-based persistence system

## 2. Architecture Overview

### Core Components
```
graph TD
    A[Telegram API] --> B[main.py]
    B --> C[State Files]
    C -->|Rule Updates| B
    D[rebooter.py] -->|Process Check| B
    B -->|Crash| D
```

### Data Flow
1. Bot authenticates via Telethon API
2. Loads persistent state from text files
3. Listens for messages in configured channels
4. Processes messages based on active rules
5. Updates state files after each operation
6. Watchdog monitors process status every 5 seconds

## 3. System Requirements

### Minimum Specifications
- **OS**: Linux (Ubuntu/Debian preferred) or Windows 10+
- **Python**: 3.8+ (3.12 recommended)
- **RAM**: 512MB (1GB recommended)
- **Storage**: 100MB free space

### Dependencies
```
telethon==1.34.0
psutil==5.9.6
```

## 4. Quick-Start (Experienced Users)

1. Install Python 3.12:
   ```bash
   sudo apt update && sudo apt install python3.12
   ```

2. Create virtual environment:
   ```bash
   python3.12 -m venv /opt/bot-env
   source /opt/bot-env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install telethon psutil
   ```

4. Configure `main.py`:
   - Set `api_id` and `api_hash` (from my.telegram.org)
   - Configure `CHENAL_BOT` with your control channel

5. Run the system:
   ```bash
   python3 main.py  # First run to create session
   python3 rebooter.py  # In separate terminal
   ```

## 5. Full Installation Guide

### Linux Installation

1. **Python Setup**:
   ```bash
   sudo apt update
   sudo apt install -y software-properties-common curl
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   sudo apt install -y python3.12 python3.12-venv python3.12-dev
   ```

2. **Environment Setup**:
   ```bash
   python3.12 -m venv /opt/bot-env
   source /opt/bot-env/bin/activate
   ```

3. **Dependencies**:
   ```bash
   pip install telethon psutil
   ```

### Windows Installation

1. Download Python 3.12 from [python.org](https://www.python.org/)
2. During installation, check "Add Python to PATH"
3. Install dependencies:
   ```cmd
   pip install telethon psutil
   ```



---
# **Enhanced Installation Guide with Troubleshooting for Non-Technical Users**  

This section provides a **detailed, step-by-step** installation guide with **extended explanations** and **troubleshooting tips** to help non-professional users set up the Telegram Forwarding Bot without issues.  

---

## **1. Before You Begin**  
### **1.1 What You Need**  
✅ **Operating System**: Windows 10/11 or Linux (Ubuntu/Debian recommended)  
✅ **Python 3.8+** (3.12 preferred) – *We’ll guide you through installation*  
✅ **Telegram Account** (with phone number for bot authentication)  
✅ **Basic Command Line Knowledge** (we’ll explain every step)  

### **1.2 Common Pitfalls & How to Avoid Them**  
❌ **Python Not Installed Correctly** → Follow our exact steps  
❌ **Missing Dependencies** → Use `pip install` carefully  
❌ **API Credentials Not Working** → Double-check `api_id` and `api_hash`  
❌ **Bot Doesn’t Start After Crash** → Use `rebooter.py` for auto-restart  

---

## **2. Step-by-Step Installation (Detailed)**  
### **2.1 Installing Python**  
#### **For Windows Users:**  
1. **Download Python 3.12** from [python.org](https://www.python.org/downloads/)  
2. **During Installation:**  
   - ✅ Check **"Add Python to PATH"** (critical!)  
   - ✅ Click **"Install Now"** (do not customize unless you know what you’re doing)  

   **Troubleshooting:**  
   - ❗ *If you see "Python not recognized" in CMD* → Reinstall and **ensure "Add to PATH" is checked**  
   - ❗ *If installer fails* → Disable antivirus temporarily and try again  

#### **For Linux Users (Ubuntu/Debian):**  
Run these commands **one by one** in Terminal:  
```bash
sudo apt update
sudo apt install -y software-properties-common curl
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-dev
```
**Verify Installation:**  
```bash
python3.12 --version  # Should show "Python 3.12.x"
```
**Troubleshooting:**  
- ❗ *If `add-apt-repository` fails* → Run `sudo apt install software-properties-common` first  
- ❗ *If Python 3.12 not found* → Check for typos, or manually download from [python.org](https://www.python.org/downloads/)  

---

### **2.2 Setting Up the Virtual Environment (Recommended)**  
**Why?** → Prevents conflicts with other Python projects.  

#### **Windows:**  
```cmd
python -m venv bot-env
bot-env\Scripts\activate
```
#### **Linux:**  
```bash
python3.12 -m venv bot-env
source bot-env/bin/activate
```
**Expected Output:**  
- Your terminal prompt should now show `(bot-env)` at the start.  

**Troubleshooting:**  
- ❗ *"venv module not found"* → Reinstall Python and ensure "pip" is selected during setup.  
- ❗ *Activation fails* → Try:  
  - Windows: `.\bot-env\Scripts\activate`  
  - Linux: `source ./bot-env/bin/activate`  

---

### **2.3 Installing Required Libraries**  
Run this in your **activated environment**:  
```bash
pip install telethon psutil
```
**Troubleshooting:**  
- ❗ *"pip not found"* → Reinstall Python with "Add to PATH" enabled.  
- ❗ *Permission errors (Linux)* → Use `pip install --user` or `sudo pip install` (not recommended, use a virtual env instead).  

---

### **2.4 Configuring the Bot**  
#### **Step 1: Get Telegram API Credentials**  
1. Go to [https://my.telegram.org/auth](https://my.telegram.org/auth)  
2. Log in with your **phone number** (the one you’ll use for the bot).  
3. Go to **"API Development Tools"**.  
4. Fill in **App title** (any name) and **Short name** (e.g., `MyForwardBot`).  
5. **Copy `api_id` and `api_hash`** (you’ll paste them into `main.py`).  

#### **Step 2: Edit `main.py`**  
Open the file in **Notepad (Windows)** or **nano (Linux)**:  
```bash
nano main.py  # Linux
notepad main.py  # Windows
```
Find and edit these lines:  
```python
api_id = 12345  # Replace with your API ID (numbers only)
api_hash = 'your_api_hash_here'  # Replace with your API Hash (keep quotes)
CHENAL_BOT = "@YourControlChannel"  # Replace with your Telegram channel (e.g., "@MyBotControl")
```
**Save the file!**  

**Troubleshooting:**  
- ❗ *Bot won’t start* → Ensure no typos in `api_id` and `api_hash`.  
- ❗ *"Invalid API ID"* → Generate new credentials at [my.telegram.org](https://my.telegram.org/).  

---

### **2.5 First Run & Authentication**  
Run the bot:  
```bash
python main.py  # Windows
python3 main.py  # Linux
```
**Follow these steps:**  
1. Enter your **phone number** (with country code, e.g., `+1234567890`).  
2. If you have **2FA**, enter your password.  
3. You’ll get a **login code** in Telegram → enter it in the terminal.  

**Expected Success:**  
- You’ll see `Logged in as [Your Bot Name]`.  
- A file `anon.session` will be created (do not delete it!).  

**Troubleshooting:**  
- ❗ *"FloodWaitError"* → Wait 24 hours or use a different account.  
- ❗ *No code received* → Check Telegram’s "Active Sessions" in Settings.  
- ❗ *"Invalid phone number"* → Include country code (e.g., `+1` for US).  

---

### **2.6 Setting Up Auto-Restart (rebooter.py)**  
#### **For Windows:**  
1. Open `rebooter.py` in Notepad.  
2. Change the last line to:  
   ```python
   monitor_script('main.py', 'main.py')  # No full path needed
   ```
3. Save and run:  
   ```cmd
   python rebooter.py
   ```

#### **For Linux:**  
1. Open `rebooter.py` in nano:  
   ```bash
   nano rebooter.py
   ```
2. Change the last line to:  
   ```python
   monitor_script('main.py', '/full/path/to/main.py')  # Replace with your actual path
   ```
3. Save (`Ctrl+O`, then `Enter`, then `Ctrl+X`).  
4. Run:  
   ```bash
   python3 rebooter.py
   ```

**Troubleshooting:**  
- ❗ *"File not found"* → Ensure the path is correct (use `pwd` in Linux to check).  
- ❗ *Script closes immediately* → Run in CMD (Windows) or `tmux` (Linux) to keep it alive.  

---

## **3. What to Do If Something Goes Wrong?**  
### **3.1 Bot Crashes or Freezes**  
✅ **Solution:** `rebooter.py` will restart it automatically.  
✅ **Manual Restart:**  
```bash
pkill -f "python main.py"  # Linux
taskkill /IM python.exe /F  # Windows
python3 main.py  # Restart
```

### **3.2 Bot Not Forwarding Messages**  
✅ **Check:**  
- Is the bot **added to both source and target channels** as admin?  
- Did you **configure rules** with `/from` or `/id`?  
- Are the rules **active** (not paused with `/stop`)?  

### **3.3 Session File Deleted or Corrupted**  
✅ **Fix:** Delete `anon.session` and restart the bot to re-authenticate.  

---

## **4. Final Checklist**  
Before declaring success, ensure:  
✔ `api_id` and `api_hash` are correctly set in `main.py`.  
✔ The bot is **logged in** (you see "Logged in as...").  
✔ `rebooter.py` is running in the background.  
✔ You’ve **tested commands** (`/help`, `/from`) in your control channel.  

---

## **5. Need More Help?**  
- **Windows Users:** Right-click → "Run as Administrator" if permissions fail.  
- **Linux Users:** Use `sudo` only if necessary (avoid for pip installs).  
- **Still stuck?** Check logs or ask in support forums with error messages.  

This guide minimizes guesswork—follow each step carefully, and your bot should run smoothly!
---

## 6. Configuration Deep-Dive

### Essential Files

1. **main.py**:
   - Lines 6-7: `api_id` and `api_hash` (from my.telegram.org)
   - Line 16: `CHENAL_BOT` - your control channel (@YourChannel)
   - Lines 14,309,861: Replace "@Channel name stub" with your dummy channel

2. **rebooter.py**:
   - Modify last line: `monitor_script('main.py', '/full/path/to/main.py')`
   - Windows: Change `python3` to `python` in `subprocess.Popen`

3. **State Files**:
   - `File_to_save_information_on_reboot.txt`: Forwarding rules
   - `save_coments.txt`: Rule comments
   - `File_to_sleap_trecing_proces.txt`: Paused rules
   - `variable_storage_file.txt`: Rule counter

### Initial Setup Example

```python
# In main.py
api_id = 12345678  # Your API ID from telegram.org
api_hash = 'your_api_hash_here'  # Your API Hash
CHENAL_BOT: str = "@YourControlChannel"  # Without quotes
```

## 7. Running as a Service

### Linux (systemd)

1. Create service file `/etc/systemd/system/telegram-bot.service`:
   ```ini
   [Unit]
   Description=Telegram Forwarding Bot
   After=network.target

   [Service]
   Type=simple
   User=root
   WorkingDirectory=/path/to/bot
   ExecStart=/opt/bot-env/bin/python /path/to/bot/main.py
   Restart=always
   Environment="PYTHONUNBUFFERED=1"

   [Install]
   WantedBy=multi-user.target
   ```

2. Enable and start:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable telegram-bot
   sudo systemctl start telegram-bot
   ```

### Windows (Task Scheduler)
1. Create task to run `main.py` at startup
2. Set action: `python.exe "C:\path\to\main.py"`
3. Configure to restart on failure

## 8. Command Reference

All commands are issued in your control channel:

|   Command   |            Example            |          Description        |
|-------------|-------------------------------|-----------------------------|
| `/help`     | `/help`                       | Show all commands           |
| `/from`     | `/from @Source to @Source`    | Create channel→channel rule |
| `/id`       | `/id 12345678 to @Target`     | Create user ID→channel rule |
| `/user`     | `/user @Username to @Target`  | Filter by username          |
| `/delete`   | `/delete 3`                   | Remove rule #3              |
| `/list`     | `/list`                       | List all rules              |
| `/pause`    | `/pause 5`                    | Pause rule #5               |
| `/resume`   | `/resume 5`                   | Resume rule #5              |
| `/off`      | `/off`                        | Pause all rules for 1 minute|

## 9. Security Best Practices

1. **API Credentials**:
   - Never commit `api_id`/`api_hash` to public repositories
   - Regenerate credentials if compromised

2. **Session Protection**:
   - Set permissions: `chmod 600 anon.session`
   - Consider `.gitignore` for session files

3. **Network Security**:
   - Use VPN for sensitive operations
   - Enable 2FA on your Telegram account

4. **Bot Account**:
   - Use dedicated Telegram account for the bot
   - Limit admin rights in channels

## 10. Maintenance & Upgrades

### Routine Checks
1. Verify state files weekly
2. Monitor disk space for log growth
3. Check for Python/package updates monthly

### Upgrade Procedure
1. Stop the bot
2. Backup state files
3. Update packages:
   ```bash
   pip install --upgrade telethon psutil
   ```
4. Test with `python3 main.py` before service restart

## 11. Troubleshooting

| Symptom | Solution |
|---------|----------|
| "No module named 'telethon'" | `pip install telethon` |
| Session not created | Delete `anon.session` and re-authenticate |
| Forwarding stops | Check `File_to_sleap_trecing_proces.txt` |
| High CPU usage | Verify no duplicate rebooter.py processes |
| API flood errors | Implement `@pausebot` then gradual restart |

## 12. FAQ

**Q: How to reset all rules?**
A: Overwrite state files with default content from Section 12 of original docs

**Q: Why aren't addresses being forwarded?**
A: Check rule status with `/show` and ensure:
- Rule is active (not paused)
- Source channel has proper permissions
- Address format matches (BTC, ETH, SOL)

**Q: How to change control channel?**
A: Update `CHENAL_BOT` in main.py and restart bot

## 13. Appendices

### A. Default State Files

**File_to_save_information_on_reboot.txt**:
```
{
  1: {'from': '@YourDummyChannel', 'to': '@YourDummyChannel'},
  ... # Repeat for 20 entries
}
```

**save_coments.txt**:
```
{
  1: {'coment': 'none'},
  ... # Repeat for 20 entries
}
```

### B. rebooter.py Customization

For Windows systems:
```python
# Change line 31 to:
subprocess.Popen(['python', script_path])

# Change monitor_script call to:
monitor_script('main.py', 'main.py')
```

### C. Performance Tuning

Add these to `main.py` for large channels:
```python
client = TelegramClient('anon', api_id, api_hash, flood_sleep_threshold=120, connection_retries=10)
```

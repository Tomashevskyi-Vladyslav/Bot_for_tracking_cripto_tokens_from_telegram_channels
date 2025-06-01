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
┌──────────────────────┐    ┌──────────────────────┐
│                      │    │                      │
│   Telegram Network   │◄──►│   Forwarding Bot     │
│                      │    │     (main.py)        │
└──────────────────────┘    └──────────┬──────────┘
                                       │
┌──────────────────────┐    ┌──────────▼──────────┐
│                      │    │                      │
│   Watchdog Service   │◄──►│   State Files       │
│     (rebooter.py)    │    │   (*.txt)           │
│                      │    │                      │
└──────────────────────┘    └──────────────────────┘
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

| Command | Example | Description |
|---------|---------|-------------|
| `/help` | `/help` | Show all commands |
| `/from` | `/from @Source @Target` | Create channel→channel rule |
| `/id` | `/id 12345678 @Target` | Create user ID→channel rule |
| `/user` | `/user @Username @Target` | Filter by username |
| `/delete` | `/delete 3` | Remove rule #3 |
| `/show` | `/show` | List all rules |
| `/stop` | `/stop 5` | Pause rule #5 |
| `/resume` | `/resume 5` | Resume rule #5 |
| `/pausebot` | `/pausebot` | Pause all rules for 1 minute |
| `/reboot` | `/reboot` | Graceful restart |

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
```json
{
  1: {'from': '@YourDummyChannel', 'to': '@YourDummyChannel'},
  ... # Repeat for 20 entries
}
```

**save_coments.txt**:
```json
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
client = TelegramClient('anon', api_id, api_hash,
                       flood_sleep_threshold=120,
                       connection_retries=10)
```

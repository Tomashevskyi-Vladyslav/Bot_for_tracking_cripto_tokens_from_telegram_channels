# Telegram Token Tracking Bot Documentation

## Overview

This Telegram bot monitors specific channels for cryptocurrency token deployment announcements and forwards relevant messages based on user-configured tracking lists. The bot supports tracking tokens from multiple sources with different message formats.

## Deployment Options

### Option 1: Direct Python Execution

**Requirements:**
- Python 3.7+
- Telethon library

**Steps:**
1. Install dependencies:
   ```bash
   pip install telethon
   ```

2. Create required files:
   ```bash
   echo "[]" > DB.txt
   echo "[]" > take_token_from_only.txt
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

### Option 2: PM2 Process Manager (for persistent execution)

1. First install PM2 globally:
   ```bash
   npm install pm2 -g
   ```

2. Start the bot with PM2:
   ```bash
   pm2 start main.py --name "telegram-token-bot" --interpreter python3
   ```

3. Useful PM2 commands:
   ```bash
   pm2 logs telegram-token-bot     # View logs
   pm2 restart telegram-token-bot  # Restart bot
   pm2 stop telegram-token-bot     # Stop bot
   ```

### Option 3: Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install telethon

# Create empty database files if they don't exist
RUN touch DB.txt take_token_from_only.txt && \
    echo "[]" > DB.txt && \
    echo "[]" > take_token_from_only.txt

CMD ["python", "main.py"]
```

**Build and Run:**
1. Build the image:
   ```bash
   docker build -t telegram-token-bot .
   ```

2. Run the container:
   ```bash
   docker run -d --name token-bot --restart unless-stopped -v ./data:/app telegram-token-bot
   ```

3. For Docker Compose (docker-compose.yml):
   ```yaml
   version: '3'
   services:
     token-bot:
       build: .
       container_name: telegram-token-bot
       restart: unless-stopped
       volumes:
         - ./data:/app
   ```

### Option 4: Systemd Service (Linux)

1. Create service file at `/etc/systemd/system/telegram-token-bot.service`:
   ```ini
   [Unit]
   Description=Telegram Token Tracking Bot
   After=network.target

   [Service]
   User=yourusername
   WorkingDirectory=/path/to/bot
   ExecStart=/usr/bin/python3 /path/to/bot/main.py
   Restart=always
   RestartSec=15

   [Install]
   WantedBy=multi-user.target
   ```

2. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable telegram-token-bot
   sudo systemctl start telegram-token-bot
   ```

## Persistence Notes

For all deployment methods except direct Python execution, ensure:
1. The `DB.txt` and `take_token_from_only.txt` files are preserved between restarts
2. For Docker, use volumes as shown in the example
3. For PM2/Systemd, ensure the working directory is correct and persistent

## Environment Variables (Recommended Enhancement)

For better security, consider modifying the code to use environment variables for sensitive data:

```python
import os
api_id = os.getenv('TELEGRAM_API_ID', '12345678')
api_hash = os.getenv('TELEGRAM_API_HASH', 'sindf341ljhdsa12')
```

Then run with:
```bash
TELEGRAM_API_ID=your_id TELEGRAM_API_HASH=your_hash python main.py
```

Or in Docker:
```bash
docker run -d -e TELEGRAM_API_ID=your_id -e TELEGRAM_API_HASH=your_hash ...
```

## Monitoring

For production deployments, consider adding:
- Log rotation (for PM2 or Systemd)
- Health checks (for Docker)
- Resource limits
- Regular backups of the data files

## Update Strategy

To update the bot:
1. For direct Python/PM2: Replace the file and restart
2. For Docker: Rebuild the image and redeploy
3. For Systemd: Replace file and `systemctl restart telegram-token-bot`

Remember to backup your `DB.txt` and `take_token_from_only.txt` files before updating!


---
### Important Notes for Deployment
Data Persistence:

For Docker deployments, ensure you mount volumes for the database files

The example above uses -v ./data:/app to persist data in a local data directory

Environment Variables:
For better security, consider modifying the code to use environment variables for:

API credentials (api_id and api_hash)

Target chat IDs

File paths

Logs Monitoring:

For Docker: docker logs telegram-token-bot -f

For systemd: journalctl -u telegram-token-bot -f

Resource Considerations:

The bot is lightweight but ensure your server has:

Stable internet connection

At least 512MB RAM

Basic CPU resources

Updates:

When updating the code, remember to:

For Docker: Rebuild the image and restart containers

For systemd: Restart the service (sudo systemctl restart telegram-token-bot)

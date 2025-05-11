import os
import requests
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Environment variables for secure access
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def send_telegram(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        logging.warning("Telegram token or chat ID not set in environment.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
        response.raise_for_status()
        logging.info("Telegram message sent successfully.")
    except requests.RequestException as e:
        logging.error(f"Telegram message failed: {e}")

def send_discord(message):
    if not DISCORD_WEBHOOK_URL:
        logging.warning("Discord webhook URL not set in environment.")
        return

    data = {"content": message}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data, headers=headers, timeout=5)
        response.raise_for_status()
        logging.info("Discord message sent successfully.")
    except requests.RequestException as e:
        logging.error(f"Discord message failed: {e}")

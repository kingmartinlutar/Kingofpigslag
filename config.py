# config.py
import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID", 0))
    API_HASH = os.getenv("API_HASH")
    ADMINS = [int(admin) for admin in os.getenv("ADMINS", "").split(",")]
    DB_URI = os.getenv("DB_URI")
    DB_NAME = os.getenv("DB_NAME", "vj_bot")
    ERROR_LOGS = os.getenv("ERROR_LOGS")  # Channel ID for error logs
    ERROR_MESSAGE = os.getenv("ERROR_MESSAGE", "false").lower() == "true"
    WEB_SERVER = os.getenv("WEB_SERVER", "true").lower() == "true"
    PORT = int(os.getenv("PORT", 8080))

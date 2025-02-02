# bot.py
import logging
from pyrogram import Client
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

class VJBot(Client):
    def __init__(self):
        super().__init__(
            "vj_bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=4,
            sleep_threshold=30,
            in_memory=True
        )

    async def start(self):
        await super().start()
        logging.info("Bot started successfully")
        if Config.WEB_SERVER:
            from web_server import keep_alive
            keep_alive()

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped successfully")

if __name__ == "__main__":
    VJBot().run()

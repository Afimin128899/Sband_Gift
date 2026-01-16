import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
FLYER_API_KEY = os.environ.get("FLYER_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

if not FLYER_API_KEY:
    raise RuntimeError("FLYER_API_KEY is not set")

import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Rotating daily, keep last 5 days
handler = TimedRotatingFileHandler(
    LOG_FILE,
    when="D",          # Rotate daily
    interval=1,
    backupCount=5,
    encoding="utf-8"
)

# Log format
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
handler.setFormatter(formatter)

# Root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

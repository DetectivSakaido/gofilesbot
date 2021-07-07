#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "gofilesbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1829039993:AAEe9z2IEdtel8NjbNnR3WY3gOXZbQJEo5s")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "6639731"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "09db81f3b9b8fcc63ce895630a32d171")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQChVBZP-Z_x5KJFpNlgY5sxjwU04JHXKVigTVpng5R2RjyhuD8bQkG4pYaM4Fdbk185ejJs-VvZz1lKzCe4P3EVYRrzC9vOE1Xm7wHaVKktUaZQ0kdtMW58H9SVJLOcbLauJH5uyUy_Dpb1ZgWUJciOdkdB7P9kp3Su1l3sR5gqk3_feZEDMRUhBHnA9fXXUS6oYilI_I5YTo4ZjwtMbKmjdcrGhlN2iNyLzdt0JRXrZFm0sgoI24a9Cd3CowBDTQ5EeTEKTsp4s1kokZoCj_Cqzd9teX6MxiDLzn8Ltt8WdfS8KkwQdPTjSlPSmN6KTXF8_WLadBDjfUB11Onp6WPdbQTveQE")

    # ID of Channels from which the bot should search files
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "-1001110968162").split())

    # Authorized users to perform delete messages in group
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "652415641 1499002873 1229514997 1760029936").split())

# ------------------------------------------ Optional Variables ------------------------------------------------------ #
    # Username of the group to tag in sending medias
    GROUP_U_NAME = os.environ.get("GROUP_U_NAME", "@animemusicstashgroup")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

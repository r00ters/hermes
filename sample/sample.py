import os
from hermes import telegram

telegram.send_message(
    os.environ['TOKEN'],
    os.environ['TELEGRAM_CHAT_ID'],
    "Hi, I'm Hermes, the herald of the gods! :)"
)

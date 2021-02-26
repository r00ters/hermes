import os
from hermes import telegram

telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

response = telegram.send_message(
    token=telegram_bot_token,
    chat_id=telegram_chat_id,
    text="Hi, I'm Hermes, the herald of the gods! :)"
)

print(response.json())

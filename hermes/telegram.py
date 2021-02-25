#!/usr/bin/env 
import requests

__all__ = ["send_message"]

def send_message(token, chat_id, text):
    telegram_url = "https://api.telegram.org/bot{}/sendMessage".format(token)

    payload = {
        "text": text.encode("utf8"),
        "chat_id": chat_id
    }

    try:
        requests.post(
            telegram_url,
            json = payload
        )

    except Exception as e:
        raise e

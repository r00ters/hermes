"""Telgram integration.

    * send_message - Send Telegram message to specified `chat_id

"""

import requests

__all__ = ["send_message"]

def send_message(token, chat_id, text):
    """Send Telegram message to specified `chat_id`.

    Parameters
    ----------
    token : str
        Your Telegram Bot Token
    chat_id : str
        Destination chat_id
    text:
        Message to send

    Raises
    ------
    Exception
        If an error occurred.

    Returns
    -------
    response
        requests.response
    """

    telegram_url = "https://api.telegram.org/bot{}/sendMessage".format(token)

    payload = {
        "text": text.encode("utf8"),
        "chat_id": chat_id
    }

    try:
        response = requests.post(
            telegram_url,
            data = payload
        )

        return response

    except Exception as e:
        raise e

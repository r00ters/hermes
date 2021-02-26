"""
Telgram integration.

    * send_message - Send Telegram message to specified `chat_id

"""

import requests

__all__ = ["send_message"]

def send_message(token, chat_id, text):
    """
    Send Telegram message to specified `chat_id`.

    ```
    # Arguments

    token (str): Your Telegram Bot Token.
    chat_id (str): Destination chat_id.
    text (str): Message to send.
    
    # Raises:
    Exception: If something bad happens.
    ValueError: If an invalid argument is specified.
    
    # Returns
    response (requests.Response): The response.
    ```
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

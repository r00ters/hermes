"""
Slack integration.

    * send_message - Send Slack message to specified `incoming webhook url`

"""

import requests
import re

__all__ = ["send_message"]

def send_message(incoming_webhook_url, text):
    """
    Send Slack message to specified `incoming webhook url`.

    ```
    # Arguments

    incoming_webhook_url (str): Your Slack Incoming Webhook URL.
    text (str): Message to send.
    
    # Raises:
    Exception: If something bad happens.
    ValueError: If incoming_webhook_url is invalid.

    # Returns
    response (requests.Response): The response.
    ```
    """

    if not re.match(r"^https:\/\/hooks\.slack\.com\/services\/T.*\/B.*\/.*", incoming_webhook_url):
        raise ValueError("Invalid Incoming Webhook URL")

    payload = {
        "text": text,
    }

    try:
        response = requests.post(
            incoming_webhook_url,
            json = payload
        )

        return response

    except Exception as e:
        raise e

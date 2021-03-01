<a name="hermes"></a>
# hermes

__Hermes - the herald of the gods__


    * PyPI name: hermes-herald
    * Package name: hermes

<a name="hermes.slack"></a>
# hermes.slack

Slack integration.

    * send_message - Send Slack message to specified `incoming webhook url`

<a name="hermes.slack.send_message"></a>
#### send\_message

```python
send_message(incoming_webhook_url, text)
```

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

<a name="hermes.telegram"></a>
# hermes.telegram

Telgram integration.

    * send_message - Send Telegram message to specified `chat_id`

<a name="hermes.telegram.send_message"></a>
#### send\_message

```python
send_message(token, chat_id, text)
```

Send Telegram message to specified `chat_id`.

```
# Arguments

token (str): Your Telegram Bot Token.
chat_id (str): Destination chat_id.
text (str): Message to send.

# Raises:
Exception: If something bad happens.

# Returns
response (requests.Response): The response.
```


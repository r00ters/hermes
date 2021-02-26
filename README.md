<a name="hermes"></a>
# hermes

__Hermes - the herald of the gods__


* PyPI name - hermes-herald
* Package name: hermes

<a name="hermes.telegram"></a>
# hermes.telegram

Telgram integration.

* send_message - Send Telegram message to specified `chat_id

<a name="hermes.telegram.send_message"></a>
#### send\_message

```python
send_message(token, chat_id, text)
```

Send Telegram message to specified `chat_id`.

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


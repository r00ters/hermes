import os
from hermes import slack

slack_incoming_webhook_url = os.environ['SLACK_INCOMING_WEBHOOK_URL']

response = slack.send_message(
    incoming_webhook_url=slack_incoming_webhook_url,
    text="Hi, I'm Hermes, the herald of the gods! :)"
)

print(response.text)

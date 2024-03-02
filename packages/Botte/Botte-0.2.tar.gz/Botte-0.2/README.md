# Botte
The most easiest telegram package that helps you to connect with the telegram api.

# Example How to send message

```
!pip install botte

```
```

from telegram_client import runbot

def message_handler(client, chat_id, text):
    client.send_message(chat_id, f"Echo: {text}")

token = 'YOUR_BOT_TOKEN'
runbot(token, message_handler)

```

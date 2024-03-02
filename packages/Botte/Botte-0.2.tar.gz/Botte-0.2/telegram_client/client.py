import requests

class TelegramClient:
    def __init__(self, token):
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.offset = None

    def listen_for_messages(self, handler):
        while True:
            updates = self.get_updates(self.offset)
            for update in updates.get('result', []):
                chat_id = update['message']['chat']['id']
                text = update['message'].get('text', '')
                handler(self, chat_id, text)
                self.offset = update['update_id'] + 1

    def send_message(self, chat_id, text):
        url = self.base_url + "sendMessage"
        data = {"chat_id": chat_id, "text": text}
        requests.post(url, data=data)

    def get_updates(self, offset=None):
        url = self.base_url + "getUpdates"
        params = {"offset": offset} if offset else {}
        response = requests.get(url, params=params)
        return response.json()

def runbot(token, message_handler):
    client = TelegramClient(token)
    client.listen_for_messages(message_handler)

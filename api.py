class MessengerAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def send_message(self, recipient_id, message):
        url = f"https://graph.facebook.com/v12.0/me/messages?access_token={self.access_token}"
        payload = {
            "recipient": {"id": recipient_id},
            "message": {"text": message}
        }
        response = requests.post(url, json=payload)
        return response.json()
# filepath: facebook-messenger/facebook-messenger/src/main.py

import sys
from messenger.api import MessengerAPI
from messenger.utils import authenticate_user

def main():
    # Authenticate user and get access token
    access_token = authenticate_user()
    if not access_token:
        print("Authentication failed. Exiting.")
        sys.exit(1)

    # Initialize Messenger API
    messenger = MessengerAPI(access_token)

    while True:
        recipient_id = input("Enter recipient ID (or 'exit' to quit): ")
        if recipient_id.lower() == 'exit':
            break
        message = input("Enter your message: ")
        response = messenger.send_message(recipient_id, message)
        print("Message sent:", response)

if __name__ == "__main__":
    main()
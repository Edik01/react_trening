# Facebook Messenger Project

This project is designed to send messages on Facebook using the Facebook Messenger API. It provides a simple interface for sending messages to users through the Messenger platform.

## Project Structure

```
facebook-messenger
├── src
│   ├── main.py          # Entry point of the application
│   ├── messenger
│   │   ├── __init__.py  # Initializes the messenger package
│   │   ├── api.py       # Contains MessengerAPI class for sending messages
│   │   └── utils.py     # Utility functions for authentication and token management
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd facebook-messenger
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Facebook App:
   - Create a Facebook App at the [Facebook Developer Portal](https://developers.facebook.com/).
   - Obtain your App ID and App Secret.
   - Set up Messenger and get the necessary permissions.

4. Configure your environment:
   - Create a `.env` file in the root directory and add your Facebook App credentials:
     ```
     APP_ID=<your_app_id>
     APP_SECRET=<your_app_secret>
     PAGE_ACCESS_TOKEN=<your_page_access_token>
     ```

## Usage

To send a message, run the main application:
```
python src/main.py
```

Follow the prompts to enter the recipient's ID and the message you wish to send.

## Notes

- Ensure that you have the necessary permissions to send messages to users.
- Refer to the [Facebook Messenger API documentation](https://developers.facebook.com/docs/messenger-platform/) for more details on message sending and API usage.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
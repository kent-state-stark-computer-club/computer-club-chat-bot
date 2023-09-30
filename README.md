# computer-club-chat-bot



This README provides a step-by-step guide to set up a Discord bot integrated with the OpenAI API.

## Prerequisites:

- Python installed on your machine.
- Basic knowledge of Python.

## Steps:

### 1. Install Necessary Libraries:

Install the required libraries using pip:

pip install discord.py openai

### 2. Create a New Discord Application:

- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Click on the "New Application" button in the top right.
- Give your application a name and click "Create".

### 3. Create a Bot User and Enable Message Content Intent:

- Inside your newly created application, navigate to the "Bot" tab on the left sidebar.
- Click on "Add Bot".
- Under the TOKEN section, click "Copy" to copy your bot token. **Keep this token private!** You will use it later to run your bot.
- Still in the "Bot" tab, under the "Privileged Gateway Intents" section, enable the "Message Content Intent". This will allow your bot to read the content of messages.

### 4. Invite Your Bot to a Server:

- Go to the "OAuth2" tab on the left sidebar in the Discord Developer Portal.
- Under "OAuth2 URL Generator", check the "bot" scope.
- Under "Bot Permissions", select the permissions your bot needs (e.g., Send Messages, Read Messages).
- Copy the generated URL, open it in a web browser, and choose a server to invite your bot to.

### 5. Obtain an OpenAI API Key:

- Sign up or log in to [OpenAI](https://www.openai.com/).
- Navigate to the API section.
- Follow the instructions to get your API key.
- **Keep this key private!** You'll use it to make requests to the OpenAI API.

### 6. Integration:

With your Discord bot token and OpenAI API key, you can now integrate both in your Python code. Always keep your keys private.


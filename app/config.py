import os
from dotenv import load_dotenv
load_dotenv()

TOKKEN = os.getenv('TOKKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
CHAT_ID = os.getenv('CHAT_ID')
ADMIN_IDS = os.getenv('ADMIN_IDS')
import os
from dotenv import load_dotenv
load_dotenv()


TOKKEN = os.getenv('TOKKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
CHAT_ID = os.getenv('CHAT_ID')
DB_LITE= os.getenv('DB_LITE')
ADMIN_IDS = [344919017, 5062940957]
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

user_id = os.getenv('USER_ID')
token = os.getenv('TOKEN')
url = os.getenv('URL')
tag = os.getenv('TAG')
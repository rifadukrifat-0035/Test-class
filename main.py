import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
database_url = os.getenv("database_url")
print(API_KEY)
print(database_url)

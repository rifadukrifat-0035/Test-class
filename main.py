import os
from dotenv import load_dotenv

# Load environment variables
API_KEY = os.getenv("API_KEY")

print(API_KEY)

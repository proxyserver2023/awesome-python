from dotenv import load_dotenv
load_dotenv()

import os
SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

print(SECRET_KEY, DATABASE_PASSWORD)
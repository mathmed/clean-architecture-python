import os
from src.main.config import app
from dotenv import load_dotenv

load_dotenv()

app.run(host="0.0.0.0", port=os.getenv("APP_PORT"))
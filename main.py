from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    secret_key = os.getenv("SECRET_KEY")
    return {"message": secret_key}
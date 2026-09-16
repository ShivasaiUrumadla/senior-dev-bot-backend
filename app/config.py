import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_APP_CLIENT_ID = os.getenv("GITHUB_APP_CLIENT_ID")
GITHUB_APP_PRIVATE_KEY = os.getenv("GITHUB_APP_PRIVATE_KEY")
GITHUB_PAT = os.getenv("GITHUB_PAT")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_SECRET_KEY=os.getenv("SUPABASE_SECRET_KEY")
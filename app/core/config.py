from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # DATABASE_URL = os.getenv("DATABASE_URL")
    DATABASE_URL = "postgresql://neondb_owner:npg_ScuH5RWaKxb2@ep-aged-term-apcp9kea.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require"

settings = Settings()
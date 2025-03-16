import os
from dotenv import load_dotenv
#from pydantic import BaseSettings
from pydantic_settings import BaseSettings


load_dotenv()

#class Settings:
    #DATABASE_URL = os.getenv("DATABASE_URL")
    #SECRET_KEY = os.getenv("SECRET_KEY")
    #ALGORITHM = "HS256"
    #ACCESS_TOKEN_EXPIRE_MINUTES = 30
class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    #DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY:str = os.getenv("SECRET_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNvcmVic3pnam13bHRxbnNvdGdtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIwNTI5NjUsImV4cCI6MjA1NzYyODk2NX0.i-WhI5nojGMKg2QGdDjSfwEAp2EeefZZGQWtCZYnUvE")
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()

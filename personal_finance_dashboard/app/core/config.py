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

settings = Settings()

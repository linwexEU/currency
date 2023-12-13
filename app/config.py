from pydantic_settings import BaseSettings 
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings): 

    APIKEY: str 
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class ConfigDict:
        env_file = ".env"


settings = Settings()
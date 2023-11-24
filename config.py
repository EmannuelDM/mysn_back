from typing import Optional
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    
    SECRET_KEY: Optional[str] = None
    ALGORITHM: Optional[str] = None
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[str] = None
    PGSQL_DATABASE: Optional[str] = None
    PGSQL_USER: Optional[str] = None
    PGSQL_PASSWORD: Optional[str] = None
    PGSQL_ENGINE: Optional[str] = None
    PGSQL_HOST: Optional[str] = None
    PGSQL_PORT: Optional[str] = None


    class Config:
        env_file = ".env"

    def get_database(self):
        return f""
    

global_settings = Settings()
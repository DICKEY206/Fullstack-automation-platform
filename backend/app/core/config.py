from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "automation_db"
    JWT_SECRET: str = "supersecretkey"
    JWT_ALGORITHM: str = "HS256"

settings = Settings()


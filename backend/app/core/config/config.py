from pydantic_settings import BaseSettings
import uuid
import os

class Setting(BaseSettings):
    DB_USERNAME: str = os.getenv("DB_USERNAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME:str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")

    POLICY_IDS: list[str] = os.getenv("POLICY_IDS")
    
    POLICY_NAMES: list[str] = os.getenv("POLICY_IDS")
    
    ALLOWED_RESOURCES: list[str] = os.getenv("ALLOWED_RESOURCES")

    SUPERADMIN_USER_ID: uuid.UUID = os.getenv("SUPERADMIN_USER_ID")
    SUPERADMIN_NAME: str = os.getenv("SUPERADMIN_NAME")
    SUPERADMIN_EMAIL: str = os.getenv("SUPERADMIN_EMAIL")
    SUPERADMIN_PASSWORD: str = os.getenv("SUPERADMIN_PASSWORD")


    SUBSCRIPTION_PLAN_IDS: list[str] = os.getenv("SUBSCRIPTION_PLAN_IDS")
    SUBSCRIPTION_PLAN_NAMES: list[str] = os.getenv("SUBSCRIPTION_PLAN_NAMES")
    SUBSCRIPTION_PLAN_COSTS: list[float] = os.getenv("SUBSCRIPTION_PLAN_COSTS")
    SUBSCRIPTION_PLAN_DETAILS: list[str] = os.getenv("SUBSCRIPTION_PLAN_DETAILS")

    PRIVATE_KEY_PATH: str = os.getenv("PRIVATE_KEY_PATH")
    ALGORITHM: str = os.getenv("ALGORITHM")

    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    REGION: str = os.getenv("REGION")
    SES_SENDER_MAIL: str = os.getenv("SES_SENDER_MAIL")

    
    @property
    def DB_URL(self):
        return os.getenv('DB_URL', f"postgresql+psycopg2://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    model_config = {
        'env_file' : ".env"
    }

settings = Setting()

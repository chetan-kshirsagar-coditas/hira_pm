from pydantic_settings import BaseSettings
import uuid


class Setting(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME:str
    DB_HOST: str
    DB_PORT: int

    POLICY_IDS: list[str]
    
    POLICY_NAMES: list[str]
    
    ALLOWED_RESOURCES: list[str]

    SUPERADMIN_USER_ID: uuid.UUID
    SUPERADMIN_NAME: str
    SUPERADMIN_EMAIL: str
    SUPERADMIN_PASSWORD: str


    SUBSCRIPTION_PLAN_IDS: list[str]
    SUBSCRIPTION_PLAN_NAMES: list[str]
    SUBSCRIPTION_PLAN_COSTS: list[float]
    SUBSCRIPTION_PLAN_DETAILS: list[str]

    PRIVATE_KEY_PATH: str
    ALGORITHM: str

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    REGION: str
    SES_SENDER_MAIL: str

    
    @property
    def DB_URL(self):
        return f"postgresql+psycopg2://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = {
        'env_file' : ".env"
    }

settings = Setting()
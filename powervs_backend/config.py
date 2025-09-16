from pydantic_settings import BaseSettings
from tortoise.contrib.fastapi import register_tortoise

class Settings(BaseSettings):
    DB_NAME: str = ""
    DB_USERNAME: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_PORT: str = ""
    SECRET_KEY: str = ""
    API_URL: str = ""
    REFRESH_SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


    class Config:
        env_file = ".env"

    @property
    def database(self):
        return f"mysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()

MODELS_LIST = ["users.models", "aerich.models",]

tortoise_config = {
    "connections": {"default": settings.database},
    "apps": {
        "models": {
            "models": MODELS_LIST,
            "default_connection": "default",
        },
    },
    "use_tz": True,  # If you want timezone-aware timestamps
    "timezone": "UTC",
}


def init_db(app) -> None:
    register_tortoise(
        app,
        config=tortoise_config,
        # db_url=Config.database_url,
        # modules={"models": ["app.models"]},
        generate_schemas=False,  # Use aerich for migrations
        add_exception_handlers=True,
    )

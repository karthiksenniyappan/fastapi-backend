from pydantic_settings import BaseSettings
from tortoise.contrib.fastapi import register_tortoise

class Settings(BaseSettings):
    db_uri:str = "mysql://root:Star1727!@127.0.0.1:3306/powervs"

settings = Settings()

MODELS_LIST = ["users.models", "aerich.models",]

tortoise_config = {
    "connections": {"default": settings.db_uri},
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

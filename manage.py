import argparse
import asyncio

from aerich import Command
from tortoise import Tortoise

from powervs_backend.config import tortoise_config


async def make_migrations():
    """Generate migration files."""
    aerich = Command(tortoise_config, app="models")
    await aerich.init()
    await aerich.migrate()
    print("MakeMigrations completed!")


async def migrate():
    """Apply migrations."""
    aerich = Command(tortoise_config, app="models")
    await aerich.init()
    result = await aerich.upgrade(run_in_transaction=True)

    for migration_files in result:
        print(migration_files)

    print("\nMigrations applied successfully!\n")

async def main():
    await Tortoise.init(config=tortoise_config)

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Manage database migrations.")
    parser.add_argument(
        "command",
        type=str,
        help="Command to run: makemigrations, migrate, downmigrate, initial_setup, create_plans",
        choices=["makemigrations", "migrate", "downmigrate", "initial_setup", "create_plans"],
    )
    args = parser.parse_args()

    if args.command == "makemigrations":
        await make_migrations()
    elif args.command == "migrate":
        await migrate()

    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())

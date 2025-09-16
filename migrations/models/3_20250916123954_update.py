from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` ADD `is_admin` BOOL NOT NULL DEFAULT 0;
        ALTER TABLE `user` ADD `is_active` BOOL NOT NULL DEFAULT 1;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP COLUMN `is_admin`;
        ALTER TABLE `user` DROP COLUMN `is_active`;"""

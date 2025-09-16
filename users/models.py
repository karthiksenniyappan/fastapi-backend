from tortoise import fields

from core.models import AbstractModel


class User(AbstractModel):
    first_name = fields.CharField(max_length=100, default="", blank=True)
    last_name = fields.CharField(max_length=100, default="", blank=True)
    email = fields.CharField(max_length=255, unique=True)
    phone_number = fields.CharField(max_length=255, unique=False, default=None, null=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    is_admin = fields.BooleanField(default=False)
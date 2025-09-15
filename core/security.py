from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_password_hash(password: str) -> str:
    """Generates a hashed password from the plain text password."""
    return password_context.hash(password)


def compare_password(password: str, _hash: str) -> bool:
    """Verifies a password against an existing hash."""
    return password_context.verify(secret=password, hash=_hash)

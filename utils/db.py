# --- Data Base -------------------------------------------
"""Database utilities for user management and authentication.

Handles SQLite database initialization, password hashing, credential verification,
and username existence checks with secure practices.
"""

import sqlite3
import hashlib
from pathlib import Path
from typing import Optional

DB_FILE = Path("users.db")

def init_db() -> None:
    """Initialize the SQLite database and create the users table if it doesn't exist."""
    if DB_FILE.exists():
        return  # Database already exists

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def hash_password(password: str) -> str:
    """Hash a password using SHA-256 and return the hexadecimal digest.

    Args:
        password: The password to hash.

    Returns:
        Hex string of the SHA256 hash.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def check_credentials(username: str, password: str) -> bool: # -> doesn't break anything btw
    """Verify if the provided username and password match a stored user.

    Args: 
        username: The username to check.
        password: The plain-text password to verify.

    Returns:
        True if credentials match, False otherwise.
    """ # args is aurguments 
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username.strip(),)
    )
    result = cursor.fetchone()
    conn.close()

    if result is None:
        return False

    stored_hash = result[0]
    return stored_hash == hash_password(password)


def user_exists(username: str) -> bool:
    """Check if a username already exists in the database.

    Args:
        username: The username to check.

    Returns:
        True if the username exists, False otherwise.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username.strip(),))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
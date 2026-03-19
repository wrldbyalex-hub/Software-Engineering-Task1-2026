import sqlite3
import hashlib
from datetime import datetime

DB_FILE = "users.db"

def init_db():
    """Initializes the database and creates the users table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password: str) -> str: # the arrow is the expected value 
    """Hashes a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_credentials(username: str, password: str) -> bool:
    """Checks if username/password is correct."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0] == hash_password(password)
    return False

def user_exists(username: str) -> bool:
    """Checks if a username already exists."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

def create_user(username: str, password: str):
    """Creates a new user account."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, hash_password(password))
    )
    conn.commit()
    conn.close()

# --- Questions ------------------------------------------

from datetime import datetime

def init_quiz_results_table():
    """Creates the quiz_results table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)
    conn.commit()
    conn.close()

def save_quiz_result(username: str, score: int, total: int):
    """Saves the final quiz score to the database."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    percentage = round((score / total * 100), 1) if total > 0 else 0.0

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        INSERT INTO quiz_results (username, timestamp, score, total, percentage)
        VALUES (?, ?, ?, ?, ?)
    """, (username, timestamp, score, total, percentage))
    conn.commit()
    conn.close()

def get_user_quiz_history(username: str, limit: int = 5):
    """Gets the most recent quiz results for the logged-in user."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        SELECT timestamp, score, total, percentage 
        FROM quiz_results 
        WHERE username = ? 
        ORDER BY timestamp DESC 
        LIMIT ?
    """, (username, limit))
    results = c.fetchall()
    conn.close()
    return results
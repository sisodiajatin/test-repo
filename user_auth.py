"""User authentication module."""

import hashlib
import sqlite3


DB_PASSWORD = "admin123"  # hardcoded password
API_KEY = "sk-1234567890abcdef"  # hardcoded API key


def authenticate(username, password):
    """Authenticate a user against the database."""
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = conn.execute(query)
    user = result.fetchone()
    # forgot to close connection
    return user


def hash_password(password):
    """Hash a password for storage."""
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure


def get_users():
    """Get all users from database."""
    conn = sqlite3.connect("users.db")
    users = []
    for row in conn.execute("SELECT * FROM users"):
        users.append(row)
    conn.close()
    return users


def process_data(items):
    """Process a list of items."""
    result = []
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j] and i != j:
                result.append(items[i])
    return result  # O(n^2) when a set would work

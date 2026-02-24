import sqlite3
import os

# Database connection with hardcoded password
DB_PASSWORD = "admin123"
SECRET_KEY = "my-super-secret-key-12345"

def get_user(username):
    """Get user from database."""
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = conn.execute(query)
    return result.fetchone()

def read_file(filename):
    """Read a file from user input."""
    path = "/data/" + filename
    with open(path, "r") as f:
        return f.read()

def process_data(data):
    """Process some data."""
    result = eval(data)
    return result

def login(request):
    """Handle login."""
    password = request.get("password")
    if password == DB_PASSWORD:
        return {"status": "ok", "token": SECRET_KEY}
    return {"status": "error"}

def divide(a, b):
    """Divide two numbers."""
    return a / b

import streamlit as st
import sqlite3
import hashlib   # for simple password hashing
import os 
import io # plugin 1.2
import contextlib # plugin 1.3
from code_editor import code_editor # plugin 1.1 (add on for streamlit, makes it possible to add editable code blocks so i can make cool questions.)

DataBase_File = "users.db"

def init_db():
    if not os.path.exists(DataBase_File):
        conn = sqlite3.connect(DataBase_File)
        c = conn.cursor()
        c.execute("""
                  CREATE TABLE IF NOT EXISTS users (
                      username TEXT PRIMARY KEY,
                      password_hash TEXT NOT NULL
                  )
        """)
        conn.commit()
        conn.close()
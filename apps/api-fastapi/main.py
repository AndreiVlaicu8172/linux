import os
import socket
import pymysql
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "webuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "webpass")
DB_NAME = os.getenv("DB_NAME", "webstack")


def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


@app.get("/user")
def get_user():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM settings WHERE id = 1;")
            row = cur.fetchone()
            name = row["name"] if row else "Unknown"
            return {"name": name}
    finally:
        conn.close()


@app.get("/id")
def get_id():
    return {"id": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "ok"}


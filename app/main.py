import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")


@app.get("/")
def read_root():
  try:
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    conn.close()
    return {"status": "success", "message": "Connected to database successfully!"}
  except Exception as e:
    return {"status": "error", "message": str(e)}


@app.get("/health")
def health():
  return {"status": "healthy"}
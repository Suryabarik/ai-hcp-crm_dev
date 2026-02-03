'''
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database file inside your project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "ai_hcp_crm.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"

# Create engine (this will create the file if it doesn't exist)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # required for FastAPI + SQLite
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

# Dependency for FastAPI routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
# database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./ai_hcp_crm.db"  # adjust path if needed

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for FastAPI routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
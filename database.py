import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Fetch the database URL from the environment, fallback to local SQLite
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./crm.db")

# Neon/Postgres requires slightly different engine arguments than SQLite
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

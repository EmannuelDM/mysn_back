from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import global_settings

DATABASE_URL = f"{global_settings.PGSQL_ENGINE}://{global_settings.PGSQL_USER}:{global_settings.PGSQL_PASSWORD}@{global_settings.PGSQL_HOST}:{global_settings.PGSQL_PORT}/{global_settings.PGSQL_DATABASE}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

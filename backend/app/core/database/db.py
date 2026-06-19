from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from app.core.config.config import settings

class Base(DeclarativeBase):
    pass

class Database:

    def __init__(self):
        self.engine = create_engine(url=settings.DB_URL)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

db_helper = Database()

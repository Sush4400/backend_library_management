from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.configs import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=True
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
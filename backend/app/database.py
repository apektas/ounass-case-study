import logging

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from app.config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD

# DATABASE_URL = f"postgresql://postgres:ounass@localhost/ounass"
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

logging.info(f"Database connection URL - {DATABASE_URL}")

# DATABASE_URL = f"sqlite:///./ounass.db"
engine = _sql.create_engine(DATABASE_URL, echo=True)
SessionLocal = _orm.sessionmaker(autoflush=False, bind=engine)
Base = _declarative.declarative_base()


# Dependency
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


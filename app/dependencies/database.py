"""Database dependencies for FastAPI routes."""
from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """Yield a database session to the caller."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

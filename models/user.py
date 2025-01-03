from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    """User model."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

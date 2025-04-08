from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "manju"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255), nullable=False)

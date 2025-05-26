from sqlalchemy import Column, Integer, String, Enum
from db.database import Base
import enum

class UserRole(enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole))

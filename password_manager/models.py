from sqlalchemy import Column, Integer, String
from database import Base   # imports base from database.py

class Password(Base):   # password class created
    __tablename__ = "passwords"     # gives tablename a name which is "passwords"

    id = Column(Integer, primary_key=True, index=True)
    website = Column(String, nullable=False)
    username = Column(String, nullable=False)
    encrypted_password = Column(String, nullable=False)


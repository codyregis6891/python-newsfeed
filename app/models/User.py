from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validates_email(self, key, email):
    #   make sure email address contains an @ character
    assert '@' in email

    return email

  @validates('password')
  def validates_password(self, key, password):
    # make sure password is at least 4 characters long
    assert len(password) > 4

    # encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)
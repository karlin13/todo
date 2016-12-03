from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    todo = Column(String(100), unique=False)
    is_complete = Column(Boolean)

    def __init__(self, todo=None, is_complete=None):
        self.todo = todo
        self.is_complete = is_complete
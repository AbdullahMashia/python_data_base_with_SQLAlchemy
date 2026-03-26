from sqlalchemy import create_engine,Column,String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///my_database.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=True)



Base.metadata.create_all(engine)
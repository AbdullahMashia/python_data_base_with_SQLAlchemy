from sqlalchemy import create_engine,Integer,String, DateTime,Boolean,select,insert,update,delete,func,ForeignKey
from sqlalchemy.orm import DeclarativeBase , mapped_column,relationship,sessionmaker



engine = create_engine('sqlite:///yeechatty.db')
Session = sessionmaker(bind=engine)
session = Session()


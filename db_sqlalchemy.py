from sqlalchemy import create_engine,Integer,String, DateTime,Boolean,select,insert,update,delete,func,ForeignKey
from sqlalchemy.orm import DeclarativeBase , mapped_column,relationship,sessionmaker


engine = create_engine('sqlite:///yeechatty.db')
Session = sessionmaker(bind=engine)
session = Session()



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key = True)
    username = mapped_column(String(50),nullable= False,unique=True)
    password = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100),nullable=False)
    country = mapped_column(String(30),nullable=False)
    age = mapped_column(Integer,nullable=False)
    created = mapped_column(DateTime,server_default = func.now,nullable=False)

    # relations


    r_reqMsg_receiver = relationship('Request_messaging',back_populates= 'r_receiver')
    r_reqMsg_sender = relationship('Request_messaging', back_populates = 'r_sender')
    r_Msgs = relationship('Messages', back_populates = 'r_User')

    r_CP = relationship('Conversations_participants',back_populates = 'r_User')


class Conversations(Base):
    __tablename__ = 'convs'
    id = mapped_column(Integer, primary_key = True)
    created_at = mapped_column(DateTime , server_default = func.now, nullable = False)
    enc_key = mapped_column(String(512),nullable=False)


    # relations

    r_CP  = relationship('Conversations_participants', back_populates = 'r_C')
    r_Msgs = relationship('Messages', back_populates = 'r_C')


class Conversations_participants(Base):
    __tablename__ = 'conv_mems'
    id = mapped_column(Integer, primary_key =True)
    conv_id = mapped_column(Integer , ForeignKey('convs.id'))
    user_id = mapped_column(Integer,ForeignKey('users.id'))


    # relations
    r_C = relationship('Conversations',back_populates = 'r_CP')

    r_User = relationship('User', back_populates ='r_CP')



class Request_messaging(Base):
    __tablename__ = 'req_msg'
    id = mapped_column(Integer, primary_key = True)
    sender_id = mapped_column(Integer, ForeignKey('users.id'))
    receiver_id = mapped_column(Integer,ForeignKey('users.id'))
    request_state = mapped_column(String(10),server_default = 'pending')
    created_at = mapped_column(DateTime, server_default = func.now)


    # relations:
    r_receiver = relationship('User',back_populates = 'r_reqMsg_receiver',foreign_keys = [receiver_id])
    r_sender = relationship('User', back_populates = 'r_reqMsg_sender', foreign_keys= [sender_id])



class Messages(Base):
    __tablename__ = 'msgs'
    id = mapped_column(Integer , primary_key=  True)
    conv_id = mapped_column(Integer, ForeignKey('convs.id'))
    sender_id = mapped_column(Integer, ForeignKey('users.id'))
    content = mapped_column(String(1024), nullable=False)
    sent_at = mapped_column(DateTime, server_default = func.now)
    type = mapped_column(String(10),server_default = 'text')


    #relations
    r_C = relationship('Conversations',back_populates= 'r_Msgs')
    r_User = relationship('User', back_populates = 'r_Msgs')





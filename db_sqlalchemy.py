<<<<<<< HEAD
from sqlalchemy import Integer, String, DateTime, ForeignKey, func,bollean
from sqlalchemy.orm import mapped_column, relationship
from my_database import Base


=======
from sqlalchemy import create_engine,Integer,String, DateTime,select,insert,update,delete,func,ForeignKey
from sqlalchemy.orm import DeclarativeBase , mapped_column,relationship,sessionmaker


engine = create_engine('sqlite:///yeechatty.db')
Session = sessionmaker(bind=engine)
session = Session()
>>>>>>> 07c99dc419e963ab2c2e2f76a89f5273bdc662d4




class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key = True)
    username = mapped_column(String(50),nullable= False,unique=True)
    password = mapped_column(String(100), nullable=False)
    publicName = mapped_column(String(50),nullable= False,unique= True)
    email = mapped_column(String(100),nullable=False)
    country = mapped_column(String(30),nullable=False)
    online_status = mapped_column(boolean, nullable = false , server_default= False)
    age = mapped_column(Integer,nullable=False)
    created = mapped_column(DateTime,server_default = func.now(),nullable=False)

    # relations


    r_reqMsg_receiver = relationship('Request_messaging',back_populates= 'r_receiver' ,foreign_keys= lambda:Request_messaging.receiver_id)
    r_reqMsg_sender = relationship('Request_messaging', back_populates = 'r_sender', foreign_keys = lambda: Request_messaging.sender_id)
    r_Msgs = relationship('Messages', back_populates = 'r_User')

    r_CP = relationship('Conversations_participants',back_populates = 'r_User')


class Conversations(Base):
    __tablename__ = 'convs'
    id = mapped_column(Integer, primary_key = True)
    created_at = mapped_column(DateTime , server_default = func.now(), nullable = False)
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
    created_at = mapped_column(DateTime, server_default = func.now())


    # relations:
    r_receiver = relationship('User',back_populates = 'r_reqMsg_receiver',foreign_keys = [receiver_id])
    r_sender = relationship('User', back_populates = 'r_reqMsg_sender', foreign_keys= [sender_id])



class Messages(Base):
    __tablename__ = 'msgs'
    id = mapped_column(Integer , primary_key=  True)
    conv_id = mapped_column(Integer, ForeignKey('convs.id'))
    sender_id = mapped_column(Integer, ForeignKey('users.id'))
    content = mapped_column(String(1024), nullable=False)
    sent_at = mapped_column(DateTime, server_default = func.now())
    type = mapped_column(String(10),server_default = 'text')


    #relations
    r_C = relationship('Conversations',back_populates= 'r_Msgs')
    r_User = relationship('User', back_populates = 'r_Msgs')






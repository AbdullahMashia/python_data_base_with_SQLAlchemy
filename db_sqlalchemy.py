from sqlalchemy import create_engine,Column,String, Integer,ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase,relationship

engine = create_engine('sqlite:///my_database.db')

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    message = relationship('Message',back_populates='user')


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key = True)
    content = Column(String(1024),nullable=False)
    user_id = Column(Integer , ForeignKey('user.id'))
    user = relationship('User',back_populates='message')



def add_user(user):
     user = User(name = user)
     session.add(user)
     session.commit()



def get_users():
    users = session.execute(select(User)).scalars().all()

    return users





def main():

    while True:
        print("Welcome to my db")
        print("1- add user\n2-show users 3- exit")
        choice = int(input("select a choice:"))

        match choice:
            case 1:
                user_name = input("Enter the user name: ")
                add_user(user_name)



            case 2:
                users = get_users()
                for user in users:
                    print(user)


            case 3:

                break



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()


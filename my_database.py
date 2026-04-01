from sqlalchemy import create_engine,Integer,String, DateTime,Boolean,select,insert,update,delete,func,ForeignKey, or_
from sqlalchemy.orm import DeclarativeBase , mapped_column,relationship,sessionmaker


engine = create_engine('sqlite:///yeechatty.db')
Session_local = sessionmaker(bind=engine)



class Base(DeclarativeBase):
    pass


# checking if email or username exist

def user_email_checker(user):

    with Session_local() as session:

        stmt = select(User).Where(or_(User.username == user["username"] , User.email == user["email"]))
        result = session.execute(stmt).scalars().all()


    return result



# adding new users
def addUser(user):
    user_email_check= {
        "username": user["username"],
        "email": user["email"]
    }




    result = user_email_checker(user_email_check)

    if result:

        if result[0]["user"] is not  None and result[0]["email"] is not None:

            return "user extists"


        if result[0]["email"] is not None:
            return 'email exitst'

        if result[0]["user"] is not None:
            return "both user and email extist"


        else:


            with  Session_local() as session:

                stmt = User(username = user["username"],password = user["password"])
                session.add(stmt)
                session.commit()


def authenticate_users(user):

    stmt = select(User).where(User.id == user["id"])

    with Session_local() as Session:
        result = Session.execute(stmt).scalars().one_or_none()

        if result is not None:
            if result.username == user["username"] and result.password == user["password"]:
                return "you are logged in"
            return "You username or password is incorrect"

        return "You data is wrong"



def find_user(user):
    stmt = select(User).where(User.name == user["publicName"])






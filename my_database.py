from sqlalchemy import create_engine,Integer,String, DateTime,Boolean,select,insert,update,delete,func,ForeignKey, or_
from sqlalchemy.orm import DeclarativeBase , mapped_column,relationship,sessionmaker

from flask import Flask, redirect, render_template,url_for

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

    with Session_local() as session:
        result = session.execute(stmt).scalars().one_or_none()

        if result is not None:
            return stmt

        return "user not found"




def user_profile(user_id):

    with Session_local() as session:
        result = session.get(User,user_id)

        if result is not None:
            return result
        return redirect ("/")





def online_users(user_id):

    with Session_local() as session:
        stmt =  select(User).where(User.online_status == True)

        results = session.execute(stmt).scalars().all()

        if results is not None:
            return results
        return "No online users"



def send_request(sender_id,rec_id):

    if sender_id != rec_id:
        with Session_local() as session:
            if not check_request(sender_id,rec_id):
                request = Request_messaging(sender_id = sender_id, receiver_id = rec_id )

                session.add(request)

                try:
                    session.commit()

                except:
                    return "request error"






def check_request(sender_id,rec_id):
    with Session_local() as session:
        stmt = select(request_messaging).where(or_(User.sender_id == sender_id, User.receiver_id ==rec_id),(User.sender_id == rec_id, User.receiver_id == sender_id))

        result = session.execute(stmt).scalars().one_or_none()

        if result is not None:
            return False

        return True



def requests_loader(user_id):

    with Session_local() as session:
        stmt = select(Request_messaging).where()






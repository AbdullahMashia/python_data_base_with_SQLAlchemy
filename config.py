import os
from dotenv import load_dotenv


class Config_db:

    root = os.path.dirname(os.path.dirname(__file__))
    db_url = os.path.join(root,"yeechatty.db")

    secret_key = os.getenv("SECRET_KEY","MY_KEY")



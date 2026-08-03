from SRC import create_app

app = create_app()


CONNECTION:
from dotenv import load_dotenv
import os 

from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('URL_DATABASE')

    #Desabilita o rastreio de modificações dos objetos
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
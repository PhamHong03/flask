# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


# mysql = MySQL()

db = SQLAlchemy()
db_session = db.session
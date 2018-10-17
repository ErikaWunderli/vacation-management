from flask import Flask
from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

DBUSER = 'postgres'
DBPASS = 'postgres'
DBHOST = 'postgres'
DBPORT = '5432'
DBNAME = 'postgres'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'foobarbaz'


db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255), unique=False)
    status = db.Column(db.String(15), unique=False)
    role = db.Column(db.String(15), unique=False)
    db.relationship('Request', backref='employee', lazy=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    status = db.Column(db.String(15), unique=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)


class CreateDB(object):
    def __init__(self, hostname=None):
        if hostname is not None:
            HOSTNAME = hostname
        import sqlalchemy
        engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
        engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE))
        db.create_all()


if __name__ == '__main__':
    manager.run()

from apka import db, mml
from flask_login import UserMixin


class Message(db.Model):
    id = db.Column('id', db.Integer(), primary_key=True)
    author = db.Column(db.String(20))
    msg = db.Column(db.String(400))
    seen = db.Column(db.Text(), default='{"username": []}')
    roomname = db.Column(db.String(4), db.ForeignKey('room.name'))

    def __init__(self, author, msg, roomname):
        self.author = author
        self.msg = msg
        self.roomname = roomname

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Room(db.Model):
    name = db.Column(db.String(4), primary_key=True ,nullable=False)
    messages = db.relationship('Message', backref='room')


class MessageSchema(mml.Schema):
  class Meta:
    fields = ('id', 'author', 'msg', 'seen')
from flask import Flask, request, jsonify, render_template
from apka import app, db, mml
from apka.models import Message, Room
from apka.schemas import Message_schema, Messages_schema
import json
from flask_cors import cross_origin
# for room generator
import string
import random

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")


"-----------------------API-----------------------------"

#Create a Message
@app.route('/message', methods=['POST'])
def add_Message():
    author = request.json['author']
    msg = request.json['msg']
    roomname = request.json['roomname']

    new_Message = Message(author, msg, roomname)

    db.session.add(new_Message)
    db.session.commit()

    return Message_schema.jsonify(new_Message)

# Get All Messages
@app.route('/message/<room>/all/<asker>', methods=['GET'])
def get_Messages(room, asker):
    all_Messages = Message.query.filter_by(roomname=room).all()
    for item in all_Messages:
        python_dict = json.loads(item.seen)
        lista_userow = python_dict['username']
        if asker not in lista_userow:
            python_dict['username'].append(asker)
        json_gotowy = json.dumps(python_dict)
        item.seen = json_gotowy
        db.session.commit()
    result = Messages_schema.dump(all_Messages)
    return jsonify(result)

    # Get All Messages by one author
@app.route('/message/<room>/byauthor/<author>/<asker>', methods=['GET'])
def get_MessagesByauthor(room, author, asker):

    all_Messages = Message.query.filter_by(roomname=room,author=author).all()
    for item in all_Messages:
        python_dict = json.loads(item.seen)
        lista_userow = python_dict['username']
        if asker not in lista_userow:
            python_dict['username'].append(asker)
        json_gotowy = json.dumps(python_dict)
        item.seen = json_gotowy
        db.session.commit()

    result = Messages_schema.dump(all_Messages)

    # for item in all_Messages:
    #     item.seen.append(asker)
    #     db.session.commit()

    return jsonify(result)

# GET msg by ID
@app.route('/message/byid/<id>/<asker>', methods=['GET'])
def get_Message(id, asker):
    message = Message.query.get(id)
    python_dict = json.loads(message.seen)
    lista_userow = python_dict['username']
    print(lista_userow)
    if asker not in lista_userow:
        python_dict['username'].append(asker)
    json_gotowy = json.dumps(python_dict)
    message.seen = json_gotowy
    db.session.commit()
    return Message_schema.jsonify(message)


#Update a Message
@app.route('/message/<id>', methods=['PUT'])
def update_Message(id):
    message = Message.query.get(id)
    msg = request.json['msg']
    message.msg = msg
    db.session.commit()
    return Message_schema.jsonify(Message)

# Delete a Message
@app.route('/message/<id>', methods=['DELETE'])
def delete_Message(id):
    message = Message.query.get(id)
    db.session.delete(message)
    db.session.commit()

    return Message_schema.jsonify(Message)

#generate room
@app.route('/room', methods=['POST'])
@cross_origin(origins="https://kamil-radzyminski.github.io")
def add_room():
    size = 4
    chars=string.ascii_lowercase + string.digits
    new_room_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
    new_Room = Room(name=new_room_name)

    db.session.add(new_Room)
    db.session.commit()
    response = {'roomname':new_room_name}

    return jsonify(**response)
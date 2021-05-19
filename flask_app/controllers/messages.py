from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/send', methods = ["POST"])
def create_message():
    if not Message.validate_message(request.form):
        return redirect ('/wall')
    data = {
        'content': request.form["content"],
        'user_id': request.form['user_id'],
        'user_id2': request.form['user_id2']
    }
    Message.create(data)
    return redirect('/wall')

@app.route('/delete/<id>')
def delete_message(id):
    data = {
        'id': id,
    }
    Message.delete(data)
    return redirect('/wall')


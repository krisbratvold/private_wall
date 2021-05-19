from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app import app       


class Message:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.user_id2 = data['user_id2']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO messages (content,user_id,user_id2) VALUES (%(content)s,%(user_id)s,%(user_id2)s);"
        user_id = connectToMySQL('wall_db').query_db(query,data)
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages;"
        results = connectToMySQL('wall_db').query_db(query)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages
    
    @classmethod
    def join(cls):
        query = "SELECT * FROM messages JOIN users ON messages.user_id2 = users.id"
        user_name = connectToMySQL('wall_db').query_db(query)
        return user_name

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL('wall_db').query_db(query,data)

    
    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(message['content']) == 0:
            flash('Message must contain more than 1 character')
            is_valid = False
        return is_valid
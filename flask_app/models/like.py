from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Like:
    db_name = "bright_ideas"

    def __init__(self,data):
        self.id = data['id']
        self.liked = data['liked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
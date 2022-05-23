from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Idea:
    db_name = "bright_ideas"

    def __init__(self,data):
        self.id = data['id']
        self.post = data['post']
        self.user_id = db_data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']





    @classmethod
    def save(cls,data):
        query = "INSERT INTO ideas (post, user_id) VALUES (%(post)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE ideas SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ideas WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)





    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ideas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ideas;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_ideas = []
        for row in results:
            all_ideas.append( cls(row) )
        return all_ideas




    @staticmethod
    def validate_idea(bright_ideas):
        is_valid = True
        if len(bright_ideas['post']) < 2:
            is_valid = False
            flash("Please type out a post","bright_ideas")
        return is_valid
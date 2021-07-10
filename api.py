from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data.db'
db = SQLAlchemy(app)

# Define a class for the Artist table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String)
    Password = db.Column(db.String)
    School = db.Column(db.String)
    Class = db.Column(db.String)
    Type = db.Column(db.String)
    Premium = db.Column(db.Boolean)

# Create the table
db.create_all()

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Create data abstraction layer
class UserSchema(Schema):
    class Meta:
        type_ = 'username'
        self_view = 'artist_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artist_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    
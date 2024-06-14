from app import db
from datetime import datetime

class Recipe(db.Model):
    __tablename__='recipes'
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(40))
    Description=db.Column(db.String(255))
    Category=db.Column(db.String(100))
    Time_long=db.Column(db.String(20))
    Ingridients=db.Column(db.Text())
    Pipeline=db.Column(db.Text())
    image=db.Column(db.String(40))

class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer(),primary_key=True)
    recipe=db.Column(db.Inteher(),db.ForeignKey('Recipe.id'))
    author=db.Column(db.String(20))
    Date=db.Column(db.DateTime(),default=datetime.ctime)
    Text=db.Column(db.Text())
import os
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectMultipleField
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from models import Recipe, db

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['IMAGES']=os.path.join(basedir,"images")
photos=UploadSet('image',IMAGES)
configure_uploads(app,photos)
patch_request_class(app)

class RecipeAdd(FlaskForm):
    name=StringField("Назва стравы: ", validators=[DataRequired()])
    Description=StringField("Апісанне стравы: ",validators=[DataRequired()])
    Category=StringField("Катэгорыя стравы: ", validators=[DataRequired()])
    Time=StringField("Час прыгатавання: ", validators=[DataRequired()])
    Ingridients=TextAreaField("Інгрыдыенты, кожны інгрыдыент з новага радку, колькасць інгрыдыентаў - праз  : ", validators=[DataRequired()])
    Pipeline=TextAreaField("Прыгатаванне, кожны этап з новага радку: ", validators=[DataRequired()])
    Image=FileField("Шлях да выявы стравы: ",validators=[FileAllowed()] )
    submit=SubmitField("Дадаць")

class RecipeEdit(FlaskForm):
    name=StringField("Назва стравы: ", validators=[DataRequired()])
    Description=StringField("Апісанне стравы: ",validators=[DataRequired()])
    Category=StringField("Катэгорыя стравы: ", validators=[DataRequired()])
    Time=StringField("Час прыгатавання: ", validators=[DataRequired()])
    Ingridients=TextAreaField("Інгрыдыенты, кожны інгрыдыент з новага радку: ", validators=[DataRequired()])
    Pipeline=TextAreaField("Прыгатаванне, кожны этап з новага радку: ", validators=[DataRequired()])
    Image=FileField("Шлях да выявы стравы: ",validators=[FileAllowed(photos,"Толькі выявы!")] )
    submit=SubmitField("Змяніць")

class CommentAdd(FlaskForm):
    name=StringField("Імя: ", validators=[DataRequired()])
    Comment=TextAreaField("Каментарый: ")
    submit=SubmitField("Дадаць")

class SearchForm(FlaskForm):
    name=StringField("Пошук па слову ў назве: ")
    Ingridients=StringField("Дадайце інгрыдыенты праз коску: ")
    Category=SelectMultipleField("Выбраць катэгорыю стравы: ", coerce=str)
    submit=SubmitField("Шукаць")

def category_list():
    form=SearchForm()
    category=set(db.session.query(Recipe.Category).all())
    form.Category.choices=[category]
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectMultipleField
from flask_uploads import UploadSet,IMAGES
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from myapp.models import Recipe, db

images=UploadSet('images',IMAGES)

class RecipeAdd(FlaskForm):
    name=StringField("Назва стравы: ", validators=[DataRequired()])
    Description=StringField("Апісанне стравы: ",validators=[DataRequired()])
    Category=StringField("Катэгорыя стравы: ", validators=[DataRequired()])
    Time=StringField("Час прыгатавання: ", validators=[DataRequired()])
    Ingridients=TextAreaField("Інгрыдыенты, кожны інгрыдыент з новага радку, колькасць інгрыдыентаў - праз  : ", validators=[DataRequired()])
    Pipeline=TextAreaField("Прыгатаванне, кожны этап з новага радку: ", validators=[DataRequired()])
    Image=FileField("Шлях да выявы стравы: ",validators=[FileAllowed(images,"Толькі выявы!")] )
    submit=SubmitField("Дадаць")

class RecipeEdit(FlaskForm):
    name=StringField("Назва стравы: ", validators=[DataRequired()])
    Description=StringField("Апісанне стравы: ",validators=[DataRequired()])
    Category=StringField("Катэгорыя стравы: ", validators=[DataRequired()])
    Time=StringField("Час прыгатавання: ", validators=[DataRequired()])
    Ingridients=TextAreaField("Інгрыдыенты, кожны інгрыдыент з новага радку: ", validators=[DataRequired()])
    Pipeline=TextAreaField("Прыгатаванне, кожны этап з новага радку: ", validators=[DataRequired()])
    Image=FileField("Шлях да выявы стравы: ",validators=[FileAllowed(images,"Толькі выявы!")] )
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
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectMultipleField
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired
from myapp.models import Recipe, db
from myapp import images

class RecipeAdd(FlaskForm):
    name=StringField("Назва стравы: ", validators=[DataRequired()])
    Description=StringField("Апісанне стравы: ",validators=[DataRequired()])
    Category=StringField("Катэгорыя стравы: ", validators=[DataRequired()])
    Time_long=StringField("Час прыгатавання: ", validators=[DataRequired()])
    Ingridients=TextAreaField("Інгрыдыенты, кожны інгрыдыент з новага радку, колькасць інгрыдыентаў - праз прабел: ", validators=[DataRequired()])
    Pipeline=TextAreaField("Прыгатаванне, кожны этап з новага радку: ", validators=[DataRequired()])
    image=FileField("Шлях да выявы стравы: ",validators=[FileAllowed(images,"Толькі выявы!")] )
    submit=SubmitField("Дадаць")

class RecipeEdit(FlaskForm):
    name=StringField("Назва стравы: ", validators=[DataRequired()])
    Description=StringField("Апісанне стравы: ",validators=[DataRequired()])
    Category=StringField("Катэгорыя стравы: ", validators=[DataRequired()])
    Time_long=StringField("Час прыгатавання: ", validators=[DataRequired()])
    Ingridients=TextAreaField("Інгрыдыенты, кожны інгрыдыент з новага радку: ", validators=[DataRequired()])
    Pipeline=TextAreaField("Прыгатаванне, кожны этап з новага радку: ", validators=[DataRequired()])
    image=FileField("Шлях да выявы стравы: ",validators=[FileAllowed(images,"Толькі выявы!")] )
    submit=SubmitField("Змяніць")

class CommentAdd(FlaskForm):
    name=StringField("Імя: ", validators=[DataRequired()])
    Comment=TextAreaField("Каментарый: ")
    submit=SubmitField("Дадаць")

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget=CheckboxInput()

class SearchForm(FlaskForm):
    name=StringField("Пошук па слову ў назве: ")
    Ingridients=StringField("Дадайце інгрыдыенты праз коску: ")
    Category=MultiCheckboxField("Выбраць катэгорыю стравы: ")
    submit=SubmitField("Шукаць")
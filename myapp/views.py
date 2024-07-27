from myapp.models import Recipe, Post
from flask import render_template, redirect, url_for, flash, make_response, session, request
from myapp.models import Recipe, Post, db
from myapp.forms import RecipeAdd, RecipeEdit, CommentAdd, SearchForm
from werkzeug.utils import secure_filename
from myapp import app, basedir
from datetime import datetime
import os

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe=db.session.query(Recipe).get(recipe_id)
    posts=db.session.query(Post).filter(Post.recipe==recipe_id).all()
    form=CommentAdd()
    return render_template('recipe.html',recipe=recipe,posts=posts,form=form)
    

@app.route('/search',methods=['post','get'])
def search():
    form=SearchForm()
    category = [result.Category for result in db.session.query(Recipe.Category).distinct()]
    form.Category.choices=[(cat,cat) for cat in category]  
    if form.validate_on_submit():
        sub=db.session.query(Recipe).subquery()
        if form.name.data != "":
            print("name")
            sub=db.session.query(sub).filter(sub.c.name.ilike("%"+form.name.data+"%")).subquery()
        if form.Ingridients.data != "":
            print("ingridients")
            ingridients=form.Ingridients.data.split(", ")
            for ingr in ingridients:
                sub=db.session.query(sub).filter(sub.c.Ingridients.ilike("%"+ingr+"%")).subquery()
        if len(form.Category.data) != 0:
            print("category")
            sub=db.session.query(sub).filter(sub.c.Category.in_(form.Category.data)).subquery()
        result=db.session.query(sub).all()
        return render_template("result.html",result=result)
    return render_template("search.html",form=form)

@app.route('/add',methods=['post','get']) 
def add():
    form=RecipeAdd()
    if form.validate_on_submit():
        if 'image' in request.files:
            file=request.files['image']
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'],filename))
            path=filename
        else:
            path=None
        r=Recipe(name=form.name.data,Description=form.Description.data,Category=form.Category.data,Time_long=form.Time_long.data,Ingridients=form.Ingridients.data,Pipeline=form.Pipeline.data,image=path)
        db.session.add(r)
        db.session.commit()
        form=CommentAdd()
        return redirect(url_for('all')) 
    return render_template('add.html',form=form)
    
@app.route('/edit/<int:recipe_id>',methods=['post','get'])
def edit(recipe_id):
    recipe=db.session.query(Recipe).get(recipe_id)
    form=RecipeEdit(obj=recipe)
    if form.validate_on_submit():
        if 'image' in request.files:
            file=request.files['image']
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'],filename))
            path=filename
        else:
            path=None
        print(path)
        recipe.name=form.name.data
        recipe.Description=form.Description.data
        recipe.Category=form.Category.data
        recipe.Time_long=form.Time_long.data
        recipe.Ingridients=form.Ingridients.data
        recipe.Pipeline=form.Pipeline.data
        recipe.image=path
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('recipe',recipe_id=recipe_id))
    return render_template('edit.html',form=form,r=recipe)

@app.route('/recipe/<int:recipe_id>',methods=['post','get'])
def add_comment(recipe_id):
    form=CommentAdd()
    if form.validate_on_submit():
        p=Post(recipe=recipe_id,author=form.name.data,Text=form.Comment.data, Date=datetime.now())
        db.session.add(p)
        db.session.commit()
    return redirect(url_for('recipe',recipe_id=recipe_id))

@app.route('/all')
def all():
    result=db.session.query(Recipe.id,Recipe.name,Recipe.Category,Recipe.Time_long).all()
    return render_template("all.html",result=result)
    
@app.route('/delete/<int:recipe_id>',methods=['post',])
def delete(recipe_id):
    for_delete=db.session.query(Post).filter(Post.recipe==recipe_id).all()
    for i in for_delete:
        db.session.delete(i)
    for_delete=db.session.query(Recipe).get(recipe_id)
    if for_delete.image is not None:
        os.remove(os.path.join(basedir, "static",for_delete.image))
    db.session.delete(for_delete)
    db.session.commit()
    return redirect(url_for('all'))
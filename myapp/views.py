from myapp.models import Recipe, Post
from flask import render_template, redirect, url_for, flash, make_response, session
from myapp.models import Recipe, Post, db
from myapp.forms import RecipeAdd, RecipeEdit, CommentAdd, SearchForm
from myapp import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/recipe/<int:recipe_id>')
def recipe_info(recipe_id):
    recipe=db.session.query(Recipe).get(recipe_id)
    posts=db.session.query(Post).filter(Post.recipe==recipe_id).all()
    form=CommentAdd()
    return render_template('recipe.html',recipe,posts,form)
    

@app.route('/search',methods=['post','get'])
def search():
    form=SearchForm()  
    if form.validate_on_submit():
        sub=db.session.query(Recipe).subquery()
        if form.name.data is not None:
            sub=db.session.query(sub).filter(sub.c.name.ilike("%"+form.name.data+"%")).subquery()
        if form.Ingridients.data is not None:
            sub=db.session.query(sub).filter(sub.c.Ingridients.in_(form.Ingridients.data.split(", "))).subquery()
        if form.Category.data is not None:
            sub=db.session.query(sub).filter(sub.c.Category.in_(form.Category.data)).subquery()
        result=db.session.query(sub).all()
        return render_template("result.html",result)
    return render_template("search.html",form=form)
    
@app.route('/add',methods=['post','get']) 
def add():
    form=RecipeAdd()
    if form.validate_on_submit():
        r=Recipe(name=form.name.data,Description=form.Description.data,Category=form.Category.data,Time=form.Time.data,Ingridients=form.Ingridients.data,Pipeline=form.Pipeline.data,Image=form.Image.data)
        db.session.add(r)
        db.session.commit()
        form=CommentAdd()
        return render_template('recipe.html',recipe=r, posts=None, form=form)
    return render_template('add.html',form=form)
    
@app.route('/edit',methods=['post','get'])
def edit(recipe_id):
    form=RecipeEdit(obj=db.session.query(Recipe).get(recipe_id))
    if form.validate_on_submit():
        r=Recipe(name=form.name.data,Description=form.Description.data,Category=form.Category.data,Time=form.Time.data,Ingridients=form.Ingridients.data,Pipeline=form.Pipeline.data,Image=form.Image.data)
        db.session.add(r)
        db.session.commit()
        return redirect(url_for('/recipe/<int:recipe_id>'))
    return render_template('edit.html',form,recipe_id)

@app.route('/recipe/<int:recipe_id>',methods=['post','get'])
def add_comment(recipe_id):
    form=CommentAdd()
    if form.validate_on_submit():
        p=Post(recipe_id=recipe_id,author=form.name,Text=form.Comment)
        db.session.add(p)
        db.session.commit()
    return redirect(url_for('/recipe/<int:recipe_id>'))

@app.route('/all')
def all_recipes():
    result=db.session.query(Recipe.id,Recipe.name,Recipe.Category,Recipe.Time_long).all()
    return render_template("all.html",result)
    
@app.route('/del/<int:recipe_id>',methods=['post',])
def receipe_del(recipe_id):
    for_delete=db.session.query(Post).filter(Post.recipe==recipe_id).all()
    for i in for_delete:
        db.session.delete(i)
    for_delete=db.session.query(Recipe).get(recipe_id)
    db.session.commit()
    return redirect(url_for('all'))
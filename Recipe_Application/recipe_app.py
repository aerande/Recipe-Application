from flask import Flask, render_template, url_for, flash, redirect
from flask_bcrypt import Bcrypt
from form import RegistrationForm, LoginForm, RecipeForm, UpdateForm
from dbconnect import connect
from datetime import datetime
app = Flask(__name__)
app.secret_key = '31597cba443076b503e67dfcd417de6e'


@app.route("/")
def home():
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM recipes ORDER BY recipe_id desc"
        cursor.execute(sql)
        recipes = cursor.fetchall()

    finally:
        connection.close()

    return render_template('home.html', recipes=recipes, title='Home Page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    connection = connect()
    bcrypt = Bcrypt()
    if form.validate_on_submit():
        try:
            cursor = connection.cursor()
            username = form.username.data
            email = form.email.data
            password = form.password.data
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, email, hashed_password))
            connection.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))

        finally:
            connection.close()

    return render_template('register.html', title='Register Page', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    bcrypt = Bcrypt()
    connection = connect()
    if form.validate_on_submit():
        try:
            email = form.email.data
            cursor = connection.cursor()
            sql = "SELECT email, password FROM users WHERE email = (%s)"
            cursor.execute(sql, email)
            data = cursor.fetchone()
            if data is not None and email == data['email'] and bcrypt.check_password_hash(data['password'], form.password.data):
                flash('You have successfully logged in!', 'success')
                return redirect(url_for('home'))

            else:
                flash('Login unsuccessful! Please check email and password.', 'danger')

        finally:
            connection.close()

    return render_template('login.html', title='Login Page', form=form)


@app.route("/view/<rid>")
def view(rid):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM recipes WHERE recipe_id = (%s)"
        cursor.execute(sql, rid)
        recipes = cursor.fetchall()

    finally:
        connection.close()

    return render_template('view.html', title='View Page', recipes=recipes)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = RecipeForm()
    connection = connect()
    if form.validate_on_submit():
        try:
            cursor = connection.cursor()
            recipe_name = form.recipe_name.data
            ingredients = form.ingredients.data
            instructions = form.instructions.data
            serving_size = form.serving_size.data
            category = form.category.data
            notes = form.notes.data
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO recipes " \
                  "(recipe_name, ingredients, instructions, serving_size, category, notes, date_added) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (recipe_name, ingredients, instructions, serving_size, category, notes, formatted_date))
            connection.commit()
            flash('Your new recipe has been created!', 'success')
            return redirect(url_for('home'))

        finally:
            connection.close()

    return render_template('add.html', title='Add Recipe', form=form)


@app.route("/update/<rid>", methods=['GET', 'POST'])
def update(rid):
    form = UpdateForm()
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM recipes WHERE recipe_id = (%s)"
        cursor.execute(sql, rid)
        recipes = cursor.fetchall()

    finally:
        connection.close()

    connection = connect()
    if form.validate_on_submit():
        try:
            cursor = connection.cursor()
            recipe_name = form.recipe_name.data
            ingredients = form.ingredients.data
            instructions = form.instructions.data
            serving_size = form.serving_size.data
            category = form.category.data
            notes = form.notes.data
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            sql = "UPDATE recipes SET " \
                  "recipe_name = (%s), " \
                  "ingredients = (%s), " \
                  "instructions = (%s), " \
                  "serving_size = (%s), " \
                  "category = (%s), " \
                  "notes = (%s), " \
                  "date_modified = (%s) " \
                  "WHERE recipe_id = (%s)"
            cursor.execute(sql, (recipe_name, ingredients, instructions, serving_size, category, notes, formatted_date, rid))
            connection.commit()
            flash('Your new recipe is updated!', 'success')
            return redirect(url_for('home'))

        finally:
            connection.close()

    return render_template('update.html', title='Update Recipe', form=form, recipes=recipes)


@app.route("/delete/<rid>")
def delete(rid):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM recipes WHERE recipe_id = (%s)"
        cursor.execute(sql, rid)
        connection.commit()

    finally:
        connection.close()

    return redirect(url_for('home'))

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import TextArea


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    serving_size = StringField('Serving Size', validators=[DataRequired()])
    category = SelectField('Category', choices=[
                                                     ('Bread recipe', 'Bread recipe'),
                                                     ('Chicken recipe', 'Chicken recipe'),
                                                     ('Cookies recipe', 'Cookies recipe'),
                                                     ('Cake recipe', 'Cake recipe'),
                                                     ('Salad recipe', 'Salad recipe'),
                                                     ('Vegan recipe', 'Vegan recipe')
                                                 ])
    notes = TextAreaField('Notes', validators=[DataRequired()])
    submit = SubmitField('Add')


class UpdateForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    instructions = StringField('Instructions', validators=[DataRequired()])
    serving_size = StringField('Serving Size', validators=[DataRequired()])
    category = SelectField('Category', choices=[
                                                     ('Bread recipe', 'Bread recipe'),
                                                     ('Chicken recipe', 'Chicken recipe'),
                                                     ('Cookies recipe', 'Cookies recipe'),
                                                     ('Cake recipe', 'Cake recipe'),
                                                     ('Salad recipe', 'Salad recipe'),
                                                     ('Vegan recipe', 'Vegan recipe')
                                                 ])
    notes = StringField('Notes', validators=[DataRequired()])
    submit = SubmitField('Update')

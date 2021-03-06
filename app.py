
from flask import Flask, render_template, request
from markupsafe import escape
from formatting import unordered_list, ordered_list, wrap_in_tags
import google_api

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/recipes')
def recipes():
  all_recipes = google_api.get_all_recipes()
  return(ordered_list('recipes', all_recipes))


@app.route('/recipes/new')
def new_recipe():
  return render_template('recipe_input.html')


@app.route('/recipes/new', methods=['POST'])
def save_new_recipe():
  ingredients = request.form['ingredients']
  ingredients_list = ingredients.split("\n")
  formatted_ingredients = unordered_list("Ingredients", ingredients_list)
  
  instructions = request.form['instructions']
  instructions_list = instructions.split("\n")
  formatted_instructions = ordered_list("Instructions", instructions_list)

  recipe_name = request.form['recipe_name']
  
  return wrap_in_tags("h1", recipe_name) + formatted_ingredients + formatted_instructions


@app.route('/recipes/recipe/<recipes_name>/')
def capitalize(recipes_name):
    return '<h1>{}</h1>'.format(escape(recipes_name.capitalize()))



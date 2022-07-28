
from flask import Flask, render_template, request
from markupsafe import escape
from formatting import unordered_list, ordered_list, wrap_in_tags


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/recipies')
def recipies():
  return '<h1>Recipies</h1>'


@app.route('/recipies/new')
def new_recipie():
  return render_template('recipie_input.html')


@app.route('/recipies/new', methods=['POST'])
def save_new_recipie():
  ingredients = request.form['ingredients']
  ingredients_list = ingredients.split("\n")
  formatted_ingredients = unordered_list("Ingredients", ingredients_list)
  
  instructions = request.form['instructions']
  instructions_list = instructions.split("\n")
  formatted_instructions = ordered_list("Instructions", instructions_list)

  recipie_name = request.form['recipie_name']
  
  return wrap_in_tags("h1", recipie_name) + formatted_ingredients + formatted_instructions


@app.route('/recipies/recipie/<recipies_name>/')
def capitalize(recipies_name):
    return '<h1>{}</h1>'.format(escape(recipies_name.capitalize()))



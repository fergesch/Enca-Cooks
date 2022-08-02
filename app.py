
from flask import Flask, render_template, request
from markupsafe import escape
from formatting import unordered_list, ordered_list, wrap_in_tags
import google_api

app = Flask(__name__)


@app.route('/')
def hello():
    all_recipes = google_api.get_all_recipes()
    recipes_sorted = sorted(all_recipes, key=lambda d: d['name'])
    return render_template('recipes.html', recipes=recipes_sorted)


@app.route('/recipes')
def recipes():
    all_recipes = google_api.get_all_recipes()
    recipes_sorted = sorted(all_recipes, key=lambda d: d['name'])
    return render_template('recipes.html', recipes=recipes_sorted)


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


@app.route('/recipe/<recipe_name>/')
def capitalize(recipe_name):
    all_recipes = google_api.get_all_recipes()
    recipe = next(
        (item for item in all_recipes if item["name"] == recipe_name), None)
    recipe_dict = google_api.get_recipe(recipe['id'])
    return render_template('recipe.html', recipe_name=recipe_name, recipe_dict=recipe_dict)

import google_api
from google.cloud import firestore

if __name__ == '__main__':
    recipes = google_api.get_all_recipes()
    # for recipe in recipes:
    #     print(recipe)
    #     print(google_api.get_recipe(recipe['id']))
    #     print()
    print(google_api.get_recipe('1X9q70Z0pS8T2HkKzAFc9_NbNBStFXDVbRM9yRoY0BI8'))
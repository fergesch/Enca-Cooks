from flask import Flask, request
from flask_cors import CORS
from google.cloud import firestore

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return("<p>Hello, World!</p>")

@app.route('/params')
def Get_Query_Params():
    var1=request.args['var1']
    var2=request.args['var2']
    return(f'var1: {var1} and Father nmae is: {var2}')

@app.route('/allRecipes')
def all_recipes():
    db = firestore.Client(project='enca-cooks')
    docs = db.collection(u'recipes_test').select(["display_name", "ingredients"]).stream()
    doc_list = []
    for doc in docs:
        doc_id = doc.id
        doc_data = doc.to_dict()
        doc_list.append({'id': doc_id, 'name': doc_data["display_name"]})
    return(doc_list)

@app.route('/recipe/<id>')
def recipe(id):
    db = firestore.Client(project='enca-cooks')
    doc_ref = db.collection('recipes_test').document(id)
    doc = doc_ref.get()
    if doc.exists:
        doc_data = doc.to_dict()
        return(doc_data)
    else:
        print(u'No such document!')
        return('No Recipe')

if __name__ == "__main__":
    app.run(debug=True)
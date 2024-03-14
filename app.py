from pymongo import MongoClient
from flask import Flask, render_template, url_for, redirect, request
from bson.objectid import ObjectId       #for converting to object

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

@app.route("/", methods=['GET','POST'])
def index():
        if request.method == 'POST':
                content = request.form['content']   #name of input tag that prints the value 
                degree = request.form['degree']
                todos.insert_one({'content': content, 'degree':degree})
                return redirect(url_for('index'))
        all_todos = todos.find()

        return render_template('index.html', todos=all_todos)

@app.route("/<id>/delete/", methods=['POST'])
def delete(id):
    todos.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index.html'))

#mongodb database
db = client.flask_database
#collection
todos = db.todos


if __name__ == "__main__":
        app.run(debug=True)
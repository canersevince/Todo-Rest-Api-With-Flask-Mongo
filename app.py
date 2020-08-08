import os
import json
from flask import Flask, request
from dotenv import load_dotenv
from db import mongo

load_dotenv()

MONGO = os.getenv('MONGO')
SECRET = os.getenv('API_SECRET_KEY')

app = Flask('Api')
app.config.from_mapping(
    SECRET_KEY=os.environ.get('API_SECRET_KEY') or 'dev_key'
)


@app.route('/', methods=['GET'])
def index():
    return "TodoApi Works!"


@app.route('/create_user', methods=['POST'])
def post():
    ## expected data = user : {name, email, password, todo : []}
    parsed = json.loads(request.data)
    new_user = parsed
    new_user['todos'] = "[]"
    add = mongo('add', new_user)
    print(add)
    if add == "Exists":
        return "User Exists"
    return "Added"


@app.route('/add_todo', methods=['POST'])
def update():
    ## expected data = user, newTodo
    parsed = json.loads(request.data)
    user = parsed['user']
    add = mongo('add_todo', user)
    return add


if __name__ == '__main__':
    app.run(debug=True)

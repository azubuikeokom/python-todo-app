from flask import Flask
from flask import request
from flask import session
from flaskr import db
from flaskr import auth
from flaskr import schema

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.post('/add-task')
def addTask():
    #add task to database
    task=[]
    task.append(request.get_json()['task'])
    task=tuple(task)
    print("Inserted {}".format(task)) 
    db.insertTask(task)
    return request.get_json()

@app.post('/remove-task/id/<int:id>')
def removeTask():
    #remove task from database
    if request.body:
        auth.authSessionKey()


@app.post('/login')
def siginIn():
    auth.authUser()
    

@app.post('/signup')
def signUp():
    #add user credentials to DB
    credentials=[]
    credentials.append(request.get_json()['username'])
    credentials.append(request.get_json()['password'])
    credentials=tuple(credentials)
    print("Inserted {}".format(credentials)) 
    db.insertUser(credentials)
    return request.get_json()

if __name__ == '__main__':
    db.createDatabase()
    schema.create_schema()
    app.run()

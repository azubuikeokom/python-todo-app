import bcrypt
import secrets
from flaskr import db

def getPassword(username):
    user_password = db.getRecord(username)
    return user_password

def authUser(credemtials):
    username = credemtials.username
    password = credemtials.password
    #hash password
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    #compare hased password with data from the database
    if password_hash == getPassword(username):
        #authenticate user and return custom page
        createSessionKey()
        return 0
    else:
        # return authentication failure message
        return 1
def createSessionKey():
    return secrets.token_urlsafe(20)

def authSessionKey():
    #check if session key is still active
    db.getRecord()
    



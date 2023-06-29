from dotenv import load_dotenv
from mysql.connector import errorcode
import mysql.connector
import os


load_dotenv()

def connectDB(user=os.getenv('DB_USERNAME'),password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),database=os.getenv('DATABASE')):
    try:
        return mysql.connector.connect(user=user,password=password,host=host,database=database)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def createDatabase():
    cxn = mysql.connector.connect(user=os.getenv('DB_USERNAME'),password=os.getenv('DB_PASSWORD'))
    cursor = cxn.cursor()
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(os.getenv('DATABASE')))
        print("Database {} created".format(os.getenv('DATABASE')))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
    else:
        cursor.close()
        cxn.close()

def insertUser(data):
    add_user = (
    "INSERT INTO users"
    "(username,passwd)"
    "VALUES(%s,%s)"
    )
    cxn = connectDB()
    cursor = cxn.cursor()
    try:
        cursor.execute(add_user,data)
        cxn.commit()
    except mysql.connector.Error as err:
        print("Failed operation: {}".format(err))
    else:
        cursor.close()
        cxn.close()

def insertTask(data):
    add_task = (
    "INSERT INTO todos"
    "(author,task)"
    "VALUES(%s,%s)"
    )
    cxn = connectDB()
    cursor = cxn.cursor()
    try:
        cursor.execute(add_task,data)
        cxn.commit()
        print("SUCCESS!")
    except mysql.connector.Error as err:
        print("Failed operation: {}".format(err))
    else:
        cursor.close()
        cxn.close()

def deleteTask(data):
    delete_task=(
        ""
    )
    cxn=connectDB()

def createTables(table_schema):
    cxn=connectDB()
    cursor = cxn.cursor()
    try:
        cursor.execute(table_schema)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
        cursor.close()
        cxn.close()

def getAllTasks(user_data):
    records=[]
    all_tasks=(
        " SELECT task "
        " FROM todos "
        " WHERE author=%s "
    )
    cxn=connectDB()
    cursor = cxn.cursor() 
    try:
        cursor.execute(all_tasks,user_data)
        for row in cursor:
            records.append(row)
        print("SUCCESS")
    except mysql.connector.Error as err:
        print("Operation Failed: {}".format(err))   
    else:
        cursor.close()
        cxn.close()
        return records



 

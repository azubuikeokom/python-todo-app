from flaskr import db

tables = {}
tables['users'] = (
    "CREATE TABLE `users` ("
    " `id` int PRIMARY KEY AUTO_INCREMENT,"
    " `username` varchar(30) UNIQUE NOT NULL,"
    " `passwd` varchar(30) NOT NULL"
    ")"
)

tables['todos'] = (
    "CREATE TABLE `todos` ("
    " `id` int PRIMARY KEY AUTO_INCREMENT,"
    " `author` varchar(30) NOT NULL,"
    " `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " `task` TEXT NOT NULL"
    ")"
)

def create_schema():
  for table in tables:
    table_schema = tables[table]
    print("Creating table {}: ".format(table), end='')
    db.createTables(table_schema)



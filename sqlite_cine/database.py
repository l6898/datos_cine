import sqlite3

CREATE_OSCARS_TABLE = "CREATE TABLE IF NOT EXISTS oscars (nombre TEXT PRIMARY KEY, año INTEGER, director TEXT, género);"
INSERT_OSCARS = "INSERT INTO oscars(nombre, año, director, género)VALUES(?,?,?,?);"

GET_ALL_OSCARS = "SELECT * FROM oscars;"
GET_OSCARS_BY_NAME = "SELECT *FROM oscars WHERE name =?;"

GET_BEST_PREPARATION_FOR_OSCAR = """
SELECT * FROM oscars
WHERE nombre = ?
ORDER BY año DESC
LIMIT 1; """


def connect():
    return sqlite3.connect('peliculas.db')

def create_tables(connection):
    with connection:
        connection.execute(CREATE_OSCARS_TABLE)

def add_oscars(connection, nombre, año, director,genero ):
    with connection:
        connection.execute(INSERT_OSCARS, (nombre, año, director, genero))

def get_all_oscars(connection):
    with connection:
        return connection.execute(GET_ALL_OSCARS).fetchall()

def get_oscars_by_name(connection, nombre):
    with connection:
        return connection.execute(GET_OSCARS_BY_NAME, (nombre,)).fetchall()

def get_best_preparation_for_oscar(connection, nombre):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_OSCAR, (nombre,)).fetchone()
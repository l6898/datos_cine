from flask import Flask
import database

MENU_PROMPT = """--Pelis--
elige entre estas opciones:
1) agregar una nueva pelicula
2)ver todas las peliculas
3)encuentra la pelicula
4)mira cual es el mejor pelicula
5)salir
tu selección:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) !="5":
        if user_input =="1":
            nombre = input("escribe el nombre:")
            año= int( input("escribe el año:"))
            director = input("el director es:")
            genero = input("el género es:")

            database.add_oscars(connection, nombre, año, director, genero)

        elif user_input =="2":
           oscars = database.get_all_oscars(connection)

           for oscar in oscars:
               print(f"{oscar[0]}({oscar[2]}) -{oscar[1]}{oscar[3]} ") 

 

        elif user_input =="3":
            name = input('busca la pelicula:')
            oscars = database.get_oscars_by_name(connection, nombre) 

            for oscar in oscars:
                   print(f"{oscar[0]}({oscar[2]}) -{oscar[1]}{oscar[3]} ")


        elif user_input =="4":
            name= input("busca la pelicula:")
            best_method = database.get_best_preparation_for_oscar(connection, nombre,)


            print(f"the best movie for {name}is {best_method[2]}")
           
        else:
            print("invalid input, try again")
    
menu()












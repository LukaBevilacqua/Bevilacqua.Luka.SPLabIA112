from funciones import *

lista_peliculas = []
flag_lista = False

# Enunciado:
# Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato:
# id_peli, titulo, genero, rating
# por ejemplo: 1,Adventures of Rocky,sin genero,0
# 2,My Brother the Devil,sin genero,0
# 3,Criminal,sin genero,0
# Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar
# nuevos archivos de salida de formato similar filtrados por varios criterios:
# el programa contará con el siguiente menú:
# 1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de
# diccionarios los elementos
# del mismo.
# 2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
# 3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
# función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
# calculado de manera aleatoria se mostrará por pantalla el mismo.
# 4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
# función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
# 1: drama
# 2: comedia
# 3: acción
# 4: terror
# 5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero
# donde solo aparezcan películas del género seleccionado. El nombre del archivo será p.e.comedias.csv
# 6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
# género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
# 7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
# 8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
# 9) Salir.


while True:
    match menu():
        case "1":
            cargar_archivo("movies.csv", lista_peliculas)
            flag_lista = True
        case "2":
            if se_cargo(flag_lista):
                imprimir_lista(lista_peliculas)
        case "3":
            if se_cargo(flag_lista):
                mostrar_rating(mapear_rating(lista_peliculas))
        case "4":
            if se_cargo(flag_lista):
                mostrar_genero(mapear_genero(lista_peliculas))
        case "5":
            if se_cargo(flag_lista):
                guardar_archivo_csv("p.e.comedias.csv", filtrar_peliculas_genero(lista_peliculas, pedir_genero()))
        case "6":
            if se_cargo(flag_lista):
                ordenar_peliculas_genero_rating(lista_peliculas)
                imprimir_lista(lista_peliculas)
        case "7":
            if se_cargo(flag_lista):
                mostrar_mayor_rating(lista_peliculas)
        case "8":
            if se_cargo(flag_lista):
                guardar_archivo_json("movies.json", lista_peliculas)
        case "9":
            if confirmar("Esta seguro que desea salir? s/n: "):
                break
    pausar()




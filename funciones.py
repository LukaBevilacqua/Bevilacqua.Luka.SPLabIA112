def menu()-> str:
    """un menu diseñado para un parcial importante
    
    Returns:
        str: la opcion elegida
    """
    limpiar_pantalla()
    print("--------------------------------------------------------------------------------------------------")
    print(f"{'Desafio STARK':^50s}")
    print("1- cargar archivo .CSV")
    print("2- imprimir lista")
    print("3- asignar rating")
    print("4- asignar genero")
    print("5- filtrar por genero")
    print("6- ordenar peliculas")
    print("7- Informar mejor rating")
    print("8- guardar peliculas")
    print("9- salir")
    return input("ingrese opcion: ").lower().strip()

def confirmar(mensaje:str)-> bool:
    """confirma con un booleano

    Args:
        mensaje (str): pregunta que sera respondida por el usuario

    Returns:
        bool: True si la respuesta es si, False si es no
    """
    rta = input(mensaje).lower().strip()
    return rta == 's'


def pausar():
    """pausa el programa
    """
    import os
    os.system("pause")

def limpiar_pantalla():
    """limpia la pantalla
    """
    import os
    os.system("cls")

def get_path(nombre_archivo: str)-> str:
    """para conseguir el path de un archivo

    Args:
        nombre_archivo (str): nombre del archivo del cual queremos obtener su path

    Returns:
        str: el path del archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_archivo(nombre_archivo: str, lista: list)-> None:
    """carga un archivo en una lista

    Args:
        nombre_archivo (str): nombre del archivo donde esta lo que vamos a pasar a la lista
        lista (list): lista donde guardamos lo del archivo
    """
    with open(get_path(nombre_archivo), "r", encoding="utf-8") as file:
        encabezado = file.readline().strip("\n").split(",")
        for linea in file.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
            id, titulo, genero, rating = linea
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = int(rating)
            lista.append(pelicula)

def se_cargo(flag: bool)->bool:
    """pregunta si se cargo la lista

    Args:
        flag (bool): bandera de la lista

    Returns:
        bool: retorna True, y si es False muestra por consola un mensaje
    """
    return True if flag else print("Primero cargue la lista...")

def imprimir_lista(lista: list)->None:
    """muesta por consola las peliculas y sus datos

    Args:
        lista (list): lista diccionario donde estan las peliculas con sus datos
    """
    for pelicula in lista:
        print("------------------------------------------------------")
        print(pelicula["id"], end=" "), print(pelicula["titulo"], end=" "), print(pelicula["genero"], end=" "), print(pelicula["rating"])

def asignar_rating(lista: list)-> None:
    """asigna el rating de las peliculas

    Args:
        lista (list): lista donde estan las peliculas
    """
    from random import randint
    for pelicula in lista:
        pelicula["rating"] = float(randint(1, 10))

def mapear_rating(lista: list)-> list:
    """mapea el rating a las peliculas

    Args:
        lista (list): lista donde estan las peliculas

    Returns:
        list: lista mapeada con los ratings
    """
    lista_retorno = []
    asignar_rating(lista)
    for pelicula in lista:
        lista_retorno.append(pelicula["titulo"]), lista_retorno.append(pelicula["rating"])
    return lista_retorno

def mostrar_rating(lista: list)-> None:
    """muestra la pelicula con su rating

    Args:
        lista (list): lista donde se encuentra la pelicula y su rating
    """
    for pelicula in lista:
        print(pelicula)

def asignar_genero(lista):
    """asigna el genero de una pelicula

    Args:
        lista (_type_): lista donde se encuentran las peliculas
    """
    from random import randint
    for pelicula in lista:
        i = randint(1, 4)
        if i == 1:
            pelicula["genero"] = "drama"
        elif i == 2:
            pelicula["genero"] = "comedia"
        elif i == 3:
            pelicula["genero"] = "accion"
        else:
            pelicula["genero"] = "terror"

def mapear_genero(lista: list)-> list:
    """mapea el genero a las peliculas

    Args:
        lista (list): lista donde estan las peliculas

    Returns:
        list: lista mapeada con los generos
    """
    lista_retorno = []
    asignar_genero(lista)
    for pelicula in lista:
        lista_retorno.append(pelicula["titulo"]), lista_retorno.append(pelicula["genero"])
    return lista_retorno

def mostrar_genero(lista: list)-> None:
    """muestra la pelicula con su genero

    Args:
        lista (list): lista donde se encuentra la pelicula y su genero
    """
    for pelicula in lista:
        print(pelicula)

def filtrar_peliculas_genero(lista: list, genero: str)-> list:
    """filtra las peliculas por genero

    Args:
        lista (list): lista donde estan las peliculas
        genero (str): genero seleccionado para filtrar las peliculas

    Returns:
        list: lista filtrada por genero
    """
    lista_filtrada = []
    for el in lista:
        if el["genero"] == genero:
            lista_filtrada.append(el)
    return lista_filtrada

def pedir_genero()->str:
    """pide el genero de una pelicula

    Returns:
        str: el genero elegido
    """
    rta = input("Ingrese el genero de las peliculas que desearia filtrar (drama, comedia, accion, terror): ").lower().strip()
    while rta != "drama" and rta != "comedia" and rta != "accion" and rta != "terror":
        rta = input("ERROR, Ingrese el genero de las peliculas que desearia filtrar (drama, comedia, accion, terror): ").lower().strip()
    return rta

def guardar_archivo_csv(archivo: str, lista: list):
    """guarda un archivo .csv

    Args:
        archivo (str): el nombre del archivo donde queremos guardar las cosas
        lista (list): lista con las cosas que queremos guardar en el archivo
    """
    with open(get_path(archivo), "w", encoding="utf-8") as file:
        encabezado = ",".join(lista[0].keys()) + "\n"
        file.write(encabezado)
        for pelicula in lista:
            values = list(pelicula.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            file.write(linea)


def swap_lista(lista: list, i: int, j: int)->None:
    """hace swap para ordenar

    Args:
        lista (list): lista a la que queremos ordenar
        i (int): elemento i
        j (int): elemento j
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_peliculas_genero_rating(lista: list)->None:
    """ordena las peliculas por genero y tambien por el rating

    Args:
        lista (list): lista a la que queremos ordenar

    Raises:
        TypeError: no es una lista
    """
    if not isinstance(lista, list):
        raise TypeError("Eso no es una lista")
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i]["genero"] == lista[j]["genero"]:
                if lista[i]["rating"] < lista[j]["rating"]:
                    swap_lista(lista, i, j)
            elif lista[i]["genero"] > lista[j]["genero"]:
                swap_lista(lista, i, j)

def mostrar_mayor_rating(lista: list)->None:
    """muestra la pelicula con mayor rating

    Args:
        lista (list): lista donde estan las peliculas
    """
    flag = True
    mejor_rating = 0
    for pelicula in lista:
        if pelicula["rating"] > mejor_rating or flag:
            flag = False
            mejor_rating = pelicula["rating"]
            titulo_mejor_rating = pelicula["titulo"]
    print(titulo_mejor_rating, end=" "), print(mejor_rating)

def guardar_archivo_json(archivo: str, lista: list)->None:
    """guarda un archivo .json

    Args:
        archivo (str): nombre del archivo donde vamos a guardar las cosas
        lista (list): lista con las cosas que queremos guardar en el archivo
    """
    import json
    with open(get_path(archivo), "w", encoding="utf-8") as file:
        json.dump(lista, file, indent= 4)
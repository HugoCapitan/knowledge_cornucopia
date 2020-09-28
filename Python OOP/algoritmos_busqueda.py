import random
import time

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


def busqueda_binaria(lista, comienzo, final , objetivo):
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if objetivo == lista[medio]:
        return True
    elif objetivo > lista[medio]:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que número quieres encontrar? '))

    ## Búsqueda lineal
    # lista = [random.randint(0,100) for i in range(tamano_de_lista)]

    # encontrado = busqueda_lineal(lista, objetivo)
    
    ## Búsqueda binaria
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    # print (lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista.')




import random
import time

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j - 1]:
                # Notacion para hacer swapping
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0,1000) for i in range(tamano_de_lista)]

    print(lista)
    print('*' * 1000)

    time_before = time.time()
    sorted_chaos = ordenamiento_por_insercion(lista)
    time_after = time.time()
    
    print(sorted_chaos)
    print(f'Sorted finished in {time_after - time_before}')
    # print(sorted_chaos)
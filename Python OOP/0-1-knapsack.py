import random

def morral(available_space, weights, values, n):

    if n == 0 or available_space == 0:
        return 0
    
    current_index = n - 1

    if weights[current_index] > available_space:
        return morral(available_space, weights, values, n - 1)

    return max(
        values[current_index] + morral(available_space - weights[current_index], weights, values, n - 1),
        morral(available_space, weights, values, n - 1)
    )

    

if __name__ == '__main__': 
    length_of_lists = 10
    valores = [random.randint(500,1000) for i in range(length_of_lists)]
    pesos = [random.randint(0,60) for i in range(length_of_lists)]
    print(valores)
    print(pesos)
    tamano_morral = 60
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
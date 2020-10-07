# Programácion dinámica y estocástica

## Objetivos
* Aprender cuando utilizar programación dinámica y sus beneficios.
* Entender la diferencia entre programas deterministas y estocásticos.
* Aprender a utilizar programación estocástica.
* Aprender a crear simulaciones computacionales básicas.

# Programación dinámica
No hay que dejarse confundir por el nombre rimbombante, ya que este es simplemente un nombre de marketing que le dio su creador Richard Bellman para conseguir financiamiento y ofuscar el hecho de que esto son simplemente matemáticas.

### En que problemas se puede utilizar
* **Subestructura óptima**: Es decir que una solución global óptima se puede encontrar al combinar soluciones óptimas de subproblemas locales.
* **Problemas empalmados**: Una solución óptima que involucra resolver el mismo problema en varias ocaciones.

### Memoization:
Es una técnica qué consiste en guardar los cómputos realizados previamente en un resultado para poder consultarlo en lugar de repetir el cómputo. Un diccionario se puede consultar en O(1) (no importa el tamaño del diccionario, las consultas siempre toman lo mismo)

## Optimización de fibonacci
Un problema en el que podemos aplicar las técnicas de la programacion dinámica es en el de Fibonacci, en el que la formula es simplement: F _(n)_ = F _(n-1)_ + F _(n-2)_

La diferencia entre los tiempos de ejecución del fibonacci recursivo vs el fibonacci dinamico son dramaticas.

### Fibonacci Recursivo
```py
def fibonacci_recursivo(n):
    if n == 1 or n == 0: 
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
```

### Fibonacci Dinamico
```py
def fibonacci_dinamico(n, memo = {}):
    # print(f'Asked for {n}')
    if n == 1 or n == 0:
        return 1
    
    try:
        result = memo[n]
        # print(f'Found {n} saved')
        return result
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        # print(f'Calculated and saved {n}')
        
        return resultado
```

# Caminos aleatorios


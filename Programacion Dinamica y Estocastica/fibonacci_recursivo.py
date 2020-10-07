def fibonacci_recursivo(n):
    if n == 1 or n == 0: 
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

if __name__ == '__main__':
    n = int(input(f'Que fibonacci quieres calcular? '))
    result = fibonacci_recursivo(n)

    print(result)
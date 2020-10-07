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

if __name__ == '__main__':
    n = int(input(f'Que fibonacci quieres calcular? '))
    result = fibonacci_dinamico(n)

    print(result)
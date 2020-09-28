import random
import time

def merge_sort(list_a):
    if len(list_a) > 1:
        middle = len(list_a) // 2
        left = list_a[middle:]
        right = list_a[:middle]

        merge_sort(left)
        merge_sort(right)

        pos_a = 0
        pos_b = 0
        pos_c = 0

        while pos_a < len(left) and pos_b < len(right):
            if left[pos_a] < right[pos_b]:
                list_a[pos_c] = left[pos_a]
                pos_a += 1
            else:
                list_a[pos_c] = right[pos_b]
                pos_b += 1

            pos_c += 1

        while pos_a < len(left):
            list_a[pos_c] = left[pos_a]
            pos_a += 1
            pos_c += 1

        while pos_b < len(right):
            list_a[pos_c] = right[pos_b]
            pos_b += 1
            pos_c += 1

    return list_a


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0,1000) for i in range(tamano_de_lista)]

    time_before = time.time()
    sorted_chaos = merge_sort(lista)
    time_after = time.time()
    
    print(f'Sorted finished in {time_after - time_before}')
    # print(sorted_chaos)

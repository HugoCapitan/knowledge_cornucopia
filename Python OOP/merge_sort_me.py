import time
import random

def merge_sort(unsorted_list):
    # 1. Divide unsorted_list into sublists of 1 or 0 elements
    # 2. Compare elements of unsorted lists until everything is sorted
    # 3. Do again
    dived_lists = list_divider([unsorted_list])
    
    sorted_list = list_merger(dived_lists)

    return sorted_list


def list_merger(lists):
    n = len(lists)
    if n == 2:
        return two_lists_merger(lists[0], lists[1])

    results = []
    for i in range(0, n, 2):
        if i == n - 1:
            results.append(lists[i])
        else:
            results.append( two_lists_merger(lists[i], lists[i + 1]))

    # print(results)

    return list_merger(results)


def two_lists_merger(list_a, list_b):
    list_c = []

    len_a = len(list_a)
    len_b = len(list_b)
    pos_a = 0
    pos_b = 0

    while pos_a < len_a and pos_b < len_b:
        if list_a[pos_a] < list_b[pos_b]:
            list_c.append(list_a[pos_a])
            pos_a += 1
        elif list_b[pos_b] < list_a[pos_a]:
            list_c.append(list_b[pos_b])
            pos_b += 1
        else:
            list_c.append(list_a[pos_a])
            list_c.append(list_b[pos_b])
            pos_a += 1
            pos_b += 1

    while pos_a < len_a:
        list_c.append(list_a[pos_a])
        pos_a += 1

    while pos_b < len_b:
        list_c.append(list_b[pos_b])
        pos_b += 1

    return list_c


def list_divider(lists):
    n = len(lists)
    results = []
    larger_lists_remaining = False
    
    for i in range(n):
        list_to_divide = lists[i]
        ln = len(list_to_divide)
        if ln == 1:
            results.append(list_to_divide)
        if ln >= 2:
            middle = ln // 2
            larger_lists_remaining = True
            results.append(list_to_divide[0:middle])
            results.append(list_to_divide[middle:ln])
        
    if larger_lists_remaining:
        return list_divider(results)
    else:
        return results


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0,1000) for i in range(tamano_de_lista)]

    time_before = time.time()
    sorted_chaos = merge_sort(lista)
    time_after = time.time()
    
    print(f'Sorted finished in {time_after - time_before}')
    # print(sorted_chaos)
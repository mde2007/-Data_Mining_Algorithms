import time 
import random


def generate_massive():
    A = [random.randint(2000, 2500) for i in range(2000)]
    return A


def linear_search(A, num):
    for i, k in enumerate(A):
        if k == num:
            return i
    return "Число не найдено"


def interpolyation_search(A, num):
    low = 0
    high = len(A) - 1
    while low <= high and A[low] <= num <= A[high]:
        if A[high] == A[low]:
            return low if A[low] == num else "Число не найдено"
        pos = low + (num - A[low]) * (high - low) // (A[high] - A[low])
        if num == A[pos]:
            return pos
        if A[pos] < num:
            low = pos + 1
        else:
            high = pos - 1
    return "Число не найдено"

def jump_search(A, num):
    n = len(A)
    step = int(n ** 0.5)
    prev = 0        
    curr = step     

    while prev < n and A[min(curr, n) - 1] < num:
        prev = curr
        curr += step

    for i in range(prev, min(curr, n)):
        if A[i] == num:
            return i
        if A[i] > num:
            break

    return "Число не найдено"

num = int(input())
A = generate_massive()
A.sort()

# Линейный поиск
start = time.perf_counter()
ind = linear_search(A, num)
end = time.perf_counter()
print(f'Индекс нужного элемента: {ind}, найдено за {(end - start):.8f} cек при помощи линейного поиска')

# Интерполяционный поиск
start = time.perf_counter()
ind = interpolyation_search(A, num)
end = time.perf_counter()
print(f'Индекс нужного элемента: {ind}, найдено за {(end - start):.8f} cек при помощи интерполяционного поиска')

# Jump searcg
start = time.perf_counter()
ind = jump_search(A, num)
end = time.perf_counter()
print(f'Индекс нужного элемента: {ind}, найдено за {(end - start):.8f} cек при помощи Jump search')
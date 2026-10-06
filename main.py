import time
import random
import tkinter as tk


def generate_massive(lo, hi):
    A = [random.randint(lo, hi) for _ in range(2000)]
    # with open("input.txt", 'r') as f:
    #     data = f.read()
    # A = [int(x) for x in data.split()]
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, A)))
    return A


def linear_search(A, num):
    for i, k in enumerate(A):
        if k == num:
            return i
    return "Число не найдено"


def interpolation_search(A, num):
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


def sentinel_linear_search(A, num):
    n = len(A)
    last = A[-1]
    A[-1] = num
    i = 0
    while A[i] != num:
        i += 1
    A[-1] = last
    if i < n - 1 or last == num:
        return i
    return "Число не найдено"


def run_search():
    lo = int(entry_lo.get())
    hi = int(entry_hi.get())
    num = int(entry_num.get())

    A = generate_massive(lo, hi)
    A_sort = sorted(A)

    tests = [
        ("Линейный поиск: \n", linear_search, A),
        ("Интерполяционный поиск: \n", interpolation_search, A_sort),
        ("Jump search поиск: \n", jump_search, A_sort),
        ("Sentinel поиск: \n", sentinel_linear_search, A),
    ]

    text = ""
    for name, func, arr in tests:
        start = time.perf_counter()
        ind = func(arr, num)
        end = time.perf_counter()
        text += f"{name}Индекс: {ind}\nВремя поиска: {end - start:.8f} сек\n\n"
    result.config(text=text)


win = tk.Tk()
win.geometry("600x450")

tk.Label(win, text="Массив A из 2000 чисел. Введите диапазон:").place(x=20, y=5)

tk.Label(win, text="от").place(x=20, y=35)
entry_lo = tk.Entry(win)
entry_lo.place(x=45, y=35, width=80)

tk.Label(win, text="до").place(x=140, y=35)
entry_hi = tk.Entry(win)
entry_hi.place(x=165, y=35, width=80)

tk.Label(win, text="Какое число ищем:").place(x=20, y=70)
entry_num = tk.Entry(win)
entry_num.place(x=150, y=70, width=80)

button = tk.Button(win, text="Найти", command=run_search)
button.place(x=250, y=66)

result = tk.Label(win, text="", justify="left")
result.place(x=20, y=110)

win.mainloop()
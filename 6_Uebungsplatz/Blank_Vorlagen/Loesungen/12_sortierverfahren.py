"""
LÖSUNG 12: Alle Sortierverfahren
(bei Merge/Heap ist die Hilfsfunktion vorgegeben, der Rest ist SELBST)
"""


def bubble_sort(numbers):                    # 🟨 SELBST
    n = len(numbers)
    for i in range(n - 1):
        list_sorted = True
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                list_sorted = False
        if list_sorted:
            return


def selection_sort(numbers):                 # 🟨 SELBST
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


def insertion_sort(numbers):                 # 🟨 SELBST
    for i in range(1, len(numbers)):
        pivot = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > pivot:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = pivot


def quicksort(numbers):                      # 🟨 SELBST
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    kleiner = [x for x in numbers[1:] if x <= pivot]
    groesser = [x for x in numbers[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)


def mergesort(numbers):                      # 🟨 SELBST (nur diese Funktion)
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    links = mergesort(numbers[:mid])
    rechts = mergesort(numbers[mid:])
    return merge(links, rechts)


def merge(left, right):                      # 🟩 vorgegeben
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heap_sort(arr):                          # 🟨 SELBST (nur diese Funktion)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):                      # 🟩 vorgegeben
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


probe = [55, 7, 78, 12, 42, 3]
print("quicksort:", quicksort(probe[:]))
print("mergesort:", mergesort(probe[:]))
a = probe[:]; bubble_sort(a); print("bubble:   ", a)
a = probe[:]; selection_sort(a); print("selection:", a)
a = probe[:]; insertion_sort(a); print("insertion:", a)
a = probe[:]; heap_sort(a); print("heap:     ", a)

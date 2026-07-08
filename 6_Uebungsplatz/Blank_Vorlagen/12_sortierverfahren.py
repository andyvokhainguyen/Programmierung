"""
Übung 12: Alle Sortierverfahren

Bei Merge und Heap ist die Hilfsfunktion (merge / heapify) vorgegeben -
du schreibst nur die Hauptfunktion. Bei den anderen den ganzen Algorithmus.
"""


def bubble_sort(numbers):
    # ✍️ SELBST: Nachbarn tauschen, wenn numbers[j] > numbers[j+1]
    #   äußere for i in range(n-1), innere for j in range(0, n-i-1), Flag zum Früh-Abbruch
    pass


def selection_sort(numbers):
    # ✍️ SELBST: Minimum im unsortierten Rest suchen (min_index), dann tauschen
    pass


def insertion_sort(numbers):
    # ✍️ SELBST: pivot = numbers[i]; größere nach rechts schieben; pivot einsetzen
    pass


def quicksort(numbers):
    # ✍️ SELBST:
    #   Basisfall len <= 1 -> return numbers
    #   pivot = numbers[0]
    #   kleiner = [x for x in numbers[1:] if x <= pivot]
    #   groesser = [x for x in numbers[1:] if x > pivot]
    #   return quicksort(kleiner) + [pivot] + quicksort(groesser)
    pass


def mergesort(numbers):
    # ✍️ SELBST: nur diese Funktion!
    #   Basisfall len <= 1 -> return numbers
    #   mid = len//2; links = mergesort(numbers[:mid]); rechts = mergesort(numbers[mid:])
    #   return merge(links, rechts)
    pass


def merge(left, right):                      # 🟩 KOMPLETT vorgegeben
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


def heap_sort(arr):
    # ✍️ SELBST: nur diese Funktion!
    #   n = len(arr)
    #   1) for i in range(n//2 - 1, -1, -1): heapify(arr, n, i)
    #   2) for i in range(n-1, 0, -1): arr[i],arr[0]=arr[0],arr[i]; heapify(arr, i, 0)
    pass


def heapify(arr, n, i):                      # 🟩 KOMPLETT vorgegeben
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


# Testaufrufe (erwartet jeweils: [3, 7, 12, 42, 55, 78])
probe = [55, 7, 78, 12, 42, 3]
print("quicksort:", quicksort(probe[:]))
print("mergesort:", mergesort(probe[:]))
a = probe[:]; bubble_sort(a); print("bubble:   ", a)
a = probe[:]; selection_sort(a); print("selection:", a)
a = probe[:]; insertion_sort(a); print("insertion:", a)
a = probe[:]; heap_sort(a); print("heap:     ", a)

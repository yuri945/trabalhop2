"""
Quick Sort
Vantagens:
- Muito eficiente na prática (O(n log n)).
Desvantagens:
- Pior caso O(n²) se o pivô for mal escolhido.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Exemplo de uso
print(quick_sort([10, 7, 8, 9, 1, 5]))

"""
Selection Sort
Vantagens:
- Simples de entender e implementar.
Desvantagens:
- Ineficiente para listas grandes (O(n²)).
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemplo de uso
print(selection_sort([64, 25, 12, 22, 11]))

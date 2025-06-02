"""
Bubble Sort
Vantagens:
- Muito fácil de entender e implementar.
Desvantagens:
- Muito ineficiente para listas grandes (O(n²)).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Exemplo de uso
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

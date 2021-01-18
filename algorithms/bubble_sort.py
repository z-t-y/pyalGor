def bubble_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


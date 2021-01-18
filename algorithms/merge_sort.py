def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    half = int(len(arr) / 2)
    left, right = arr[:half], arr[half:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
            continue
        result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

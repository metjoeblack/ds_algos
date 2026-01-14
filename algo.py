

def binary_search(seq, target):
    left_idx, right_idx = 0, len(seq) - 1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if seq[mid_idx] == target:
            return mid_idx
        elif seq[mid_idx] < target:
            left_idx += mid_idx + 1
        else:
            right_idx -= mid_idx - 1
    return -1


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



if __name__ == "__main__":
    print(selection_sort([2, 3, 1, 5, 10, 11, 2, 4]))
    print(insertion_sort([2, 3, 1, 5, 10, 11, 2, 4]))
    



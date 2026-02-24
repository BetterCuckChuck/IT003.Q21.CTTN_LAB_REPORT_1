import numpy as np
import heapq
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(arr):
    arr_copy = list(arr)
    n = len(arr_copy)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copy, n, i)
    for i in range(n - 1, 0, -1):
        arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
        heapify(arr_copy, i, 0)
    return arr_copy

def heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[largest]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def numpy_sort(arr):
    # Chuyển về numpy array và sort (QuickSort tối ưu C)
    np_arr = np.array(arr)
    np_arr.sort()
    return np_arr

def run_benchmark():
    # Bước 1: Đọc dữ liệu
    print("Đang đọc dữ liệu...")
    data_arrays = []
    with open("dataset.txt", 'r') as f:
        lines = f.readlines()
        for i in range(5): # 5 dòng đầu là int
            data_arrays.append(list(map(int, lines[i].strip().split())))
        for i in range(5, 10): # 5 dòng sau là float
            data_arrays.append(list(map(float, lines[i].strip().split())))

    # Bước 2: Chạy thử nghiệm
    algo_names = ['QuickSort', 'MergeSort', 'HeapSort', 'NumpySort']
    
    print(f"{'Dãy':<20} | {'QuickSort':<10} | {'MergeSort':<10} | {'HeapSort':<10} | {'Numpy':<10}")
    print("-" * 75)

    labels = [
        "1. Inc Int", "2. Dec Int", 
        "3. Rand Int A", "4. Rand Int B", "5. Rand Int C",
        "6. Rand Float A", "7. Rand Float B", "8. Rand Float C", "9. Rand Float D", "10. Rand Float E"
    ]

    totals = [0, 0, 0, 0]
    num_cases = len(data_arrays)

    for idx, arr_original in enumerate(data_arrays):
        current_times = []
        test_functions = [quick_sort, merge_sort, heap_sort, numpy_sort]

        for i, func in enumerate(test_functions):
            start = time.perf_counter()
            func(arr_original)
            duration_ms = round((time.perf_counter() - start) * 1000)
            current_times.append(duration_ms)
            totals[i] += duration_ms
        
        print(f"{labels[idx]:<20} | {current_times[0]:<10} | {current_times[1]:<10} | {current_times[2]:<10} | {current_times[3]:<10}")

    # Calculate and print Average row
    print("-" * 75)
    avg_quick = round(totals[0] / num_cases)
    avg_merge = round(totals[1] / num_cases)
    avg_heap  = round(totals[2] / num_cases)
    avg_numpy = round(totals[3] / num_cases)
    
    print(f"{'AVERAGE':<20} | {avg_quick:<10} | {avg_merge:<10} | {avg_heap:<10} | {avg_numpy:<10}")

if __name__ == "__main__":
    run_benchmark()
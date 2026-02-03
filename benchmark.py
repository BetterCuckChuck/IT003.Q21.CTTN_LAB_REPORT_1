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
    h = []
    for value in arr:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

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

    for idx, arr_original in enumerate(data_arrays):
        times = []
        
        # Test QuickSort
        arr = arr_original.copy()
        start = time.time()
        quick_sort(arr)
        times.append(time.time() - start)
        
        # Test MergeSort
        arr = arr_original.copy()
        start = time.time()
        merge_sort(arr)
        times.append(time.time() - start)
        
        # Test HeapSort
        arr = arr_original.copy()
        start = time.time()
        heap_sort(arr)
        times.append(time.time() - start)
        
        # Test Numpy Sort
        arr = arr_original.copy()
        start = time.time()
        numpy_sort(arr)
        times.append(time.time() - start)
        
        print(f"{labels[idx]:<20} | {times[0]:<10.6f} | {times[1]:<10.6f} | {times[2]:<10.6f} | {times[3]:<10.6f}")

if __name__ == "__main__":
    run_benchmark()
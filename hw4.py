"""
Python має дві вбудовані функції сортування: sorted і sort.
Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.
Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. 
Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних.
Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах
Для заміру часу виконання алгоритмів використовуйте модуль timeit.
Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків,
 використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.
"""
import random
from timeit import timeit

def insertion_sort(lst):
    """Insertion function """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    """Merge sort function """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    """Merge function"""
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def test_merge_sort(array):
    """Merge sort test function"""
    merge_sort(array)


def test_insertion_sort(array):
    """Insertion sort test function"""
    insertion_sort(array)


def test_timsort_sort(array):
    """Timsort sort test function"""
    sorted(array)

def run_test(func_part_name, array_part_name, times=1000):
    """Run test function"""
    print(f"Testing function {func_part_name} for array:{array_part_name} ....")
    elapsed_time = timeit(
        f"test_{func_part_name}_sort(array_{array_part_name})",
        setup=f"from __main__ import test_{func_part_name}_sort",
        number=times, globals=globals()
        )
    return f"Function: {func_part_name} sort array: {array_part_name} elapsed time:{elapsed_time}"

# Generate rundom numbers
array_sorted = [i for i in range(2000)]
array_not_sorted = [random.randint(1, 2000) for _ in range(2000)]
array_part_sorted = [i for i in range(500)] + [random.randint(500, 1500) for _ in range(1000)] +\
    [i for i in range(1500, 2000)]

for func_short_name in ["merge", "insertion", "timsort"]:
    for array_short_name in ["sorted", "not_sorted", "part_sorted"]:
        print(run_test(func_short_name, array_short_name, 5000))

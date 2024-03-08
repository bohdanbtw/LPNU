import numpy as np
import time
import tracemalloc
import memory_profiler
import random



def reverse_array(array):
  return array[::-1]

def bubble_sort(array):
  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
  return array

def insertion_sort(array):
  for i in range(1, len(array)):
    current_element = array[i]
    j = i - 1
    while j >= 0 and array[j] > current_element:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = current_element
  return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def binary_search(array):
  low = 0
  high = len(array) - 1
  mid = 0
  value = random.choice(array.copy())


  while low <= high:
    mid = (low + high) // 2
    if array[mid] == value:
      return mid
    elif array[mid] < value:
      low = mid + 1
    else:
      high = mid - 1

  return -1

def measure_time(func, array):
  start_time = time.time()
  func(array)
  end_time = time.time()
  return end_time - start_time

def measure_memory_tracemalloc(func, array):
  tracemalloc.start()
  func(array)
  current_memory, _ = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  return current_memory

def measure_memory_memory_profiler(func, array):
  @memory_profiler.profile
  def wrapper():
    func(array)

  wrapper()
  return memory_profiler.get_peak_memory()

def main():
  # array = np.randint(0, 100000, size = 10000)
  array = np.random.rand(10000)
  array = np.round(array, decimals=6)

  print(array)
  # Завдання 1: Обернути масив (reverse the array)

  start_time = time.time()
  
  reverse_array(array.copy())

  time.sleep(1)
  end_time = time.time()
  print((end_time - start_time) - 1)

  # Завдання 2: Сортування бульбашкою (bubble sort)
 
  start_time = time.time()
  
  bubble_sort(array.copy())

  end_time = time.time()
  print(end_time - start_time)

  # Завдання 3: Сортування вставкою (insertion_sort sort)

  start_time = time.time()
  
  insertion_sort(array.copy())

  end_time = time.time()
  print(end_time - start_time)

  # Завдання 4: Швидке сортування
 
  start_time = time.time()
  
  quick_sort(array.copy())

  end_time = time.time()
  print(end_time - start_time)

  # Завдання 5: Бінарний пошук

  np.sort(array)
  start_time = time.time()
  
  binary_search(array)
  time.sleep(1)
  end_time = time.time()
  print((end_time - start_time) - 1)


if __name__ == "__main__":
  main()

import random

def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

random_array = [random.randint(1, 50) for i in range(50)]
print(random_array)


print(bubble_sort(random_array))
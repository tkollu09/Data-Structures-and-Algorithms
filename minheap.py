# -*- coding: utf-8 -*-
"""MinHeap.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xwrXUlTn61_mott1_jbj6LLti3H64PQO

Min Heap Class
"""

class Min_Heap:
    def __init__(self):
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        self.percolateUp(len(self.heap) - 1) #should track length if using real array and not list

    def percolateUp(self, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def removeMin(self):
      if not self.heap:
        return None
      removed = self.heap[0]
      self.heap[0] = self.heap[len(self.heap) - 1] #should track length if using real array and not list
      self.heap.pop()
      self.percolateDown(0)
      return removed

    def percolateDown(self, index):
      length = len(self.heap)
      while True:
          left = 2 * index + 1
          right = 2 * index + 2
          smallest = index
          if left < length and self.heap[left] < self.heap[smallest]:
              smallest = left
          if right < length and self.heap[right] < self.heap[smallest]:
              smallest = right
          if smallest == index:
              break
          self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
          index = smallest


    def peekMin(self):
      if not self.heap:
        return None
      return self.heap[0]

    def lastNode(self):
      if not self.heap:
        return None
      return self.heap[len(self.heap) - 1] #should track length if using real array and not list

    def display(self):
      if not self.heap:
        return None
      return self.heap

"""Testing Heap"""

heap = Min_Heap()
test_input = [10, 20, 5, 30, 2, 7]
for val in test_input:
    heap.add(val)
print("Heap after insertions:", heap.display())
removed = []
while heap.peekMin() is not None:
    removed.append(heap.removeMin())
print("Removed elements in order:", removed)
print("Heap after removals:", heap.display())

heap1 = Min_Heap()
test_input1 = [10, 20, 5, 30, 2, 7]
for val in test_input1:
    heap1.add(val)
print("Heap after insertions:", heap1.display())
while heap1.peekMin() is not None:
  print(heap1.removeMin())
print("Heap after removals:", heap1.display())
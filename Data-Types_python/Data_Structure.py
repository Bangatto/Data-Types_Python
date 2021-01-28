#STACK
#List implementation 
# runs into speed issues..if the stack memory becomes bigger than the block of memory available
#then python need to do some memory allocation which slows down the append() calls[if the allocated size is full, an array 
# of double the size is created and the elements are copied into it which is 0(N) hence amortized time complexity of 0(1)]
stack = []
stack.append("BMO")
stack.append("Tesla")
stack.append("Google")
stack.append("BlackRock")
print(stack)
stack.pop()
print(stack)
print(stack.pop(-1))

#FAster Append and faster pop - USE DEQUE class from Collections ---O(1)
from collections import deque
stack = deque()
stack.append("BMO")
stack.appendleft("Google")
stack.append("Intuit")
stack.appendleft("BlackRock")
print(list(stack))
stack.pop()
stack.popleft()

#QUEUE  
#operated on First In, First Out (FIFO) policy, the first added elements are removed first
#Allows Inserting(Enqueue) and Removing(Dequeue) into the queue
#They do not allow random access to objects in the containers

#Implementation
#LIST -- Not very efficient as there is shifting to be done when removing the first element -- O(N)
#Use append(element) --> to enqueue an element and pop(0) to remove the first element added
q = []
q.append("Google")
q.append("Salesforce")
q.append("BlackRock")

#show the elements in the queue
#[Google, Salesforce, BlackRock]
q.pop(0) #Google
q.pop(0) #Salesforce

#Collections.deque class - MOST EFFICIENT
#this is the most recommended implementation becasue it allows Double End access of the elements
#You can add elements at the beginning and at the end
#Uses append(element) -- for Enqueue and popleft() to remove from the beginning
from collections import deque
q = deque()
q.append("Google")
q.append("Salesforce")
q.append("BlackRock")

q.popleft() #Google
q.popleft() #Salesforce

#HEAP
#Available in Heapq module
#Called Priority Queue-> The smallest element is always at the root ---> heap[0]
#heapify(iterable)---convert the iterable into a heap--->heap order(min heap)
#heapify----transform the list into a heap, in-place, in linear time
#heappush(iterable, element)--> insert element into the heap and order is always maintain
#heappop(iterable)---> removes and return the smallest element from the heap
import heapq
arr = [5,7,8,4,3]
print("Array is here",arr)
heapq.heapify(arr) #transform the list into a heap-inline
heapq.heappush(arr, 10)
heapq.heappush(arr, 1)
heapq.heappush(arr, 9)

heapq.heappop(arr) #1
heapq.heappop(arr) #3
heapq.heappop(arr) #4
#array has been transformed in-place and therefore it returns a heap
print(arr)
print(arr[0])

#nlargest(k, iterable)--returns a list with the kth largest element from the from the dataset
print(heapq.nlargest(1, arr))
print(heapq.nlargest(3, arr))
#nsmallest(k,iterable)--returns a list with the kth smallest element from the iterable 
print(heapq.nsmallest(1, arr))
print(heapq.nsmallest(3, arr))

#The above two perform best for smaller values of N. For larger values, use sorted() instead.

#Combined Heappush and Heappop (heappushpop(iterable, elemeent)) --> More Efficient than Separate heappush followed by a heappop()
print(heapq.heappushpop(arr, 12))

#TIME COMPLEXITIES
#Insertion-heappush (log N)-compare with the parent element only
#Delete -heappop (log N)-after removal, the heap invariant has to be maintained
#Heapify --O(N) rearrange all the nodes in the heap to obey heap invariant property

#MAX-HEAP
heapq._heapify_max(arr) #transform the iterable inline into a Max-Heap, largest element at index 0
heapq._heappop_max(arr) # removes and return the element at index 0 --->Largest element
print(arr)
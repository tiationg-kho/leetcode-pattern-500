# complexity

- **Time Complexity**
    - **Constant. O(k)**
        - running time is independent of the input size
    - **Logarithmic. O(log(n))**
        - like binary search or heap operations
    - **Linear. O(n)**
        - like nodes’ traversal
    - **Linearithmic**. **O(n * log(n))**
        - most sort operations
    - **Quadratic. O(n\*\*2)**
        - like a for-loop inside a for-loop
    - **Cubic. O(n\*\*3)**
        - like triple level’s for-loops
    - **Exponential. O(2\*\*n)**
        - like determining each element taking or not
    - **Factorial. O(n!)**
        - involves the idea of recursion
    - **Combinations. nCr** - O(n! / (r! * (n-r)!))
        - selecting items from a collection
    - **Catalan Number. Catalan(n)** - ((2n)C(n)) / (n+1) or C(2n, n) / (n+1) or (2n)! / (n+1)!n!
        - like n nodes can construct how many different structure binary trees
    - **Permutations. nPr** - O(n! / (n-r)!)
        - selecting items from a collection (order matter)
- **Space Complexity**
    - store space cost
    - should consider the temporary usage
        - like the dynamic cost inside some calling method
    - also consider the recursion’s cost
        - it will occupy memory stack
- **time and space are interrelated**
    - should consider the current demand to decide how to implement algorithm
    - sometimes we can also consider the amortized time complexity or average time complexity instead of only the worst case time complexity
        - average
            - quick sort: worst-case time complexity is O(n**2), average time complexity is O(nlogn)
                - worst-case happens due to bad pivot choice or nearly sorted array
        - amortized
            - dynamic array adding element: worst-case time complexity is O(n), amortized time complexity is O(1)
                - because when array is full, resizing takes O(n) time

# **Python**
# list
```python
# list

# initialize is O(n)
list0 = list() # []
list1 = [] # []
list2 = [1] * 5 # [1, 1, 1, 1, 1]
list3 = [i for i in range(5)] # [0, 1, 2, 3, 4]
list4 = [i ** 2 for i in range(5) if i % 2 == 0] # [0, 4, 16]
list5 = [[] for i in range(3)] # [[], [], []]
list6 = [[0 for c in range(2)] for r in range(3)] # [[0, 0], [0, 0], [0, 0]]

# list comprehension is O(n)
list1 = [6, 2, 8, 3, 1]
newlist = [x ** 2 for x in list1] # [36, 4, 64, 9, 1]
list2 = [1, 4, 5, 8, 9, 11, 13, 12]
newlist = [x for x in list2 if x % 2 == 1] # [1, 5, 9, 11, 13]
list3 = [1, 4, 5, 8, 9, 11, 13, 12]
newlist = [x + 1 if x % 2 == 1 else x for x in list3] # [2, 4, 6, 8, 10, 12, 14, 12]
list4 = [str(i) for i in range(1, 10)] # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list5 = [1, 3, 5, 7, 9, 11]
newlist = [x - 1 for x in list5] # [0, 2, 4, 6, 8, 10]

# reverse is O(n)
listA =[1, 2, 3]
listA.reverse()
print(listA) # [3, 2, 1]

# shallow copy is O(n)
# only copy the elements' ref, will have problems with 2D arrays
listA = [1, 2, 3]
listB = listA[:]
listC = list(listA)
print(listA) # [1, 2, 3]
print(listB) # [1, 2, 3]
print(listC) # [1, 2, 3]
listB[1] = 500
print(listA) # [1, 2, 3]
print(listB) # [1, 500, 3]
print(listC) # [1, 2, 3]

listA = [1, [10, 20]]
listB = listA[:]
listC = list(listA)
print(listA) # [1, [10, 20]]
print(listB) # [1, [10, 20]]
print(listC) # [1, [10, 20]]
listB[1][0] = 500
print(listA) # [1, [500, 20]]
print(listB) # [1, [500, 20]]
print(listC) # [1, [500, 20]]

# deep copy is O(n)
# clone the elements
import copy
listA = [1, [10, 20]]
listB = copy.deepcopy(listA)
print(listA) # [1, [10, 20]]
print(listB) # [1, [10, 20]]
listB[1][0] = 500
print(listA) # [1, [10, 20]]
print(listB) # [1, [500, 20]]

# append is O(1) in avg
list0 = []
list0.append(2) # [2]

# insert to the specified position
# append is O(1) but insert is O(n)
nums = [1, 2, 3, 4]
nums.insert(0, 12) # [12, 1, 2, 3, 4]

# extend is O(k)
nums = [12, 4, 3, 2, 1]
nums.extend([200, 300 ,500]) # [12, 4, 3, 2, 1, 200, 300, 500]
res = []
res.extend([[] for _ in range(5)])
print(res) # [[], [], [], [], []]
res = []
res.extend([])
print(res) # []
res = []
res.extend([[]])
print(res) # [[]]

# concat is O(n)
list1 = [1, 3, 60]
list2 = list1 + [5]
print(list1) # [1, 3, 60]
print(list2) # [1, 3, 60, 5]
list1 = [1, 3, 60]
list2 = list1.append(5)
print(list1) # [1, 3, 60, 5]
print(list2) # None
arr = [5, 8, 10]
arr = [0] + arr + [99]
print(arr) # [0, 5, 8, 10, 99]

# slice is O(k)
listA = [1, 3, 990, 30]
slice1 = listA[0:9]
slice2 = listA[1:3]
print(slice1) # [1, 3, 990, 30]
print(slice2) # [3, 990]

# pop() the last element is O(1)
# remove(value) and pop(index) are O(n)
nums = [12, 4, 3, 2, 1, 200, 300, 500]
nums.remove(300) # [12, 4, 3, 2, 1, 200, 500]
nums.pop(0) # [4, 3, 2, 1, 200, 500]
nums.pop() # [4, 3, 2, 1, 200]

# get is O(1)
arr = [5, 8, 10]
num = arr[1]
print(num) # 8

# index(value), return its index (first met), is O(n)
nums = [4, 3, 2, 1, 200]
nums.index(200) # 4

# min or max is O(n)
list_min_max = [20, 49, 8, -20]
max(list_min_max) # 49
min(list_min_max) # -20

# bisect
# finding insertion point for new element while maintaining the sorted order
# use left to find >= target and smallest
# use right to find > target and smallest 
# check location costs O(logn)
# insort inside costs O(n)
import bisect
list_bi = [20, 49, 88, 120]
i =bisect.bisect_left(list_bi, 50) # 2
j =bisect.bisect_right(list_bi, 50) # 2
list_bi2 = [20, 49, 50, 50, 88, 120]
k =bisect.bisect_left(list_bi2, 50) # 2
l =bisect.bisect_right(list_bi2, 50) # 4
m =bisect.bisect_right(list_bi2, 10) # 0
n =bisect.bisect_right(list_bi2, 130) # 6
m =bisect.bisect_left(list_bi2, 10) # 0
n =bisect.bisect_left(list_bi2, 130) # 6
list_bi = [20, 49, 88, 120]
bisect.insort_left(list_bi, 50)
print(list_bi) # [20, 49, 50, 88, 120]

# len is O(1)
arr = [5, 8, 10]
len(arr) # 3

# traverse is O(n)
nums = [20, 50, 60, -10, 100, -50]
for num in nums:
  print(num)
'''
20
50
60
-10
100
-50
'''

nums = [4, 2, 6, 9]
for i in range(len(nums) - 1, -1, -1):
  print(i)
'''
3
2
1
0
'''

nums = [1, 2, 3, 4]
for i, num in enumerate(nums):
    print(i, num)
'''
0 1
1 2
2 3
3 4
'''

nums = [1, 2, 3, 4]
for num in reversed(nums): # reverse list when looping. if use "sorted" then become O(nlogn)
    print(num)
print(nums)
'''
4
3
2
1
[1, 2, 3, 4]
'''

# zip() is O(n)
# zip will stop when one list reach end
names = ["aaa", "bbb", "cc", "dddd", "e"]
scores = [40, -5, 100, 99]
for name, score in zip(names, scores):
    print(f"name: {name}; score: {score}")
'''
name: aaa; score: 40
name: bbb; score: -5
name: cc; score: 100
name: dddd; score: 99
'''
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"idx: {i}; name: {name}; score: {score}")
'''
idx: 0; name: aaa; score: 40
idx: 1; name: bbb; score: -5
idx: 2; name: cc; score: 100
idx: 3; name: dddd; score: 99
'''

# 2D list operations
matrix = [[0, 5, 2], [7, 4, 5], [6, 7, 18]] # O(RC)
print(matrix)
'''
[[0, 5, 2], 
 [7, 4, 5], 
 [6, 7, 18]]
'''
c1, c2 = 0, 2
col = [row[c2] - row[c1] for row in matrix] # O(R)
print(col) # [2, -2, 12]
r1, r2 = 0, 2
row = [n2 - n1 for n1, n2 in zip(matrix[r1], matrix[r2])] # O(C)
print(row) # [6, 2, 16]

# count is O(n)
nums = [10, 20, 10, 20, 300, 500, 600]
nums.count(10) # 2
nums.count(300) # 1

# sort is O(nlogn)
# default sort (ascending)
nums.sort() # [1, 2, 3, 4, 12]
# reverse sort (descending)
nums.sort(reverse = True) # [12, 4, 3, 2, 1]
# listName.sort(), space O(n), time O(nlogn), no return value
# sorted(listName), space O(n), time O(nlogn), has return value,
# sorted(listName), without affecting the original, 
# sorted(listName), takes any iterable (list, tuple, set, dict(only get keys)), return list
list_unsort = [4, 5, 1, -10]
list_sorted = sorted(list_unsort)
print(list_unsort) # [4, 5, 1, -10]
print(list_sorted) # [-10, 1, 4, 5]
# self-defined sort for list
xs.sort(key = lambda x: - len(x)) # ['xxxxxxxxxx', 'xxxx', 'xxx', 'xx']
interval = [[10, -4], [2, 3], [7, -140]]
sorted(interval, key = lambda x: x[0]) # [[2, 3], [7, -140], [10, -4]]
a = [5, -5, -18, 10, 0]
a.sort(key = lambda x: x < 0) # [5, 10, 0, -5, -18]
# less than 0 one group, rest one group, inside group remain original order
b = [5, -5, -18, 10, 0]
b.sort(key = lambda x: abs(x)) # [0, 5, -5, 10, -18]
c = [5, -5, -18, 10, 0]
c.sort(key = lambda x: (x < 0, abs(x))) # [0, 5, 10, -5, -18]
d = [5, -5, -18, 10, 0]
d.sort(key = lambda x: (abs(x), x < 0)) # [0, 5, -5, 10, -18]
e = [5, -5, -18, 10, 0]
e.sort(key = lambda x: (abs(x), x > 0)) # [0, -5, 5, 10, -18]

# map is O(n)
# loops over the items
# map(str, nums) is a quick way to convert list's element to string

# SortedList
from sortedcontainers import SortedList
# O(nlogn) for init with parameters
sl = SortedList() # SortedList([])
sl = SortedList([3, 1, 2, 5, 4]) # SortedList([1, 2, 3, 4, 5])
sl = SortedList()
# O(logn) for add
sl.add(3)
sl.add(1)
sl.add(2) # SortedList([1, 2, 3])
# O(klogn) for update
sl = SortedList()
sl.update([3, 1, 2]) # SortedList([1, 2, 3])
# O(logn) for remove by val
sl = SortedList([1, 2, 3, 4, 5])
sl.remove(5) # SortedList([1, 2, 3, 4])
sl == [1, 2, 3, 4] # True
# O(logn) for pop largest element or pop by index
sl = SortedList('abcde')
sl.pop() # 'e'
sl.pop(2) # 'c' # SortedList(['a', 'b', 'd'])
# O(logn) for bisect_left
sl = SortedList([10, 11, 12, 13, 14])
sl.bisect_left(12) # 2
```

# dict
```python
# dict

# initialize is O(n)
d = {}
d = {'apple': 100}
# defaultdict
from collections import defaultdict
d = defaultdict(list)
print(d["A"]) # []
d = defaultdict(int)
print(d["A"]) # 0
d = defaultdict(lambda: 1)
print(d["A"]) # 1
d = defaultdict(lambda: [0] * 5)
d["A"][3] = 100
print(d) # defaultdict {'A': [0, 0, 0, 100, 0]})
d = defaultdict(ListNode) # we can also use our cutsom class as arg

# sometimes maintain a list in a dict's value is useful
hashmap = {}
hashmap["A"] = [100]
print(hashmap) # {'A': [100]}
hashmap["A"].append(200)
print(hashmap) # {'A': [100, 200]}

# put element, O(1) in avg
# dict require hashable keys (number, string, tuple...)
# or put an existed element, O(1) in avg
d = {'apple': 100}
d['box'] = 50
d['apple'] = 200
print(d) # {'apple': 200, 'box': 50}

# get value by indexing, O(1) in avg, could throw key error if key not existed
d = {'apple': 200, 'box': 50}
d['box'] # 50
# d['cat'] # key error

# pop element, O(1)
# pop will also return the deleted value
# pop wrong key without default value will throw key error
val = d.pop("box") 
print(val) # 50
print(d) # {}
val = d.pop("bird", "nonono")
print(val) # nonono
# d.pop('cat') # key error

# check key, O(1)
# key in mapping, return True or False
d = {'apple': 200, 'box': 50}
if "apple" in d:
    print("good")
'''
good
'''

# loop is O(n)
# loop dict's key
# if we want to pop key during iteration, use "for key in list(d.keys())"
for key in d:
    print(key)
'''
apple
box
'''
# loop dict's items
for key, val in d.items():
    print(key)
    print(val)
    print("---")
'''
apple
200
---
box
50
---
'''

# get all keys is O(n) if iterate
d = {'apple': 200, 'box': 50}
d.keys() # dict_keys(['apple', 'box'])

# get all values is O(n) if iterate
d.values() # dict_values([200, 50])

# get all items is O(n) if iterate
d.items() # dict_items([('apple', 200), ('box', 50)])

# length, O(1)
len(d) # 2

# get max val's key is O(n)
# notice max function only get the first one met condition
ages = {'Xatt': 30, 'Toe': 29, 'Nix': 31, 'Apps': 31, 'Appx': 31}
key_with_max_value = max(ages, key = ages.get) 
print(key_with_max_value) # Nix
key_with_max_value = max(ages, key = lambda x: ages[x])
print(key_with_max_value) # Nix
max_key = max(ages.keys())
print(max_key) # Xatt
value_with_max_key = ages[max(ages.keys())]
print(value_with_max_key) # 30

# SortedDict
from sortedcontainers import SortedDict
# init, O(1)
sd = SortedDict()
print(sd) # SortedDict({})
# add, O(logn)
sd['c'] = 3
print(sd) # SortedDict({'c': 3})
# pop, O(logn)
num = sd.pop('c')
print(num) # 3
print(sd) # SortedDict({})
# setdefault, O(logn)
sd.setdefault('a', 10)
print(sd) # SortedDict({'a': 10})
sd.setdefault('a', 5)
print(sd) # SortedDict({'a': 10})
sd.setdefault('b', [])
print(sd) # SortedDict({'a': 10, 'b': []})
sd.setdefault('c', []).append(18)
print(sd) # SortedDict({'a': 10, 'b': [], 'c': [18]})
sd.setdefault('c', []).append(5)
print(sd) # SortedDict({'a': 10, 'b': [], 'c': [18, 5]})
# get, O(logn)
# get with wrong key will throw key error
num = sd['a']
print(num) # 10
nums = sd['c']
print(nums) # [18, 5]
# peekitem, O(logn)
k_v = sd.peekitem(0)
print(k_v) # ('a', 10)
k_v = sd.peekitem(- 1)
print(k_v) # ('c', [18, 5])
k_v = sd.peekitem()
print(k_v) # ('c', [18, 5])
# bisect_left for key, O(logn)
sd = SortedDict({5: 'a', 10: 'b', 20: 'c'})
idx = sd.bisect_left(10)
print(idx) # 1
k_v = sd.peekitem(idx) 
print(k_v) # (10, 'b')
idx = sd.bisect_left(15)
print(idx) # 2
k_v = sd.peekitem(idx) 
print(k_v) # (20, 'c')
idx = sd.bisect_left(0)
print(idx) # 0
idx = sd.bisect_left(25)
print(idx) # 3
```

# set
```python
# set

# initialize is O(n)
s1 = set()
# with elements to initialize
s2 = {"a", "b", "c", "d"}

# add, O(1)
s1.add(999)
print(s1) # {999}
s2.add("errr")
print(s2) # {'b', 'errr', 'a', 'd', 'c'}

# update can add multiple ones, O(k)
list_for_update = [77, 88, 100]
s1.update(list_for_update)
print(s1) # {88, 100, 77, 999}

# search element, O(1)
print(500 in s1) # False

# get size, O(1)
print(len(s1)) # 4
print(len(s2)) # 5

# remove/discard element, O(1)
# if the item to remove does not exist, remove() will raise an error
# discard() won't raise any error
s2 = {'b', 'errr', 'a', 'd', 'c'}
s2.remove("errr")
print(s2) # {'b', 'c', 'a', 'd'}
dis_rtn = s2.discard("a")
dis_rtn = s2.discard("zzz")
print(s2) # {'b', 'c', 'd'}

# pop(), cannot guarantee which element, O(1)
s = {1, 2, 3, 4}
val = s.pop()
print(val) # 1
print(s) # {2, 3, 4}

# intersection() is O(min(n, m))
# method returns a set that contains the similarity between two or more sets
# set.intersection(set1, set2 ... etc)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
print(s3) # {3}

# union() is O(n+m)
# will create a new set that contains all the elements from the sets provided
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3) # {1, 2, 3, 4, 5}

# difference() is O(n)
# will return only the elements that are unique to the first set (invoked set)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)
s4 = s2.difference(s1)
print(s3) # {1, 2}
print(s4) # {4, 5}

# symmetric_difference() is O(n+m)
# will return all the elements that are not common between them
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3) # {1, 2, 4, 5}
```

# tuple
```python
# tuple

# tuple is a collection which is ordered and unchangeable
# tuple's operations and complexities are same as list except for those would change elements

# unpack is O(n)
t = ("a", "b", "c", "d", "e")
(front, *middle, end) = t
print(front) # a
print(middle) # ['b', 'c', 'd']
print(end) # e

# initialize is O(n)
t = tuple(("a", "b", "c")) # ('a', 'b', 'c')
t = tuple(["a", "b", "c"]) # ('a', 'b', 'c')
# one item tuple, remember the comma
t = ("abc",) # ('abc',)
```

# heap
```python
# heap

# heap is a complete binary tree
# min heap's min is its root
# min heap's every node's value is smaller than its children

from heapq import *

# using heapify to convert list into heap, O(n)
# initializing list first, if list is empty then skip heapify step
nums = [5, 7, 9, 1, 3]
heapify(nums)
print(nums) # [1, 3, 9, 7, 5]

# peek root, heap[0] element returns the smallest element each time, O(1)
nums[0] # 1

# push, O(logn)
heappush(nums, 4)
print(nums) # [1, 3, 4, 7, 5, 9]

# pop, O(logn) 
num = heappop(nums)
print(num) # 1
print(nums) # [3, 5, 4, 7, 9]

# how to create max heap, just times -1 to every element and create min heap
list1 = [5, 7, 9, 1, 3]
list2 = [-(ele) for ele in list1]
heapify(list2)
print(list2) # [-9, -7, -5, -1, -3]
```

# queue
```python
# queue
# in Python, list can be used as stack
# but we use deque as queue

from collections import deque

# initialize is O(n)
queue1 = deque("apple") # deque(['a', 'p', 'p', 'l', 'e'])
queue2 = deque() # deque([])
queue3 = deque((25, 40)) # deque([25, 40])
queue4 = deque(["apple"]) # deque(['apple'])
listA = [4, 4]
queue5 = deque(listA) # deque([4, 4])
queue6 = deque(range(5)) # deque([0, 1, 2, 3, 4])
queue7 = deque([]) # deque([])
# initialize with max len
# will auto popleft when over capacity
q = deque([], maxlen=2)
q.append(1)
q.append(2)
print(q) # deque([1, 2], maxlen=2)
q.append(3)
print(q) # deque([2, 3], maxlen=2)

# append(value), O(1)
queue2 = deque() # deque([])
queue2.append("a") # deque(['a'])
queue2.append(["b"]) # deque(['a', ['b']])
queue2.append("c") # deque(['a', ['b'], 'c'])

# popleft(), O(1)
queue2.popleft() # a
queue2.popleft() # ['b']
queue2.popleft() # c
# queue2.popleft() # index error

# pop() is O(1), remove the end of the deque

# appendleft() is O(1), add to the front of the deque

# extend() is O(k), add multiple values
```

# number
```python
# number

# num of max or min value
float('inf') # inf (max num)
float('-inf') # -inf (min num)

# exponent
2 ** 3 # 8

# modulus/remainder
22 % 8 # 6

# integer division
22 // 8 # 2

# divmod() method takes two numbers and returns a pair of numbers (a tuple) 
# consisting of their quotient and remainder
print(divmod(3, 8)) # (0, 3)
print(divmod(32, 8)) # (4, 0)
print(divmod(13, 8)) # (1, 5)

# type change
str(29) # '29'
int(7.7) # 7
float("111.3") # 111.3

# abs
abs(-66.6) # 66.6

# min, can put key inside
a = [1, 2, 3]
min(a) # 1

# max, can put key inside
a = {'aaa', 'bb', 'ccccc', 'ee'}
max(a, key = lambda x: len(x)) # ccccc

# sum
a = [1, 2, 3]
sum(a) # 6

# binary transition
# remember to remove the '0b'
# 0b is a prefix for binary (base-2) literal
# 0x is a prefix for hexadecimal (base-16) literal
# the leading 0s are omitted and that's why we have 10101 instead of 010101
bin(10) # '0b1010'
int("1010", 2) # 10
bin(0xff) # '0b11111111'
int(0xff) # 255

# convert an integer val to 4-byte string
# 256 == 8 bits == 1 byte
bin(0xff) # '0b11111111'
val = 255
byte_array = [(val >> (8 * i)) & 0xFF for i in range(4)][:: - 1] # [0, 0, 0, 255] 
val = 256 + 2
byte_array = [(val >> (8 * i)) & 0xFF for i in range(4)][:: - 1] # [0, 0, 1, 2]
val = 256 * 2
byte_array = [(val >> (8 * i)) & 0xFF for i in range(4)][:: - 1] # [0, 0, 2, 0]
val = 256 * 256 * 256 * 255 + 65 # 4278190145
byte_array = [(val >> (8 * i)) & 0xFF for i in range(4)][:: - 1] # [255, 0, 0, 65]
char_array = [chr(val) for val in byte_array] # ['ÿ', '\x00', '\x00', 'A']
string = ''.join(char_array)
print(len(string)) # 4

# gcd
# also here is a lcm() could be used, from math import lcm
from math import gcd
a = 50
b = 30
gcd = gcd(a, b)
print(gcd) # 10
lcm = a * b // gcd
print(lcm) # 150

# random
# [a, b]
import random
num0 = random.randint(0, 3)
num1 = random.randint(0, 3)
num2 = random.randint(0, 3)
num3 = random.randint(0, 3)
num4 = random.randint(0, 3)
print(num0, num1, num2, num3, num4) # 1 0 3 2 3
# choice
import random
listA = [1, 2, 3, 4]
print(random.choice(listA)) # 4
print(random.choice(listA)) # 1
print(random.choice(listA)) # 2
print(random.choice(listA)) # 3
print(random.choice(listA)) # 4
# [a, b) 
import random
print(random.randrange(3, 9)) # 6

# negative division
# be careful when dealing negative division
num = 10
num2 = - 7
num3 = - 17
print(num / num2) # -1.4285714285714286
print(num / num3) # -0.5882352941176471
print(num // num2) # - 2
print(num // num3) # - 1
print(int(num / num2)) # - 1 # truncate toward zero
print(int(num / num3)) # 0 # truncate toward zero
num = 10
num2 = 7
num3 = 17
print(num // num2) # 1
print(num // num3) # 0
print(-105 // 10) # - 11
print(int(-105 / 10)) # - 10
print(-102 % 10) # 8
print(102 % -10) # -8

# is_integer(), only for float
num1 = 0.0
num2 = - 1.0
num3 = 1.0
num4 = 1.2
num5 = 10.01
print(num1.is_integer()) # True
print(num2.is_integer()) # True
print(num3.is_integer()) # True
print(num4.is_integer()) # False
print(num5.is_integer()) # False

# type checking
num1 = 1
num2 = 9.9
num3 = [0, 1]
num4 = [0, 1, 2]
num5 = None
print(isinstance(num1, int)) # True
print(isinstance(num2, float)) # True
print(isinstance(num3, list)) # True
print(isinstance(num4, int)) # False
print(isinstance(num5, int)) # False

# permutations and combinations
from itertools import permutations
from itertools import combinations
# nPr = n! // (n-r)!
# nCr = n! // (r!*(n-r)!)
perm1 = permutations([1, 2, 3])
print(list(perm1)) 
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm2 = permutations([1, 2, 3, 4], 2)
print(list(perm2)) 
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
comb1 = combinations([1, 2, 3, 4], 2)
print(list(comb1)) 
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
comb2 = combinations([1, 1, 1, 4], 2)
print(list(comb2))
# [(1, 1), (1, 1), (1, 4), (1, 1), (1, 4), (1, 4)]
comb2 = combinations([1, 1, 1, 4], 2)
print(set(comb2))
# {(1, 1), (1, 4)}

# floor and ceil
import math
math.ceil(1.4) # 2
math.floor(1.4) # 1
math.ceil(- 1.1) # - 1
math.floor(- 1.1) # - 2

# bitmasking
# start from: mask = 0
# checking: mask & 1<<k == 0, if equals 0 means not mask 1<<k yet
# masking: mask = mask | 1<<k
# notice: we can also use "mask = mask ^ 1<<k" to mask for different purpose
mask = 0
print(bin(mask)) # 0b0
print(mask & 1<<3) # 0
mask = mask | 1<<3
print(mask) # 8
print(bin(mask)) # 0b1000
print(mask & 1<<3) # 8
print(mask & 1<<5) # 0
mask = mask | 1<<5
print(mask) # 40
print(bin(mask)) # 0b101000
print(mask & 1<<3) # 8
print(mask & 1<<5) # 32
print(mask & 1<<4) # 0
mask = 0
print(mask & 1<<3) # 0
mask = mask ^ 1<<3
print(mask) # 8
print(mask & 1<<3) # 8
mask = mask ^ 1<<3
print(mask) # 0

# a + b == ((a & b) << 1) + (a ^ b)
# first part means if each bit is 1 in both a and b, then we need to carry to next bit
# second part means if each bit is (1 and 0) or (0 and 1) in a and b, we don't need to shift, just add it to result
a = 3
b = 18
print(a + b) # 21
print((a & b)) # 2
print((a & b) << 1) # 4
print(a ^ b) # 17
print(a + b == ((a & b) << 1) + (a ^ b)) # True
print(bin(3)) #     0b11
print(bin(18)) # 0b10010
print(bin(21)) # 0b10101
print(bin(2)) #     0b10
print(bin(4)) #    0b100
print(bin(17)) # 0b10001
def bitwise_add(a, b):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a
num = bitwise_add(3, 2)
print(num) # 5

# logic operate table
# bitwise and
# bitwise or
# bitwise xor
# bitwise not
'''
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0

1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0

x & 0 = 0
x & 1 = x
x ^ 0 = x
x ^ 1 = ~x
'''

# isclose()
import math  
print(math.isclose(1, 1)) # True
print(math.isclose(1, 1.1)) # False
print(math.isclose(1, 1.01)) # False
print(math.isclose(1, 1.001)) # False
print(math.isclose(1, 1.0001)) # False
print(math.isclose(1, 1.00001)) # False
print(math.isclose(1, 1.000001)) # False
print(math.isclose(1, 1.0000001)) # False
print(math.isclose(1, 1.00000001)) # False
print(math.isclose(1, 1.000000001)) # False
print(math.isclose(1, 1.0000000001)) # True

# e
print(1.5434e5) # 154340.0
print(2e6) # 2000000.0

# num is a power of two: n > 0 and n & (n - 1) == 0
# num is a power of four: n > 0 and n & (n - 1) == 0 and n % 3 == 1

# format()
print(format(215.2, '.3f')) # '215.200'
print(format(215.2, '9')) # '    215.2'
print(format(215.2, '09')) # '0000215.2'
print(format(215.2, '016.5f')) # '0000000215.20000'

# factorial
import math
print(math.factorial(5)) # 120

# sqrt
from math import sqrt
print(sqrt(5)) # 2.23606797749979
print(int(sqrt(5))) # 2
```

# string
```python
# string

# split
s = "hello, this is hooo, I am yolo"
new_s = s.split(", ") # ['hello', 'this is hooo', 'I am yolo']
s = "f s t v gyh"
new_s = s.split(" ") # ['f', 's', 't', 'v', 'gyh']
s = "f& ,s t vb= gyh"
new_s = s.split(",") # ['f& ', 's t vb= gyh']
s = "//../..xd/.rs/"
new_s = s.split("/") # ['', '', '..', '..xd', '.rs', '']
s = "///"
new_s = s.split("/") # ['', '', '', '']

# search
sentence = 'hello'
result = sentence.index('el') # 1

# startswith
txt = "Hello, welcome to my world."
x = txt.startswith("Hello") # True

# sort
string = "note book"
string_sorted = sorted(string)
print(string) # note book
print(string_sorted) # [' ', 'b', 'e', 'k', 'n', 'o', 'o', 'o', 't']

# join
print("!".join(string_sorted)) #  !b!e!k!n!o!o!o!t
print("@".join(["a", "Q", "123"])) # a@Q@123
print("&".join("apple care")) # a&p&p&l&e& &c&a&r&e

# upper, there is also a lower() func
b = {"abc", "def"}
c = {s.upper() for s in b} # {'ABC', 'DEF'}

# isalnum() method returns all characters in the string are alphanumeric (either alphabets or numbers) or not
name = "M234onica"
print(name.isalnum()) # True
name = "M3onica Gell22er "
print(name.isalnum()) # False

# isalpha()
txt = "324"
print(txt.isalpha()) # False
txt = "CompanyXXXZ"
print(txt.isalpha()) # True
txt = "3df4"
print(txt.isalpha()) # False

# isdigit/isnumeric/isdecimal, for base 10 numbers
txt = "10"
x = txt.isdigit() # True
y = txt.isnumeric() # True
z = txt.isdecimal() # True
txt = "-10"
x = txt.isdigit() # False
y = txt.isnumeric() # False
z = txt.isdecimal() # False

# convert
int('-15') # -15
chr(97)  # a
chr(126) # ~
ord('\x00') # 0, '\x00' is null character in hexadecimal notation
ord('\u0000') # 0, '\u0000' is null character in Unicode notation. 0000 is the hexadecimal representation of the Unicode point for the null character
ord('0') # 48
ord('9') # 57
ord('A') # 65
ord('Z') # 90
ord('a') # 97
ord('z') # 122
ord('\xFF') # 255
ord('\u00FF') # 255

# pre-initialized string
import string 
result = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
result = string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
result = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
result = string.hexdigits # 0123456789abcdefABCDEF
result = string.digits # 0123456789

# count
string = "apple"
print(string.count('#')) # 0
print(string.count('p')) # 2

# lstrip(), also have rstrip() / strip()
s1 = '    4024'
print(s1.lstrip()) # '4024'
print(s1) # '    4024'
s2 = '....40'
print(s2.lstrip('.')) # '40'
print(s2) # '....40'

# capitalize
txt = "hello"
print(txt.capitalize()) # Hello

# unpack
txt = 'abcd'
c1, c2, c3, c4 = txt
print(c1, c2, c3, c4) # a b c d

# fstring
name = 'Ononx'
print(f'hi {name}') # hi Ononx

# replace
s = '000X0'
s = s.replace('X', '*') # 000*0

# concat
s = '0'
s = '1' + s + '1' # '101'
```

# class
```python
# class

# typical usage
from functools import cache
class App:
    def __init__(self):
        self.name = "app"

    def printString(self, string):
        print(string)
    
    @cache
    def factorial(self, n):
        return n * self.factorial(n - 1) if n else 1
    
if __name__ == "__main__":
    app = App()
    print(app.name) # app
    app.printString("test") # test
    print(app.factorial(5)) # 120

# dunder method
# initializes new object instances
def __init__(self, args):
    pass
# defines equal comparison
def __eq__(self, other):
    pass
# defines less than comparison
def __lt__(self, other):
    pass
# defines less or equal comparison
def __le__(self, other):
    pass
# provides string representation of object
def __str__(self):
    pass
# returns length or size of object
def __len__(self):
    pass

# decorator
# cache decorator can memoize or cache the return value of a function
from functools import cache
@cache
def method():
    pass

# module

# a module in Python is essentially a file containing Python definitions and statements
# the file name is the module name with the suffix .py added
# can define functions, classes, and variables, and can include runnable code

# __name__ variable evaluates to the name of the module
# if a file is being run as the main program, __name__ is set to the string "__main__"

# CODES will run when we are running this module as the main program
# if we are importing this module, then these CODES will not run
if __name__ == "__main__":
	# CODES here
    pass

# scope
# LEGB rules: local -> enclosing -> global -> builtin

# global scope
x = "globalX"
y = "globalY"
z = "globalZ"

def outer():
    # enclosing scope
    x = "enclosingX"
    y = "enclosingY"
    z = "enclosingX"

    def inner():
        # global
        global z

        # nonlocal
        nonlocal y
        
        # local scope
        x = "localX"

        print(x)
        print(y)
        print(z)

    inner()

outer()
# localX
# enclosingY
# globalZ

```

# **Java**

# Array
```Java
package ArraySyntax;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        // Array

        // Array init in O(n)
        int[] intArr = new int[5];
        System.out.println(Arrays.toString(intArr)); // [0, 0, 0, 0, 0]

        long[] longArr = new long[5];
        System.out.println(Arrays.toString(longArr)); // [0, 0, 0, 0, 0]

        char[] charArr = new char[5];
        System.out.println(Arrays.toString(charArr)); // [, , , , ]
        System.out.println(charArr[0] == '\u0000'); // true

        int[] intArr2 = new int[]{9, 3, 2, 100, 4};
        System.out.println(Arrays.toString(intArr2)); // [9, 3, 2, 100, 4]
        System.out.println("-----");

        // Array set in O(1)
        intArr[2] = 100;
        System.out.println(Arrays.toString(intArr)); // [0, 0, 100, 0, 0]
        System.out.println("-----");

        // Array get in O(1)
        int ele = intArr[2];
        System.out.println(ele); // 100
        System.out.println("-----");

        // Array length in O(1)
        int size = intArr.length;
        System.out.println(size); // 5
        System.out.println("-----");

        // Array fill in O(n)
        Arrays.fill(intArr, 9);
        System.out.println(Arrays.toString(intArr)); // [9, 9, 9, 9, 9]
        System.out.println("-----");

        // Array traverse in O(n)
        for (int i = 0; i < intArr2.length; i++) {
            System.out.print(i + ": " + intArr2[i] + ", ");
        }
        System.out.println(); // 0: 9, 1: 3, 2: 2, 3: 100, 4: 4,

        for (int num: intArr2) {
            System.out.print(num + ", ");
        }
        System.out.println(); // 9, 3, 2, 100, 4,
        System.out.println("-----");

        // Array sort
        // if elements are primitives, use dual-pivot quick sort
        // time in O(nlogn) in avg/best, worst can be O(n**2)
        // space in O(logn) in avg/best, worst can be O(n)
        // if elements are objects, use timsort (merge sort and insertion sort)
        // time in O(nlogn) in avg/worst, best can be O(n) for nearly sorted data
        // space in O(n)
        Arrays.sort(intArr2);
        System.out.println(Arrays.toString(intArr2)); // [2, 3, 4, 9, 100]

        String[] stringArr = {"a", "c", "e", "b", "d"};
        Arrays.sort(stringArr, Comparator.naturalOrder()); // Comparator do not support primitive types
        System.out.println(Arrays.toString(stringArr)); // [a, b, c, d, e]

        Arrays.sort(stringArr, Comparator.reverseOrder()); // Comparator do not support primitive types
        System.out.println(Arrays.toString(stringArr)); // [e, d, c, b, a]

        String[] stringArr2 = {"banana", "cucumber", "apple"};
        Arrays.sort(stringArr2, (a, b) -> Integer.compare(b.length(), a.length()));
        System.out.println(Arrays.toString(stringArr2)); // [cucumber, banana, apple]

        int[][] intervals = new int[][]{{1, 3}, {1, 2}, {0, 0}, {4, 5}};
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        for (int[] interval: intervals) {
            System.out.println(Arrays.toString(interval));
        }
        /*
        [0, 0]
        [1, 2]
        [1, 3]
        [4, 5]
        */
        System.out.println("-----");

        // Array reverse in O(n)
        System.out.println(Arrays.toString(intArr2)); // [2, 3, 4, 9, 100]
        int left = 0;
        int right = intArr2.length - 1;
        while (left < right) {
            int temp = intArr2[left];
            intArr2[left] = intArr2[right];
            intArr2[right] = temp;
            left += 1;
            right -= 1;
        }
        System.out.println(Arrays.toString(intArr2)); // [100, 9, 4, 3, 2]
        System.out.println("-----");

        // Array 2D in O(RC)
        int[][] matrix1 = new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        for (int row = 0; row < matrix1.length; row++) {
            for (int col = 0; col < matrix1[row].length; col++) {
                System.out.print(matrix1[row][col] + " ");
            }
            System.out.println();
        }
        /*
        1 2 3 
        4 5 6 
        7 8 9 
        */

        int[][] matrix2 = new int[3][5];
        for (int row = 0; row < matrix2.length; row++) {
            for (int col = 0; col < matrix2[row].length; col++) {
                System.out.print(matrix2[row][col] + " ");
            }
            System.out.println();
        }
        System.out.println("-----");
        /*
        0 0 0 0 0 
        0 0 0 0 0 
        0 0 0 0 0 
        */

        // Array of objects convert to ArrayList in O(n)
        String[] objArr = {"A", "B", "C", "D"};
        List<String> arrayList = new ArrayList<>(Arrays.asList(objArr));
        System.out.println(arrayList); // [A, B, C, D]
        System.out.println("-----");

        // Array of primitives convert to ArrayList in O(n)
        int[] priArr = new int[]{3, 9, 10};
        ArrayList<Integer> arrayList2 = new ArrayList<>();
        for (int num: priArr) {
            arrayList2.add(num);
        }
        System.out.println(arrayList2); // [3, 9, 10]
        System.out.println("-----");

        // Array copyOfRange in O(n)
        String[] stringArr3 = new String[]{"H", "A", "L", "I"};
        String[] stringArr3Copy1 = Arrays.copyOfRange(stringArr3, 1, 2);
        System.out.println(Arrays.toString(stringArr3Copy1)); // [A]

        String[] stringArr3Copy2 = Arrays.copyOfRange(stringArr3, 0, stringArr3.length);
        System.out.println(Arrays.toString(stringArr3Copy2)); // [H, A, L, I]
        System.out.println("-----");

        // Array min or max in O(n)
        char[] charArr2 = {'H', 'Z', 'X', 'B'};
        char maxChar = charArr2[0];
        for (char c: charArr2) {
            if (c > maxChar) {
                maxChar = c;
            }
        }
        System.out.println(maxChar); // Z

        Character[] characterArr = {'Q', 'R', 'Y', 'B'};
        Character minCharacter = characterArr[0];
        for (Character c: characterArr) {
            if (c < minCharacter) {
                minCharacter = c;
            }
        }
        System.out.println(minCharacter); // B
        System.out.println("-----");
    }
}

```

# ArrayList
```Java
package ArrayListSyntax;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        // ArrayList
        // contain objects instead of primitives

        // ArrayList init in O(1) or O(n)
        List<Integer> list1 = new ArrayList<>();
        List<int[]> listOfArr = new ArrayList<>();
        System.out.println(list1); // []
        System.out.println("-----");

        // ArrayList add in O(1) (avg)
        list1.add(5);
        list1.add(8);
        list1.add(20);
        System.out.println(list1); // [5, 8, 20]
        System.out.println("-----");

        // ArrayList get in O(1)
        System.out.println(list1.get(0)); // 5
        System.out.println("-----");

        // ArrayList size in O(1)
        System.out.println(list1.size()); // 3
        System.out.println(list1.isEmpty()); // false
        System.out.println("-----");

        // ArrayList set in O(1)
        list1.set(2, 99);
        System.out.println(list1); // [5, 8, 99]
        System.out.println("-----");

        // ArrayList add (with idx) in O(n)
        list1.add(0, 100);
        System.out.println(list1); // [100, 5, 8, 99]
        System.out.println("-----");

        // ArrayList remove in O(n), but remvoe last element is O(1)
        list1.remove(list1.size() - 1);
        System.out.println(list1); // [100, 5, 8]
        System.out.println("-----");

        // ArrayList sort in O(nlogn)
        Collections.sort(list1);
        System.out.println(list1); // [5, 8, 100]

        Collections.sort(list1, Comparator.reverseOrder());
        System.out.println(list1); // [100, 8, 5]

        Collections.sort(list1, Comparator.naturalOrder());
        System.out.println(list1); // [5, 8, 100]

        ArrayList<String> stringArrayList = new ArrayList<>(Arrays.asList("ab", "o", "zxz"));
        Collections.sort(stringArrayList, (a, b) -> Integer.compare(b.length(), a.length()));
        System.out.println(stringArrayList); // [zxz, ab, o]
        System.out.println("-----");

        // ArrayList convert to array of objects in O(n)
        List<String> list2 = new ArrayList<>(Arrays.asList("A", "B", "C"));
        String[] array = list2.toArray(new String[list2.size()]);
        System.out.println(Arrays.toString(array)); // [A, B, C]
        System.out.println("-----");

        // ArrayList convert to array of primitives in O(n)
        List<Integer> integerList = new ArrayList<>(Arrays.asList(1, 2, 3));
        int[] intArr = new int[integerList.size()];
        for (int i = 0; i < integerList.size(); i++) {
            intArr[i] = integerList.get(i);
        }
        System.out.println(Arrays.toString(intArr)); // [1, 2, 3]
        System.out.println("-----");

        // ArrayList reverse in O(n)
        Collections.reverse(list2);
        System.out.println(list2); // [C, B, A]
        System.out.println("-----");

        // ArrayList traverse in O(n)
        List<String> list3 = new ArrayList<>();
        list3.add("Item1");
        list3.add("Item2");
        list3.add("Item3");
        for (int i = 0; i < list3.size(); i++) {
            String item = list3.get(i);
            System.out.println("for-loop: " + item);
        }
        /*
        for-loop: Item1
        for-loop: Item2
        for-loop: Item3
        */

        for (String item: list3) {
            System.out.println("for-each: " + item);
        }
        System.out.println("-----");
        /*
        for-each: Item1
        for-each: Item2
        for-each: Item3
        */

        // ArrayList 2D in O(RC)
        List<List<Integer>> matrix = new ArrayList<>();
        for (int r = 0; r < 3; r++) {
            List<Integer> innerList = new ArrayList<>();
            for (int c = 0; c < 5; c++) {
                innerList.add(0);
            }
            matrix.add(innerList);
        }
        System.out.println(matrix);
        System.out.println("-----");
        /*
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        */

        // ArrayList subList in O(n)
        List<String> subList3 = list3.subList(1, 2);
        System.out.println(subList3); // [Item2]

        List<String> subList4 = list3.subList(0, list3.size());
        System.out.println(subList4); // [Item1, Item2, Item3]
        System.out.println("-----");

        // ArrayList addAll in O(k)
        subList3.addAll(Arrays.asList("newItem1", "newItem2"));
        System.out.println(subList3); // [Item2, newItem1, newItem2]

        String[] stringArr = new String[]{"item100", "item200", "item500"};
        subList3.addAll(Arrays.asList(Arrays.copyOfRange(stringArr, 0, 2)));
        System.out.println(subList3); //[ Item2, newItem1, newItem2, item100, item200]

        List<Integer> firstList = new ArrayList<>();
        firstList.add(10);
        firstList.add(20);
        List<Integer> secondList = new ArrayList<>();
        secondList.add(- 5);
        firstList.addAll(secondList);
        System.out.println(firstList); // [10, 20, -5]
        System.out.println("-----");

        // ArrayList min or max in O(n)
        int minVal = Collections.min(firstList);
        System.out.println(minVal); // - 5

        Integer maxVal = Collections.max(firstList);
        System.out.println(maxVal); // 20
        System.out.println("-----");

        // ArrayList binarySearch in O(logn)
        // if have duplicate target vals, not guarantee which idx of them will be returned
        // try to get first/last one of them will cost additional O(k)
        List<Integer> list4 = new ArrayList<>(Arrays.asList(20, 49, 88, 120));
        int foundIdx = Collections.binarySearch(list4, 49);
        System.out.println(foundIdx); // 1

        int nonFoundIdx1 = Collections.binarySearch(list4, 50);
        System.out.println(nonFoundIdx1); // - 3
        System.out.println(~ nonFoundIdx1); // 2, is insertion point idx

        int nonFoundIdx2 = Collections.binarySearch(list4, 130);
        System.out.println(nonFoundIdx2); // - 5
        System.out.println(~ nonFoundIdx2); // 4, is insertion point idx

        int nonFoundIdx3 = Collections.binarySearch(list4, 8);
        System.out.println(nonFoundIdx3); // - 1
        System.out.println(~ nonFoundIdx3); // 0, is insertion point idx
        System.out.println("-----");
    }
}

```

# HashMap
```Java
package HashMapSyntax;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {

    public static void main(String[] args) {

        // HashMap

        // HashMap init in O(1) or O(n)
        HashMap<String, Integer> map = new HashMap<>();
        System.out.println(map); // {}
        System.out.println("-----");

        // HashMap put in O(1) (avg)
        map.put("first", 1);
        map.put("second", 2);
        System.out.println(map); // {first=1, second=2}

        map.put("second", 50);
        System.out.println(map); // {first=1, second=50}
        System.out.println("-----");

        // HashMap get in O(1) (avg)
        System.out.println(map.get("first")); // 1
        System.out.println(map.get("third")); // null
        System.out.println("-----");

        // HashMap containsKey in O(1) (avg)
        System.out.println(map.containsKey("first")); // true
        System.out.println(map.containsKey("third")); // false
        System.out.println("-----");

        // HashMap remove in O(1) (avg)
        map.remove("second");
        System.out.println(map); // {first=1}
        System.out.println("-----");

        // HashMap size in O(1)
        System.out.println(map.size()); // 1
        System.out.println(map.isEmpty()); // false
        System.out.println("-----");

        // HashMap keySet in O(n)
        map.put("fourth", 400);
        Set<String> set = map.keySet();
        System.out.println(set); // [fourth, first]

        List<String> keysList = new ArrayList<>(set);
        System.out.println(keysList); // [fourth, first]
        System.out.println("-----");

        // HashMap values in O(n)
        Collection<Integer> collection = map.values();
        System.out.println(collection); // [400, 1]

        List<Integer> valuesList = new ArrayList<>(collection);
        System.out.println(valuesList); // [400, 1]
        System.out.println("-----");

        // HashMap entrySet in O(n)
        Set<Map.Entry<String, Integer>> entrySet = map.entrySet();
        System.out.println(entrySet); // [fourth=400, first=1]
        System.out.println("-----");

        // HashMap traverse in O(n)
        HashMap<String, Integer> map2 = new HashMap<>();
        map2.put("A", 100);
        map2.put("B", 500);
        map2.put("C", 10);
        for (String key: map2.keySet()) {
            System.out.println("Key: " + key);
        }
        /*
        Key: A
        Key: B
        Key: C
        */

        for (Integer value: map2.values()) {
            System.out.println("Value: " + value);
        }
        /*
        Value: 100
        Value: 500
        Value: 10
        */

        for (Map.Entry<String, Integer> entry: map2.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println("Key: " + key + ", Value: " + value);
        }
        System.out.println("-----");
        /*
        Key: A, Value: 100
        Key: B, Value: 500
        Key: C, Value: 10
        */

        // HashMap getOrDefault in O(1) (avg)
        HashMap<String, Integer> map3 = new HashMap<>();
        map3.put("A", 95);
        map3.put("B", 89);
        int aScore = map3.getOrDefault("A", 0);
        System.out.println(aScore); // 95

        int cScore = map3.getOrDefault("C", 0);
        System.out.println(cScore); // 0
        System.out.println("-----");

        // HashMap compute in O(1) (avg)
        HashMap<String, Integer> map4 = new HashMap<>();
        map4.compute("A", (k, v) -> v == null ? 1 : v + 1);
        System.out.println(map4); // {A=1}

        map4.compute("A", (k, v) -> v == null ? 1 : v + 1);
        System.out.println(map4); // {A=2}

        map4.compute("B", (k, v) -> v == null ? 1 : v + 1);
        System.out.println(map4); // {A=2, B=1}
        System.out.println("-----");

        // HashMap computeIfAbsent in O(1) (avg)
        HashMap<String, List<String>> map5 = new HashMap<>();
        map5.computeIfAbsent("Interviewer", k -> new ArrayList<>()).add("Bob");
        System.out.println(map5); // {Interviewer=[Bob]}

        map5.computeIfAbsent("Manager", k -> new ArrayList<>()).add("Ada");
        map5.computeIfAbsent("Manager", k -> new ArrayList<>()).add("Cela");
        System.out.println(map5); // {Interviewer=[Bob], Manager=[Ada, Cela]}
        System.out.println("-----");

        // HashMap min or max in O(n)
        String maxKey = Collections.max(map2.keySet());
        System.out.println(maxKey); // C

        Integer minVal = Collections.min(map2.values());
        System.out.println(minVal); // 10

        Integer maxVal = null;
        String keyWithMaxVal = null;
        for (String key: map2.keySet()) {
            if (maxVal == null || map2.get(key) > maxVal) {
                maxVal = map2.get(key);
                keyWithMaxVal = key;
            }
        }
        System.out.println(maxVal); // 500
        System.out.println(keyWithMaxVal); // B
        System.out.println("-----");
    }
}

```

# HashSet
```Java
package HashSetSyntax;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) {

        // HashSet

        // HashSet init in O(1) or O(n)
        HashSet<Integer> set = new HashSet<>();
        System.out.println(set); // []
        System.out.println("-----");

        // HashSet add in O(1) (avg)
        boolean bool1 = set.add(100);
        System.out.println(bool1); // true

        boolean bool2 = set.add(500);
        System.out.println(bool2); // true
        System.out.println(set); // [100, 500]

        boolean bool3 = set.add(100);
        System.out.println(bool3); // false
        System.out.println(set); // [100, 500]
        System.out.println("-----");

        // HashSet contains in O(1) (avg)
        System.out.println(set.contains(100)); // true
        System.out.println(set.contains(3000)); // false
        System.out.println("-----");

        // HashSet remove in O(1) (avg)
        boolean bool4 = set.remove(500);
        System.out.println(bool4); // true

        boolean bool5 = set.remove(500);
        System.out.println(bool5); // false
        System.out.println(set); // [100]
        System.out.println("-----");

        // HashSet size in O(1)
        System.out.println(set.size()); // 1
        System.out.println(set.isEmpty()); // false
        System.out.println("-----");

        // HashSet traverse in O(n)
        HashSet<Integer> set2 = new HashSet<>(Arrays.asList(1, 3, 5, 10));
        for (Integer item: set2) {
            System.out.println(item);
        }
        System.out.println("-----");
        /*
        1
        3
        5
        10
        */

        // HashSet addAll in O(k)
        set2.addAll(Arrays.asList(5, 5, 5, 50, 100));
        System.out.println(set2); // [1, 50, 3, 100, 5, 10]
        System.out.println("-----");

        // HashSet min or max in O(n)
        Integer maxVal = Collections.max(set2);
        System.out.println(maxVal); // 100

        int minVal = Collections.min(set2);
        System.out.println(minVal); // 1
        System.out.println("-----");
    }
}

```

# PriorityQueue
```Java
package PriorityQueueSyntax;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) {

        // PriorityQueue

        // PriorityQueue init in O(1) or O(n)
        PriorityQueue<Integer> pq1 = new PriorityQueue<>(); // min heap
        PriorityQueue<Integer> pq2 = new PriorityQueue<>(Comparator.reverseOrder()); // max heap
        PriorityQueue<FreqWord> pq3 =
                new PriorityQueue<>((a, b) -> !a.freq().equals(b.freq()) ?
                        a.freq().compareTo(b.freq()) : a.content().compareTo(b.content()));
        PriorityQueue<int[]> pq4 = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0])); // max heap
        System.out.println(pq1); // []
        System.out.println("-----");

        // PriorityQueue peek in O(1)
        pq3.offer(new FreqWord("mango", 25));
        System.out.println(pq3.peek()); // FreqWord[content=mango, freq=25]

        pq3.offer(new FreqWord("pineapple", 10));
        System.out.println(pq3.peek()); // FreqWord[content=pineapple, freq=10]

        pq3.offer(new FreqWord("banana", 10));
        System.out.println(pq3.peek()); // FreqWord[content=banana, freq=10]

        pq3.offer(new FreqWord("apple", 5));
        System.out.println(pq3.peek()); // FreqWord[content=apple, freq=5]

        pq3.offer(new FreqWord("grape", 5));
        System.out.println(pq3.peek()); // FreqWord[content=apple, freq=5]
        System.out.println("-----");

        // PriorityQueue size in O(1)
        System.out.println(pq3.size()); // 5
        System.out.println(pq3.isEmpty()); // false
        System.out.println("-----");

        // PriorityQueue offer in O(logn)
        pq1.offer(100);
        pq1.offer(50);
        pq1.offer(200);
        System.out.println(pq1.peek()); // 50

        pq2.offer(100);
        pq2.offer(50);
        pq2.offer(200);
        System.out.println(pq2.peek()); // 200
        System.out.println("-----");

        // PriorityQueue poll in O(logn)
        System.out.println(pq1.size()); // 3
        Integer num = pq1.poll();
        System.out.println(num); // 50
        System.out.println(pq1.size()); // 2
        System.out.println(pq1.peek()); // 100
        System.out.println("-----");
    }
}

record FreqWord(String content, Integer freq) { }

```

# ArrayDeque
```Java
package ArrayDequeSyntax;

import java.util.ArrayDeque;

public class Main {

    public static void main(String[] args) {

        // ArrayDeque (as stack)
        // push/pop direction is opposite to Python's list (as stack)

        // ArrayDeque (as stack) init in O(1) or O(n)
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        System.out.println(stack); // []
        System.out.println("-----");

        // ArrayDeque (as stack) push in O(1) (in left)
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack); // [3, 2, 1]
        System.out.println("-----");

        // ArrayDeque (as stack) pop in O(1) (in left)
        Integer num1 = stack.pop();
        System.out.println(num1); // 3
        System.out.println(stack); // [2, 1]
        System.out.println("-----");

        // ArrayDeque (as stack) peek in O(1) (in left)
        Integer num2 = stack.peek();
        System.out.println(num2); // 2
        System.out.println(stack); // [2, 1]
        System.out.println("-----");

        // ArrayDeque (as stack) size in O(1)
        System.out.println(stack.size()); // 2
        System.out.println(stack.isEmpty()); // false
        System.out.println("-----");

        // ArrayDeque (as queue)
        // offer/poll direction is same as Python's deque (as queue)

        // ArrayDeque (as queue) init
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        ArrayDeque<int[]> queue2 = new ArrayDeque<>();
        ArrayDeque<Pair> queue3 = new ArrayDeque<>();
        System.out.println(queue); // []
        System.out.println("-----");

        // ArrayDeque (as queue) offer in O(1) (in right)
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        System.out.println(queue); // [1, 2, 3]
        System.out.println("-----");

        // ArrayDeque (as queue) poll in O(1) (in left)
        Integer num3 = queue.poll();
        System.out.println(num3); // 1
        System.out.println(queue); // [2, 3]
        System.out.println("-----");

        // ArrayDeque (as queue) peek (in left) and peekLast (in right) in O(1)
        Integer num4 = queue.peek();
        System.out.println(num4); // 2
        System.out.println(queue); // [2, 3]

        Integer num5 = queue.peekLast();
        System.out.println(num5); // 3
        System.out.println(queue); // [2, 3]
        System.out.println("-----");

        // ArrayDeque (as queue) size in O(1)
        System.out.println(queue.size()); // 2
        System.out.println(queue.isEmpty()); // false
        System.out.println("-----");
    }
}

class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

record Pair(TreeNode node, int level) { };

```

# String
```Java
package StringSyntax;

import java.util.Arrays;
import java.util.Objects;

public class Main {

    public static void main(String[] args) {

        // String and StringBuilder and StringBuffer

        // String: Immutable, thread-safe,
        // inefficient in scenarios requiring extensive modifications due to constant creation of new objects

        // StringBuilder: Mutable, not thread-safe,
        // efficient for single-threaded scenarios where lots of modifications are required

        // StringBuffer: Mutable, thread-safe,
        // suitable for multithreading scenarios but slower than StringBuilder due to synchronization

        // String length in O(1)
        String s = "Apple";
        System.out.println(s.length()); // 5
        System.out.println("-----");

        // String charAt in O(1)
        char letter = s.charAt(4);
        System.out.println(letter); // e
        System.out.println("-----");

        // String substring in O(n)
        // [a, b)
        System.out.println(s.substring(0, 2)); // Ap
        System.out.println("-----");

        // String contains, startsWith, endsWith in O(n)
        boolean bool1 = s.contains("pp");
        System.out.println(bool1); // true

        boolean bool2 = s.contains("zq");
        System.out.println(bool2); // false

        boolean bool3 = s.startsWith("Axp");
        System.out.println(bool3); // false

        boolean bool4 = s.endsWith("pple");
        System.out.println(bool4); // true
        System.out.println("-----");

        // String indexOf in O(n)
        System.out.println(s.indexOf("pl")); // 2
        System.out.println(s.indexOf("z")); // - 1
        System.out.println("-----");

        // String convert to char array in O(n)
        char[] arr = s.toCharArray();
        System.out.println(arr); // Apple
        System.out.println(arr[4]); // e
        System.out.println("-----");

        // String split in O(n)
        String sentence = "apple,banana,mango";
        String[] words = sentence.split(",");
        System.out.println(Arrays.toString(words)); // [apple, banana, mango]
        System.out.println("-----");

        // String equals, compareTo in O(n)
        String s1 = "apple";
        String s2 = "apple";
        String s3 = "banana";
        System.out.println(Objects.equals(s1, s2)); // true
        System.out.println(s1.compareTo(s2)); // 0
        System.out.println(s1.compareTo(s3)); // - 1
        System.out.println("-----");

        // String toUpperCase, toLowerCase in O(n)
        String upperS = s.toUpperCase();
        System.out.println(upperS); // APPLE

        String lowerS = s.toLowerCase();
        System.out.println(lowerS); // apple
        System.out.println("-----");

        // String strip in O(n)
        String beforeStrip = "   Polo. ";
        String afterStrip = beforeStrip.strip();
        System.out.println(afterStrip); // Polo.
        System.out.println("-----");

        // String replace in O(n)
        String beforeReplace = "Yolo";
        String afterReplace = beforeReplace.replace("o", "a");
        System.out.println(afterReplace); // Yala
        System.out.println("-----");

        // String concat in O(n)
        String s4 = "p" + "a" + "b";
        System.out.println(s4); // pab

        String s5 = "Hello".concat(" World").concat("!!");
        System.out.println(s5); // Hello World!!
        System.out.println("-----");

        // String from int in O(logn) (base 10) or O(1)
        int i = 1001;
        String iString = i + "";
        System.out.println(iString); // 1001
        System.out.println("-----");

        // String to int in O(n)
        int intFromString = Integer.parseInt(iString);
        System.out.println(intFromString); // 1001
        System.out.println("-----");

        // char from int in O(1)
        int asciiForA = 65;
        char charA = (char) asciiForA;
        System.out.println(charA); // A
        System.out.println("-----");

        // char to int in O(1)
        char charZ = 'Z';
        int asciiForZ = charZ + 0;
        System.out.println(asciiForZ); // 90
        System.out.println("-----");

        // char to String in O(1)
        String stringZ = charZ + "";
        System.out.println(stringZ); // Z
        System.out.println("-----");

        // char related methods
        char c1 = 'a';
        char c2 = 'A';
        char c3 = '5';
        System.out.println(Character.isLowerCase(c1)); // true
        System.out.println(Character.toLowerCase(c2)); // a
        System.out.println(Character.isUpperCase(c2)); // true
        System.out.println(Character.toUpperCase(c1)); // A
        System.out.println(Character.isLetter(c1)); // true
        System.out.println(Character.isDigit(c3)); // true
        System.out.println(Character.isLetterOrDigit(c3)); // true

        String sFromChar = Character.toString(c3);
        System.out.println(sFromChar); // 5
        System.out.println("-----");

        // StringBuilder related methods
        StringBuilder sb1 = new StringBuilder();
        sb1.append("f");
        sb1.append("c");
        String s6 = sb1.toString();
        System.out.println(s6); // fc

        StringBuilder sb2 = new StringBuilder(s);
        sb2.append("f");
        String s7 = sb2.reverse().toString();
        System.out.println(s7); // felppA
        System.out.println("-----");

        // StringBuffer related methods
        // toString, O(n)
        // append, O(L)
        // insert, O(n)
        // delete, O(n)
        // replace, O(n+L)
        // reverse, O(n)
        // charAt, O(1)
        // deleteCharAt, O(n), and O(1) for last idx
        // length, O(1)

        StringBuffer sbf = new StringBuffer("Hello");
        sbf.append(" World");
        String s8 = sbf.toString();
        System.out.println(s8); // Hello World

        StringBuffer sbf2 = new StringBuffer("Hello");
        sbf2.insert(2, "WWW");
        String s9 = sbf2.toString();
        System.out.println(s9); // HeWWWllo

        StringBuffer sbf3 = new StringBuffer("HelloWorld");
        sbf3.delete(5, 10);
        String s10 = sbf3.toString();
        System.out.println(s10); // Hello

        StringBuffer sbf4 = new StringBuffer("HelloWorld");
        sbf4.replace(5, 10, " Friend");
        String s11 = sbf4.toString();
        System.out.println(s11); // Hello Friend

        StringBuffer sbf5 = new StringBuffer("Hello");
        sbf5.reverse();
        String s12 = sbf5.toString();
        System.out.println(s12); // olleH

        Character c = sbf5.charAt(3);
        System.out.println(c); // e

        sbf5.deleteCharAt(3);
        String s13 = sbf5.toString();
        System.out.println(s13); // ollH

        System.out.println(sbf5.length()); // 4
        System.out.println("-----");
    }
}

```

# TreeMap
```Java
package TreeMapSyntax;

import java.util.Collection;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) {

        // TreeMap

        // TreeMap init in O(1) or O(n)
        TreeMap<String, Integer> treeMap1 = new TreeMap<>();
        System.out.println(treeMap1); // {}
        System.out.println("-----");

        // TreeMap size in O(1)
        System.out.println(treeMap1.size()); // 0
        System.out.println(treeMap1.isEmpty()); // true
        System.out.println("-----");

        // TreeMap put in O(logn)
        treeMap1.put("apple", 10);
        treeMap1.put("banana", 30);
        System.out.println(treeMap1); // {apple=10, banana=30}

        treeMap1.put("banana", 45);
        System.out.println(treeMap1); // {apple=10, banana=45}
        System.out.println("-----");

        // TreeMap get in O(logn)
        System.out.println(treeMap1.get("apple")); // 10
        System.out.println(treeMap1.get("mango")); // null
        System.out.println("-----");

        // TreeMap containsKey in O(logn)
        System.out.println(treeMap1.containsKey("apple")); // true
        System.out.println(treeMap1.containsKey("mango")); // false
        System.out.println("-----");

        // TreeMap delete in O(logn)
        Integer val1 = treeMap1.remove("banana");
        System.out.println(val1); // 45

        Integer val2 = treeMap1.remove("banana");
        System.out.println(val2); // null
        System.out.println(treeMap1); // {apple=10}
        System.out.println("-----");

        // TreeMap firstKey in O(logn)
        TreeMap<Integer, String> treeMap2 = new TreeMap<>();
        treeMap2.put(100, "apple");
        treeMap2.put(500, "banana");
        treeMap2.put(300, "mango");
        System.out.println(treeMap2); // {100=apple, 300=mango, 500=banana}
        System.out.println(treeMap2.firstKey()); // 100
        System.out.println("-----");

        // TreeMap lastKey in O(logn)
        System.out.println(treeMap2.lastKey()); // 500
        System.out.println("-----");

        // TreeMap ceilingKey in O(logn)
        System.out.println(treeMap2.ceilingKey(400)); // 500
        System.out.println(treeMap2.ceilingKey(500)); // 500
        System.out.println(treeMap2.ceilingKey(600)); // null
        System.out.println("-----");

        // TreeMap floorKey in O(logn)
        System.out.println(treeMap2.floorKey(200)); // 100
        System.out.println(treeMap2.floorKey(100)); // 100
        System.out.println(treeMap2.floorKey(50)); // null
        System.out.println("-----");

        // TreeMap lowerKey in O(logn)
        System.out.println(treeMap2.lowerKey(200)); // 100
        System.out.println(treeMap2.lowerKey(100)); // null
        System.out.println(treeMap2.lowerKey(50)); // null
        System.out.println("-----");

        // TreeMap higherKey in O(logn)
        System.out.println(treeMap2.higherKey(400)); // 500
        System.out.println(treeMap2.higherKey(500)); // null
        System.out.println(treeMap2.higherKey(600)); // null
        System.out.println("-----");

        // TreeMap keySet in O(n)
        Set<Integer> set = treeMap2.keySet();
        System.out.println(set); // [100, 300, 500]
        System.out.println("-----");

        // TreeMap values in O(n)
        Collection<String> collection = treeMap2.values();
        System.out.println(collection); // [apple, mango, banana]
        System.out.println("-----");

        // TreeMap entrySet in O(n)
        Set<Map.Entry<Integer, String>> entrySet = treeMap2.entrySet();
        System.out.println(entrySet); // [100=apple, 300=mango, 500=banana]
        System.out.println("-----");

        // TreeMap traverse in O(n)
        for (Integer key: treeMap2.keySet()) {
            System.out.println("Key: " + key);
        }
        /*
        Key: 100
        Key: 300
        Key: 500
        */

        for (String value: treeMap2.values()) {
            System.out.println("Value: " + value);
        }
        /*
        Value: apple
        Value: mango
        Value: banana
         */

        for (Map.Entry<Integer, String> entry: treeMap2.entrySet()) {
            Integer key = entry.getKey();
            String value = entry.getValue();
            System.out.println("Key: " + key + ", Value: " + value);
        }
        System.out.println("-----");
        /*
        Key: 100, Value: apple
        Key: 300, Value: mango
        Key: 500, Value: banana
         */
    }
}

```

# Number
```Java
package NumberSyntax;

import java.util.Objects;
import java.util.Random;

public class Main {

    public static void main(String[] args) {

        // Number

        // abs, floor, ceil
        int neg = - 100;
        int pos = Math.abs(neg);
        System.out.println(pos); // 100

        double floorVal = 2.8;
        int intVal = (int) Math.floor(floorVal);
        System.out.println(intVal); // 2

        double ceilVal = 2.1;
        int intVal2 = (int) Math.ceil(ceilVal);
        System.out.println(intVal2); // 3
        System.out.println("-----");

        // min and max
        int max1 = Integer.MAX_VALUE;
        Integer min1 = Integer.MIN_VALUE;
        System.out.println(max1); // 2147483647 (2**31 - 1)
        System.out.println(min1); // -2147483648 (- 2**31)

        long max2 = Long.MAX_VALUE;
        Long min2 = Long.MIN_VALUE;
        System.out.println(max2); // 9223372036854775807 (2**63 - 1)
        System.out.println(min2); // -9223372036854775808 (- 2**63)

        System.out.println(Math.max(1, 2)); // 2
        System.out.println(Math.min(1, 5)); // 1
        System.out.println("-----");

        // division
        int num1 = 80;
        int num2 = 7;
        System.out.println(num1 / num2); // 11
        System.out.println(num1 % num2); // 3
        int num3 = - 10;
        int num4 = 7;
        int num5 = 17;
        System.out.println(num3 / num4); // - 1, truncate toward zero
        System.out.println(num3 / num5); // 0, truncate toward zero
        System.out.println(num3 % num4); // - 3
        System.out.println(num3 % num5); // - 10
        System.out.println("-----");

        // random
        // [a, b]
        int a = 2;
        int b = 5;
        Random random = new Random();
        int randomInt = random.nextInt(b - a + 1) + a;
        System.out.println(randomInt); // 2 or 3 or 4 or 5
        System.out.println("-----");

        // pow
        int base = 11;
        double res = Math.pow(base, 3);
        System.out.println(res); // 1331.0

        int intRes = (int) res;
        System.out.println(intRes); // 1331
        System.out.println("-----");

        // swap
        int first = 100;
        int second = 200;
        int temp = first;
        first = second;
        second = temp;
        System.out.println(first); // 200
        System.out.println(second); // 100
        System.out.println("-----");

        // compare (focus on val)
        /*
        01. int x, int y. use:
            x == y
            x != y
            x > y
            x < y
            x >= y
            x <= y
            Integer.compare(x, y)

        02. char x, char y. use:
            x == y
            x != y
            x > y
            x < y
            x >= y
            x <= y
            Character.compare(x, y)

        03. int x, Integer y. use:
            Objects.equals(x, y)
            x > y (notice: not null-safe)
            x < y (notice: not null-safe)
            x >= y (notice: not null-safe)
            x <= y (notice: not null-safe)

        04. char x, Character y. use:
            Objects.equals(x, y)
            x > y (notice: not null-safe)
            x < y (notice: not null-safe)
            x >= y (notice: not null-safe)
            x <= y (notice: not null-safe)

        05. Integer x, Integer y. use:
            Objects.equals(x, y)
            x > y (notice: not null-safe)
            x < y (notice: not null-safe)
            x >= y (notice: not null-safe)
            x <= y (notice: not null-safe)
            x.compareTo(y) (notice: not null-safe)

        06. Character x, Character y. use:
            Objects.equals(x, y)
            x > y (notice: not null-safe)
            x < y (notice: not null-safe)
            x >= y (notice: not null-safe)
            x <= y (notice: not null-safe)
            x.compareTo(y) (notice: not null-safe)

        07. String x, String y. use:
            Objects.equals(x, y)
            x.compareTo(y) (notice: not null-safe)
        */
    }
}

```

# **C#**

# Array
```csharp
// T[]

// arr init in O(1) or O(n)
int[] intArr = new int[5];
Console.WriteLine(string.Join(", ", intArr)); // 0, 0, 0, 0, 0

long[] longArr = new long[5];
Console.WriteLine(string.Join(", ", longArr)); // 0, 0, 0, 0, 0

char[] charArr = new char[5];
Console.WriteLine(string.Join(", ", charArr)); // , , , , 
Console.WriteLine(charArr[0] == '\u0000'); // True

int[] intArr2 = [9, 3, 2, 100, 4];
Console.WriteLine(string.Join(", ", intArr2)); // 9, 3, 2, 100, 4

// arr[idx] = val (set) in O(1)
intArr[2] = 100;
Console.WriteLine(string.Join(", ", intArr)); // 0, 0, 100, 0, 0
Console.WriteLine("-----");

// arr[idx] (get) in O(1)
int ele = intArr[2];
Console.WriteLine(ele); // 100
Console.WriteLine("-----");

// arr.Length in O(1)
int size = intArr.Length;
Console.WriteLine(size); // 5
Console.WriteLine("-----");

// arr traverse in O(n)
for (int i = 0; i < intArr2.Length; i++)
{
    Console.Write($"{i}: {intArr2[i]}, ");
}
Console.WriteLine(); // 0: 9, 1: 3, 2: 2, 3: 100, 4: 4, 

foreach (var num in intArr2)
{
    Console.Write($"{num}, ");
}
Console.WriteLine(); // 9, 3, 2, 100, 4, 
Console.WriteLine("-----");

// arr 2D/jagged in O(RC)
int rows = 5;
int cols = 3;
int[,] twoDArray = new int[rows, cols];
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < cols; j++)
    {
        twoDArray[i, j] = i * cols + j;
    }
}
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < cols; j++)
    {
        Console.Write(twoDArray[i, j] + " ");
    }
    Console.WriteLine();
}
Console.WriteLine(twoDArray.GetLength(0)); // 5
Console.WriteLine(twoDArray.GetLength(1)); // 3
/*
0 1 2 
3 4 5 
6 7 8 
9 10 11 
12 13 14
*/

// jagged array is better choice if need sorting, but should manually init second dimension
int[][] jaggedArray = new int[rows][];
for (int i = 0; i < rows; i++)
{
    jaggedArray[i] = new int[cols];
    for (int j = 0; j < cols; j++)
    {
        jaggedArray[i][j] = i * cols + j;
    }
}
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < cols; j++)
    {
        Console.Write(jaggedArray[i][j] + " ");
    }
    Console.WriteLine();
}
Console.WriteLine(jaggedArray.Length); // 5
Console.WriteLine(jaggedArray[0].Length); // 3
Console.WriteLine("-----");
/*
0 1 2 
3 4 5 
6 7 8 
9 10 11 
12 13 14 
*/

// Array.Sort(arr)
// c# use introsort algorithm
// time O(nlogn)
// space O(logn)
// mainly like quicksort
// or if size <= 16, use insertion sort instead
// or if recursion stack too deep, use heap sort instead
Array.Sort(intArr2);
Console.WriteLine(string.Join(", ", intArr2)); // 2, 3, 4, 9, 100

string[] stringArr = ["banana", "cucumber", "apple"];
Array.Sort(stringArr, (x, y) => x.Length.CompareTo(y.Length));
Console.WriteLine(string.Join(", ", stringArr)); // apple, banana, cucumber

int[][] intervals = [[1, 3], [1, 2], [0, 0], [4, 5]];
Array.Sort(intervals, (x, y) => x[0] == y[0] ? x[1].CompareTo(y[1]) : x[0].CompareTo(y[0]));
for (int i = 0; i < intervals.Length; i++)
{
    Console.WriteLine($"[{intervals[i][0]}, {intervals[i][1]}]");
}
Console.WriteLine("-----");
/*
[0, 0]
[1, 2]
[1, 3]
[4, 5]
*/

// Array.Reverse(arr) in O(n)
Array.Reverse(intArr2);
Console.WriteLine(string.Join(", ", intArr2)); // 100, 9, 4, 3, 2
Console.WriteLine("-----");

// arr.ToList() in O(n)
int[] oldArr = [1, 5, 2];
List<int> newList = oldArr.ToList();
Console.WriteLine(string.Join(", ", newList)); // 1, 5, 2
Console.WriteLine("-----");

// arr.Skip(idx).Take(count).ToArray() (get subarray) in O(n)
string[] stringArr2 = ["H", "A", "L", "I", "P", "Z"];
string[] subStringArr2 = stringArr2.Skip(1).Take(3).ToArray();
Console.WriteLine(string.Join(", ", subStringArr2)); // A, L, I

string[] subStringArr3 = stringArr2.ToArray();
Console.WriteLine(string.Join(", ", subStringArr3)); // H, A, L, I, P, Z
Console.WriteLine("-----");

// arr.Min() or arr.Max() in O(n)
char[] charArr2 = ['H', 'Z', 'X', 'B'];
char minChar = charArr2.Min();
char maxChar = charArr2.Max();
Console.WriteLine(minChar); // B
Console.WriteLine(maxChar); // Z
Console.WriteLine("-----");

```

# List
```csharp
// List<T>

// list init in O(1) or O(n)
List<int> list1 = [];
List<int[]> listOfArr = [];
Console.WriteLine("-----");

// list.Add(val) in O(1) (avg)
list1.Add(5);
list1.Add(8);
list1.Add(20);
Console.WriteLine(string.Join(", ", list1)); // 5, 8, 20
Console.WriteLine("-----");

// list[idx] (get) in O(1)
int val = list1[0];
Console.WriteLine(val); // 5
Console.WriteLine("-----");

// list.Count in O(1)
int size = list1.Count;
Console.WriteLine(size); // 3
Console.WriteLine("-----");

// list.RemoveAt(lastIdx) in O(1), other idx is O(n)
List<int> listForRemove = [1, 2, 3];
listForRemove.RemoveAt(listForRemove.Count - 1);
Console.WriteLine(string.Join(", ", listForRemove)); // 1, 2
Console.WriteLine("-----");

// list[idx] = val (set) in O(1)
list1[2] = 99;
Console.WriteLine(string.Join(", ", list1)); // 5, 8, 99
Console.WriteLine("-----");

// list.Insert(idx, val) in O(n)
list1.Insert(0, 100);
Console.WriteLine(string.Join(", ", list1)); // 100, 5, 8, 99
Console.WriteLine("-----");

// list.Sort() in O(nlogn)
list1.Sort();
Console.WriteLine(string.Join(", ", list1)); // 5, 8, 99, 100

list1.Sort((x, y) => y.CompareTo(x));
Console.WriteLine(string.Join(", ", list1)); // 100, 99, 8, 5
Console.WriteLine("-----");

// list.ToArray() in O(n)
List<string> list2 = ["A", "B", "C"];
string[] array = list2.ToArray();
Console.WriteLine(string.Join(", ", array)); // A, B, C
Console.WriteLine("-----");

// list.Reverse() in O(n)
list2.Reverse();
Console.WriteLine(string.Join(", ", list2)); // C, B, A
Console.WriteLine("-----");

// list traverse in O(n)
List<string> list3 = ["Item1", "Item2", "Item3"];
for (int i = 0; i < list3.Count; i++)
{
    string item = list3[i];
    Console.WriteLine($"for: {item}");
}
/*
for: Item1
for: Item2
for: Item3
*/

foreach (var item in list3)
{
    Console.WriteLine($"foreach: {item}");
}
Console.WriteLine("-----");
/*
foreach: Item1
foreach: Item2
foreach: Item3
*/

// list 2D in O(RC)
List<List<int>> matrix = [];
int rows = 3;
int cols = 5;
for (int r = 0; r < rows; r++)
{
    List<int> innerList = [];
    for (int c = 0; c < cols; c++)
    {
        innerList.Add(0);
    }
    matrix.Add(innerList);
}
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < cols; j++)
    {
        Console.Write(matrix[i][j] + " ");
    }
    Console.WriteLine();
}
Console.WriteLine("-----");
/*
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
*/

// list.Skip(idx).Take(count).ToList() (get sublist) in O(n)
List<string> subList3 = list3.Skip(1).Take(2).ToList();
Console.WriteLine(string.Join(", ", subList3)); // Item2, Item3

List<string> subList4 = list3.ToList();
Console.WriteLine(string.Join(", ", subList4)); // Item1, Item2, Item3
Console.WriteLine("-----");

// list.AddRange(collection) in O(k)
subList3.AddRange(["newItem1", "newItem2"]);
Console.WriteLine(string.Join(", ", subList3)); // Item2, Item3, newItem1, newItem2
Console.WriteLine("-----");

// list.Min() or arr.Max() in O(n)
List<char> list4 = ['H', 'Z', 'X', 'A'];
char minChar = list4.Min();
char maxChar = list4.Max();
Console.WriteLine(minChar); // A
Console.WriteLine(maxChar); // Z
Console.WriteLine("-----");

```

# Dictionary
```csharp
// Dictionary<TKey, TValue>

// dict init in O(1) or O(n)
Dictionary<string, int> map = [];
Console.WriteLine("-----");

// dict[key] = val (add) in O(1) (avg)
map["first"] = 1;
map["second"] = 2;
Console.WriteLine(string.Join(", ", map)); // [first, 1], [second, 2]
Console.WriteLine("-----");

// dict[key] = value (update) in O(1) (avg)
map["second"] = 50;
Console.WriteLine(string.Join(", ", map)); // [first, 1], [second, 50]
Console.WriteLine("-----");

// dict[key] (get) in O(1) (avg)
int key = map["first"];
Console.WriteLine(key); // 1
Console.WriteLine("-----");

// dict.ContainsKey(key) in O(1) (avg)
bool exist = map.ContainsKey("second");
bool exist2 = map.ContainsKey("nonkey");
Console.WriteLine(exist); // True
Console.WriteLine(exist2); // False
Console.WriteLine("-----");

// dict.Remove(key) in O(1) (avg)
bool removeSucc = map.Remove("second");
bool removeSucc2 = map.Remove("nonkey");
Console.WriteLine(removeSucc); // True
Console.WriteLine(removeSucc2); // False
Console.WriteLine(string.Join(", ", map)); // [first, 1]
Console.WriteLine("-----");

// dict.Count in O(1)
int count = map.Count;
Console.WriteLine(count); // 1
Console.WriteLine("-----");

// dict.Keys in O(n)
map["third"] = 999;
var keys = map.Keys;
Console.WriteLine(string.Join(", ", keys)); // first, third

List<string> keysList = keys.ToList();
Console.WriteLine(string.Join(", ", keysList)); // first, third
Console.WriteLine("-----");

// dict.Values in O(n)
var values = map.Values;
Console.WriteLine(string.Join(", ", values)); // 1, 999

List<int> valuesList = values.ToList();
Console.WriteLine(string.Join(", ", valuesList)); // 1, 999
Console.WriteLine("-----");

// dict traverse in O(n)
Dictionary<string, int> map2 = [];
map2["A"] = 100;
map2["B"] = 500;
map2["C"] = 10;
foreach (var k in map2.Keys)
{
    Console.WriteLine($"Key: {k}");
}
/*
Key: A
Key: B
Key: C
*/
foreach (var v in map2.Values)
{
    Console.WriteLine($"Value: {v}");
}
/*
Value: 100
Value: 500
Value: 10
*/
foreach (var pair in map2)
{
    string k = pair.Key;
    int v = pair.Value;
    Console.WriteLine($"Key: {k}, Value: {v}");
}
Console.WriteLine("-----");
/*
Key: A, Value: 100
Key: B, Value: 500
Key: C, Value: 10
*/

// dict.Min() or dict.Max() or dict.MaxBy() in O(n)
string? minKey = map2.Keys.Min();
Console.WriteLine(minKey); // A
int maxValue = map2.Values.Max();
Console.WriteLine(maxValue); // 500
string keyWithMaxValue = map2.MaxBy(pair => pair.Value).Key;
Console.WriteLine(keyWithMaxValue); // B
Console.WriteLine("-----");

```

# HashSet
```csharp
// HashSet<T>

// set init in O(1) or O(n)
HashSet<int> set = [];
Console.WriteLine("-----");

// set.Add(val) in O(1) (avg)
bool addSucc = set.Add(5);
Console.WriteLine(addSucc); //True

bool addSucc2 = set.Add(5);
Console.WriteLine(addSucc2); // False

set.Add(10);
Console.WriteLine(string.Join(", ", set)); // 5, 10
Console.WriteLine("-----");

// set.Contains(val) in O(1) (avg)
bool contain = set.Contains(100);
Console.WriteLine(contain); // False

bool contain2 = set.Contains(10);
Console.WriteLine(contain2); // True
Console.WriteLine("-----");

// set.Remove(val) in O(1) (avg)
bool removeSucc = set.Remove(100);
Console.WriteLine(removeSucc); // False

bool removeSucc2 = set.Remove(10);
Console.WriteLine(removeSucc2); // True
Console.WriteLine(string.Join(", ", set)); // 5
Console.WriteLine("-----");

// set.Count in O(1)
int count = set.Count;
Console.WriteLine(count); // 1
Console.WriteLine("-----");

// set traverse in O(n)
set.Add(80);
set.Add(95);
foreach (var val in set)
{
    Console.Write($"{val}, ");
}
Console.WriteLine(); // 5, 80, 95, 
Console.WriteLine("-----");

// set.UnionWith(collection) in O(k)
set.UnionWith([5, 80, 80, 80, 80, 80, 80, 81, 82]);
Console.WriteLine(string.Join(", ", set)); // 5, 80, 95, 81, 82
Console.WriteLine("-----");

// set.Min() or set.Max() in O(n)
int min = set.Min();
int max = set.Max();
Console.WriteLine(min); // 5
Console.WriteLine(max); // 95
Console.WriteLine("-----");

```

# PriorityQueue
```csharp
// PriorityQueue<TElement, TPriority>

// heap init in O(1) or O(nlogn), no builtin heapify to achieve O(n)
int[] arr = [1, 2, 3, 4, 8, 200];
PriorityQueue<int, int> minHeap = new();
foreach (var val in arr)
{
    minHeap.Enqueue(val, val);
}
PriorityQueue<int, int> maxHeap = new();
foreach (var val in arr)
{
    maxHeap.Enqueue(val, -val);
}
PriorityQueue<(string, int), (string, int)> heapWithComparer =
    new(Comparer<(string, int)>.Create((x, y) => x.Item2 == y.Item2 ? x.Item1.CompareTo(y.Item1) : x.Item2.CompareTo(y.Item2)));
Console.WriteLine("-----");

// heap.Peek() in O(1)
int topElement = minHeap.Peek();
Console.WriteLine(topElement); // 1

int topElement2 = maxHeap.Peek();
Console.WriteLine(topElement2); // 200

heapWithComparer.Enqueue(("mango", 25), ("mango", 25));
Console.WriteLine(heapWithComparer.Peek()); // (mango, 25)

heapWithComparer.Enqueue(("pineapple", 10), ("pineapple", 10));
Console.WriteLine(heapWithComparer.Peek()); // (pineapple, 10)

heapWithComparer.Enqueue(("banana", 10), ("banana", 10));
Console.WriteLine(heapWithComparer.Peek()); // (banana, 10)

heapWithComparer.Enqueue(("apple", 5), ("apple", 5));
Console.WriteLine(heapWithComparer.Peek()); // (apple, 5)

heapWithComparer.Enqueue(("grape", 5), ("grape", 5));
Console.WriteLine(heapWithComparer.Peek()); // (apple, 5)
Console.WriteLine("-----");

// heap.Count in O(1)
int count = heapWithComparer.Count;
Console.WriteLine(count); // 5
Console.WriteLine("-----");

// heap.Enqueue(val, priority) in O(logn)
minHeap.Enqueue(-50, -50);
Console.WriteLine(minHeap.Peek()); // -50
Console.WriteLine("-----");

// heap.Dequeue() in O(logn)
int ele = minHeap.Dequeue();
Console.WriteLine(ele); // -50
Console.WriteLine(minHeap.Peek()); // 1
Console.WriteLine("-----");

```

# Stack
```csharp
// Stack<T>

// stack init in O(1)
// Push/Pop direction is opposite to Python's list (as stack)
Stack<int> stack = [];
Console.WriteLine("-----");

// stack.Push(val) in O(1)
stack.Push(100);
stack.Push(30);
stack.Push(66);
Console.WriteLine(string.Join(", ", stack)); // 66, 30, 100
Console.WriteLine("-----");

// stack.Pop() in O(1)
int val = stack.Pop();
Console.WriteLine(val); // 66
Console.WriteLine(string.Join(", ", stack)); // 30, 100
Console.WriteLine("-----");

// stack.Peek() in O(1)
int top = stack.Peek();
Console.WriteLine(top); // 30
Console.WriteLine("-----");

// stack.Count in O(1)
int count = stack.Count;
Console.WriteLine(count); // 2
Console.WriteLine("-----");

```

# Queue
```csharp
// Queue<T>

// queue init in O(1)
// Enqueue/Dequeue direction is same as Python's deque (as queue)
Queue<int> queue = [];
Console.WriteLine("-----");

// queue.Enqueue(val) in O(1)
queue.Enqueue(100);
queue.Enqueue(30);
queue.Enqueue(66);
Console.WriteLine(string.Join(", ", queue)); // 100, 30, 66
Console.WriteLine("-----");

// queue.Dequeue() in O(1)
int val = queue.Dequeue();
Console.WriteLine(val); // 100
Console.WriteLine(string.Join(", ", queue)); // 30, 66
Console.WriteLine("-----");

// queue.Peek() in O(1)
int oldest = queue.Peek();
Console.WriteLine(oldest); // 30
Console.WriteLine("-----");

// queue.Count in O(1)
int count = queue.Count;
Console.WriteLine(count); // 2
Console.WriteLine("-----");

```

# LinkedList (use as Deque)
```csharp
// LinkedList<T>

// deque init in O(1)
LinkedList<int> deque = [];
Console.WriteLine("-----");

// deque.AddLast(val) or deque.AddFirst(val) in O(1)
deque.AddLast(100);
deque.AddLast(30);
deque.AddLast(66);
Console.WriteLine(string.Join(", ", deque)); // 100, 30, 66
Console.WriteLine("-----");

// deque.RemoveFirst() or deque.RemoveLast() in O(1)
deque.RemoveFirst();
Console.WriteLine(string.Join(", ", deque)); // 30, 66
Console.WriteLine("-----");

// deque.First.Value or deque.Last.Value in O(1)
int oldest = deque.First.Value;
int newest = deque.Last.Value;
Console.WriteLine(oldest); // 30
Console.WriteLine(newest); // 66
Console.WriteLine("-----");

// deque.Count in O(1)
int count = deque.Count;
Console.WriteLine(count); // 2
Console.WriteLine("-----");

```

# string
```csharp
// string

// string: immutable
// StringBuilder: mutable

using System.Text;  // For StringBuilder

// str.Length in O(1)
string s = "Apple";
int len = s.Length;
Console.WriteLine(len); // 5
Console.WriteLine("-----");

// str[idx] (get) in O(1)
char letter = s[4];
Console.WriteLine(letter); // e
Console.WriteLine("-----");

// str.Substring(idx, count) or str.Substring(idx) in O(n)
string substr = s.Substring(1, 2);
Console.WriteLine(substr); // pp
Console.WriteLine("-----");

// str.Contains(val), str.StartsWith(val), str.EndsWith(val) in O(n)
bool bool1 = s.Contains("pp");
Console.WriteLine(bool1); // True

bool bool2 = s.StartsWith("zq");
Console.WriteLine(bool2); // False

bool bool3 = s.EndsWith("pple");
Console.WriteLine(bool3); // True
Console.WriteLine("-----");

// str.IndexOf(val) in O(n)
int idx1 = s.IndexOf("pl");
Console.WriteLine(idx1); // 2

int idx2 = s.IndexOf("z");
Console.WriteLine(idx2); // -1
Console.WriteLine("-----");

// str.toArry() in O(n)
char[] arr = s.ToArray();
Console.WriteLine(string.Join(", ", arr)); // A, p, p, l, e
char c = arr[0];
Console.WriteLine(c); // A
string sFromChars = string.Join("", arr);
Console.WriteLine(sFromChars); // Apple
Console.WriteLine("-----");

// str.Split(delimiter) in O(n)
string sentence = "apple,banana,mango";
string[] words = sentence.Split(",");
Console.WriteLine(string.Join(", ", words)); // apple, banana, mango
Console.WriteLine("-----");

// s1 == s2, s1.CompareTo(s2) in O(n)
string s1 = "apple";
string s2 = "apple";
string s3 = "banana";
bool bool4 = s1 == s2;
Console.WriteLine(bool4); // True

int compare1 = s1.CompareTo(s2);
Console.WriteLine(compare1); // 0

int compare2 = s1.CompareTo(s3);
Console.WriteLine(compare2); // -1
Console.WriteLine("-----");

// str.ToUpper(), str.ToLower() in O(n)
string s4 = s1.ToUpper();
Console.WriteLine(s4); //APPLE

string s5 = s4.ToLower();
Console.WriteLine(s5); // apple
Console.WriteLine("-----");

// str.Trim() in O(n)
string beforeStrip = "   Polo. ";
string afterStrip = beforeStrip.Trim();
Console.WriteLine(afterStrip); // Polo.
Console.WriteLine("-----");

// str.Replace(old, new) in O(n)
string beforeReplace = "Yolo";
string afterReplace = beforeReplace.Replace("o", "a");
Console.WriteLine(afterReplace); // Yala
Console.WriteLine("-----");

// str from int in O(L)
int i = 1001;
string iString = i.ToString();
Console.WriteLine(iString); // 1001
Console.WriteLine("-----");

// int.Parse(str) (str to int) in O(L)
int j = int.Parse("2020");
Console.WriteLine(j); // 2020
Console.WriteLine("-----");

// char from int in O(1)
int asciiForA = 65;
char a = (char)asciiForA;
Console.WriteLine(a); // A
Console.WriteLine("-----");

// char to int in O(1)
char z = 'Z';
int asciiForZ = z;
Console.WriteLine(asciiForZ); // 90
Console.WriteLine("-----");

// char related methods
char c1 = 'a';
char c2 = 'A';
char c3 = '5';
Console.WriteLine(char.IsLower(c1)); // True
Console.WriteLine(char.ToLower(c2)); // a
Console.WriteLine(char.IsUpper(c2)); // True
Console.WriteLine(char.ToUpper(c1)); // A
Console.WriteLine(char.IsLetter(c1)); // True
Console.WriteLine(char.IsDigit(c3)); // True
Console.WriteLine(char.IsLetterOrDigit(c3)); // True
Console.WriteLine(c3.ToString()); // 5
Console.WriteLine("-----");

// sb init in O(1) or O(n)
StringBuilder sb = new();
Console.WriteLine("-----");

// sb.Append(str) in O(L)
sb.Append("appppple");
sb.Append("ZX");
sb.Append('q');
Console.WriteLine(sb); // apppppleZXq
Console.WriteLine("-----");

// sb.Remove(idx, count) in O(n)
sb.Remove(1, 5);
Console.WriteLine(sb); // aleZXq
Console.WriteLine("-----");

// sb[idx] (get) in O(1)
char c4 = sb[4];
Console.WriteLine(c4); // X
Console.WriteLine("-----");

// sb.Length in O(1)
int count = sb.Length;
Console.WriteLine(count); // 6
Console.WriteLine("-----");

// sb.ToString() in O(n)
string s6 = sb.ToString();
Console.WriteLine(s6); // aleZXq
Console.WriteLine("-----");

```

# number
```csharp
// number

// Math related method
Math.Max(5, 10); // 10
Math.Min(5, 10); // 5
Math.Sign(-10); // - 1

double d0 = Math.Abs(-4.7);
Console.WriteLine(d0); // 4.7

double d1 = Math.Pow(2, 3);
Console.WriteLine(d1); // 8
double d2 = Math.Sqrt(64);
Console.WriteLine(d2); // 8

double d3 = Math.Floor(9.99);
Console.WriteLine(d3); // 9
double d4 = Math.Floor(-9.99);
Console.WriteLine(d4); // -10

double d5 = Math.Truncate(9.99);
Console.WriteLine(d5); // 9
double d6 = Math.Truncate(-9.99);
Console.WriteLine(d6); // -9

double d7 = Math.Ceiling(9.01);
Console.WriteLine(d7); // 10
double d8 = Math.Ceiling(-9.01);
Console.WriteLine(d8); // -9

double d9 = Math.Round(9.015, 2);
Console.WriteLine(d9); // 9.02
double d10 = Math.Round(-9.014, 2);
Console.WriteLine(d10); // -9.01
Console.WriteLine("-----");

// MaxValue and MinValue
int max1 = int.MaxValue;
int min1 = int.MinValue;
Console.WriteLine(max1); // 2147483647
Console.WriteLine(min1); // -2147483648
Console.WriteLine("-----");

// division
int num1 = 80;
int num2 = 7;
Console.WriteLine(num1 / num2); // 11
Console.WriteLine(num1 % num2); // 3
int num3 = -10;
int num4 = 7;
int num5 = 17;
Console.WriteLine(num3 / num4); // -1, truncate toward zero
Console.WriteLine(num3 / num5); // 0, truncate toward zero
Console.WriteLine(num3 % num4); // -3
Console.WriteLine(num3 % num5); // -10
Console.WriteLine("-----");

// random.Next(include, exclude)
// [a, b)
int a = 2;
int b = 5;
Random random = new();
int randomInt = random.Next(a, b);
Console.WriteLine(randomInt); // 2 or 3 or 4
Console.WriteLine("-----");

// swap by ValueTuple
int first = 100;
int second = 200;
(first, second) = (second, first);
Console.WriteLine(first); // 200
Console.WriteLine(second); // 100
Console.WriteLine("-----");

```

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
    - sometimes we can use the amortized time complexity or average time complexity instead of the worst case time complexity

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
list1 = [6, 2, 8, 3 , 1]
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

# add is O(1) in avg
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

# concatenation is O(n)
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

# del is O(n)
list1 = ['cat', 'bat', 'rat', 'elephant']
del list1[0:2]
print(list1) # ['rat', 'elephant']
del list1[1]
print(list1) # ['rat']

# clear O(n)
listA = []
listA.append(['f'])
print(listA) # [['f']]
listA.clear()
print(listA) # []

# get/access by index is O(1)
arr = [5, 8, 10]
num = arr[1]
print(num) # 8

# index(value), return its index (first met), is O(n)
nums = [4, 3, 2, 1, 200]
nums.index(200) # 4

# find min or max val in the list is O(n)
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

# get length is O(1)
arr = [5, 8, 10]
len(arr) # 3

# loop is O(n)
# traversal
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
# reverse traversal
nums = [4, 2, 6, 9]
for i in range(len(nums) - 1, -1, -1):
  print(i)
'''
3
2
1
0
'''
# loop with index
nums = [1, 2, 3, 4]
for i, num in enumerate(nums):
    print(i, num)
'''
0 1
1 2
2 3
3 4
'''
# reverse list when looping
# if using "sorted" then become O(nlogn)
nums = [1, 2, 3, 4]
for num in reversed(nums):
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

# check is O(n)
# check exist or not
print('howdy' in ['hello', 'hi', 'howdy', 'heyas']) # True
print('hx' not in ['hello', 'hi', 'howdy', 'heyas']) # True
# True if at least one item in collection is truthy, False if empty
any([False, True, False]) # True
any([]) # False
any([None, None]) # False
# True if all items in collection are true
all([True, 1, 3, True]) # True

# count is O(n)
nums = [10, 20, 10, 20, 300, 500, 600]
nums.count(10) # 2
nums.count(300) # 1

# iter() creates an object which can be iterated one element at a time
# have to call next() to get first element
# use list() to returns a list of iterator's remaining elements, cannot iteration afterwards
iter_list = iter([0, 5, 10, 20, 30])   
next(iter_list) # 0
next(iter_list) # 5
list(iter_list) # [10, 20, 30]

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
def myLen(element):
  return len(element)
xs = ['xxxx', 'xxxxxxxxxx', 'xxx', 'xx']
xs.sort(key = myLen) # ['xx', 'xxx', 'xxxx', 'xxxxxxxxxx']
xs.sort(key = lambda x: - len(x)) # ['xxxxxxxxxx', 'xxxx', 'xxx', 'xx']
interval = [[10, -4], [2, 3], [7, -140]]
sorted(interval, key = lambda x: x[0]) # [[2, 3], [7, -140], [10, -4]]
from functools import cmp_to_key
sorted(interval, key = cmp_to_key(lambda p, q: p[1] - q[1])) # [[7, -140], [10, -4], [2, 3]]
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
def addition(n):
    return n + n
nums = (1, 2, 3, 4)
result = map(addition, nums)
print(result) # map object ref
print(list(result)) # [2, 4, 6, 8]
nums = [25, 10, 3]
strings = list(map(str, nums))
print(strings) # ['25', '10', '3']
strings = ['2', '2', '1']
nums = list(map(int, strings))
print(nums) # [2, 2, 1]
names = ['appLE', 'cAndy']
strings = list(map(str.capitalize, names))
print(strings) # ['Apple', 'Candy']
names = ['   apple ', 'candy ']
strings = list(map(str.strip, names))
print(strings) # ['apple', 'candy']
nums1 = [25, 10, 3]
nums2 = [2, 2, 1]
strings = list(map(pow, nums1, nums2))
print(strings) # [625, 100, 3]
names = ['appLE', 'cAndy']
strings = list(map(len, names))
print(strings) # [5, 5]
names = ['   apple ', 'candy ']
strings = list(map(str.upper, names))
print(strings) # ['   APPLE ', 'CANDY ']
# map with lambda
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = map(lambda x, y: x + y, nums1, nums2)
print(list(result)) # [5, 7, 9]

# filter is O(n)
nums = [1, 10, 3, 4, 5, 7, 9]
new_nums = filter(lambda x: x % 2, nums)
print(nums) # [1, 10, 3, 4, 5, 7, 9]
print(new_nums) # filter object ref
print(list(new_nums)) # [1, 3, 5, 7, 9]

# reduce is O(n)
from functools import reduce
nums = [1, 3, 5, 7, 9]
def add(x, y):
    return x + y
print(reduce(add, nums)) # 25
print(reduce(lambda x, y: x + y, nums)) # 25
print(nums) # [1, 3, 5, 7, 9]

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

# add element, O(1)
# dict require hashable keys (number, string, tuple...)
# or update/set an existed element, O(1)
d = {'apple': 100}
d['box'] = 50
d['apple'] = 200
print(d) # {'apple': 200, 'box': 50}

# get value by get method, O(1)
# return None if key is not existed and default value not defined
# return default value if key is not existed
# get value by indexing, O(1), could throw key error if key not existed
d = {'apple': 200, 'box': 50}
d.get('box') # 50
d.get('cat') # None
d.get('box', 999) # 50
d.get('cat', 999) # 999
d['box'] # 50
# d['cat'] # key error

# del element, O(1)
# delete key-value pair from dict
# delete wrong key will throw key error
del d['apple']
print(d) # {'box': 50}

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

# get all keys is O(1)
d = {'apple': 200, 'box': 50}
d.keys() # dict_keys(['apple', 'box'])

# get all values is O(1)
d.values() # dict_values([200, 50])

# get all items is O(1)
d.items() # dict_items([('apple', 200), ('box', 50)])

# length, O(1)
len(d) # 2

# is empty, O(1)
len(d) == 0 # False

# setdefault is O(1)
d = {'a':1, 'b':5}
res1 = d.get('e', 98)
res2 = d.setdefault('b', 59)
res3 = d.setdefault('c', 590)
print(res1) # 98
print(res2) # 5
print(res3) # 590
print(d) # {'a': 1, 'b': 5, 'c': 590}
map1 = {}
map1.setdefault("x", []).append(1)
print(map1) # {'x': [1]}
map1.setdefault("y", []).append(2)
print(map1) # {'x': [1], 'y': [2]}
map1.setdefault("x", []).append(3)
print(map1) # {'x': [1, 3], 'y': [2]}
map1.setdefault("z", []).append(4)
print(map1) # {'x': [1, 3], 'y': [2], 'z': [4]}

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
print(math.isclose(1, 1.000000001)) # False
print(math.isclose(1.1, 1.100000001)) # True
print(math.isclose(1.11, 1.110000001)) # True

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
ord('0')  # 48
ord('9')  # 57
ord('A')  # 65
ord('Z')  # 90
ord('a')  # 97
ord('z')  # 122

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
# list
```Java
// Array and ArrayList

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // init
        int[] arr1 = new int[5];
        long[] arr2 = new long[5];
        char[] arr3 = new char[5];
        int[] arr4 = {9, 3, 2, 100, 4};

        System.out.println(Arrays.toString(arr1)); // [0, 0, 0, 0, 0]
        System.out.println(Arrays.toString(arr2)); // [0, 0, 0, 0, 0]
        System.out.println(Arrays.toString(arr3)); // [, , , , ]
        System.out.println(arr3[0] == '\u0000'); // true
        System.out.println(Arrays.toString(arr4)); // [9, 3, 2, 100, 4]

        // update in O(1)
        arr1[2] = 100;
        System.out.println(Arrays.toString(arr1)); // [0, 0, 100, 0, 0]

        // get in O(1)
        int ele = arr1[2];
        System.out.println(ele); // 100

        // size in O(1)
        int size = arr1.length;
        System.out.println(size); // 5

        // fill in O(n)
        Arrays.fill(arr1, 9);
        System.out.println(Arrays.toString(arr1)); // [9, 9, 9, 9, 9]

        // loop in O(n)
        for (int i = 0; i < arr4.length; i++) {
            System.out.print(i + ": " + arr4[i] + ", "); 
        }
        System.out.println(); // 0: 9, 1: 3, 2: 2, 3: 100, 4: 4,

        for (int num: arr4) {
            System.out.print(num + ", "); 
        }
        System.out.println(); // 9, 3, 2, 100, 4, 

        // sort in O(nlogn)
        Arrays.sort(arr4);
        System.out.println(Arrays.toString(arr4)); // [2, 3, 4, 9, 100]

        String[] arr5 = {"a", "b", "c", "d", "e"};
        Arrays.sort(arr5, Comparator.reverseOrder());
        System.out.println(Arrays.toString(arr5)); // [e, d, c, b, a]

        String[] arr6 = {"banana", "cucumber", "apple"};

        Arrays.sort(arr6, (a, b) -> a.length() - b.length());
        System.out.println(Arrays.toString(arr6)); // [apple, banana, cucumber]
        Arrays.sort(arr6, (a, b) -> b.length() - a.length());
        System.out.println(Arrays.toString(arr6)); // [cucumber, banana, apple]

        // 2D array
        int[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

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
        /*
        0 0 0 0 0 
        0 0 0 0 0 
        0 0 0 0 0 
        */
    }
}

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // init
        List<Integer> list1 = new ArrayList<>();

        System.out.println(list1); // []

        // append in O(1) (avg)
        list1.add(5);
        list1.add(8);
        list1.add(20);
        System.out.println(list1); // [5, 8, 20]

        // get in O(1)
        System.out.println(list1.get(0)); // 5

        // size in O(1)
        System.out.println(list1.size()); // 3

        // update in O(1)
        list1.set(2, 99);
        System.out.println(list1); // [5, 8, 99]

        // insert in O(n)
        list1.add(0, 100);
        System.out.println(list1); // [100, 5, 8, 99]

        // delete in O(n)
        list1.remove(list1.size() - 1);
        System.out.println(list1); // [100, 5, 8]

        // sort in O(nlogn)
        Collections.sort(list1);
        System.out.println(list1); // [5, 8, 100]
        Collections.sort(list1, (a, b) -> b - a);
        System.out.println(list1); // [100, 8, 5]
    }
}
```

# dict
```Java
// HashMap

import java.util.*;

public class Main {

    public static void main(String[] args) {
        
        // init
        Map<String, Integer> map = new HashMap<>();

        // add and update in O(1)
        map.put("first", 1);
        map.put("second", 2);
        System.out.println(map); // {first=1, second=2}

        map.put("second", 50);
        System.out.println(map); // {first=1, second=50}

        // get in O(1)
        System.out.println(map.get("first")); // 1
        System.out.println(map.get("third")); // null

        // look in O(1)
        System.out.println(map.containsKey("first")); // true
        System.out.println(map.containsKey("third")); // false

        // delete in O(1)
        map.remove("second");
        System.out.println(map); // {first=1}
        map.remove("second");
        System.out.println(map); // {first=1}

        // size in O(1)
        System.out.println(map.size()); // 1

        // above ops are avg O(1) due to the possibility of hash collision

        // get keys in O(1), but print them out is O(n)
        map.put("fourth", 400);
        Set<String> set = map.keySet();
        System.out.println(set); // [fourth, first]

        // get values in O(n)
        Collection<Integer> collection = map.values();
        System.out.println(collection); // [400, 1]

        // get key-value pairs in O(1), but print them out is O(n)
        Set<Map.Entry<String, Integer>> entrySet = map.entrySet();
        System.out.println(entrySet); // [fourth=400, first=1]
    }
}
```

# set
```Java
// HashSet

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // init
        Set<Integer> set = new HashSet<>();
        System.out.println(set); // []

        // add in O(1)
        boolean bool1 = set.add(100);
        boolean bool2 = set.add(500);
        System.out.println(bool1); // true
        System.out.println(bool2); // true
        System.out.println(set); // [100, 500]

        boolean bool3 = set.add(100);
        System.out.println(bool3); // false
        System.out.println(set); // [100, 500]

        // look in O(1)
        System.out.println(set.contains(100)); // true
        System.out.println(set.contains(3000)); // false

        // size in O(1)
        System.out.println(set.size()); // 2

        // delete in O(1)
        boolean bool4 = set.remove(500);
        boolean bool5 = set.remove(500);
        System.out.println(bool4); // true
        System.out.println(bool5); // false
        System.out.println(set); // [100]
    }
}
```

# tree map
```Java
// TreeMap

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // init
        TreeMap<String, Integer> treeMap1 = new TreeMap<>();
        System.out.println(treeMap1); // {}

        // size in O(1)
        System.out.println(treeMap1.size()); // 0

        // add and update in O(logn)
        treeMap1.put("apple", 10);
        treeMap1.put("banana", 30);
        System.out.println(treeMap1); // {apple=10, banana=30}
        treeMap1.put("banana", 45);
        System.out.println(treeMap1); // {apple=10, banana=45}

        // get in O(logn)
        System.out.println(treeMap1.get("apple")); // 10
        System.out.println(treeMap1.get("mango")); // null

        // look in O(logn)
        System.out.println(treeMap1.containsKey("apple")); // true
        System.out.println(treeMap1.containsKey("mango")); // false

        // delete in O(logn)
        Integer val1 = treeMap1.remove("banana");
        Integer val2 = treeMap1.remove("banana");
        System.out.println(val1); // 45
        System.out.println(val2); // null
        System.out.println(treeMap1); // {apple=10}

        // first key in O(logn)
        TreeMap<Integer, String> treeMap2 = new TreeMap<>();
        treeMap2.put(100, "apple");
        treeMap2.put(500, "banana");
        treeMap2.put(300, "mango");
        System.out.println(treeMap2); // {100=apple, 300=mango, 500=banana}
        System.out.println(treeMap2.firstKey()); // 100

        // last key in O(logn)
        System.out.println(treeMap2.lastKey()); // 500

        // ceiling key in O(logn)
        System.out.println(treeMap2.ceilingKey(400)); // 500
        System.out.println(treeMap2.ceilingKey(500)); // 500
        System.out.println(treeMap2.ceilingKey(600)); // null
        
        // floor key in O(logn)
        System.out.println(treeMap2.floorKey(200)); // 100
        System.out.println(treeMap2.floorKey(100)); // 100
        System.out.println(treeMap2.floorKey(50)); // null
        
        // lower key in O(logn)
        System.out.println(treeMap2.lowerKey(200)); // 100
        System.out.println(treeMap2.lowerKey(100)); // null
        System.out.println(treeMap2.lowerKey(50)); // null
    }
}
```

# heap
```Java
// PriorityQueue

import java.util.*;

class FreqWord {
    private String content;
    private Integer freq;

    public FreqWord(String content, Integer freq) {
        this.content = content;
        this.freq = freq;
    }

    public String getContent() { return content; }
    public Integer getFreq() { return freq; }
}

public class Main {

    public static void main(String[] args) {

        // init, default is min heap
        PriorityQueue<Integer> pq1 = new PriorityQueue<>();
        PriorityQueue<Integer> pq2 = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<FreqWord> pq3 = 
            new PriorityQueue<>((a, b) -> a.getFreq() != b.getFreq() ? 
                                a.getFreq() - b.getFreq() : a.getContent().compareTo(b.getContent()));
        /*
        PriorityQueue<FreqWord> pq3 = new PriorityQueue<>(
            Comparator.comparing(FreqWord::getFreq)
                      .thenComparing(FreqWord::getContent)
        );
        */

        // peek in O(1)
        pq3.offer(new FreqWord("mango", 25));
        System.out.println(pq3.peek().getContent()); // mango
        pq3.offer(new FreqWord("pineapple", 10));
        System.out.println(pq3.peek().getContent()); // pineapple
        pq3.offer(new FreqWord("banana", 10));
        System.out.println(pq3.peek().getContent()); // banana
        pq3.offer(new FreqWord("apple", 5));
        System.out.println(pq3.peek().getContent()); // apple
        pq3.offer(new FreqWord("grape", 5));
        System.out.println(pq3.peek().getContent()); // apple

        // size in O(1)
        System.out.println(pq3.size()); // 4

        // push in O(logn)
        pq1.offer(100);
        pq1.offer(50);
        pq1.offer(200);
        System.out.println(pq1.peek()); // 50
        pq2.offer(100);
        pq2.offer(50);
        pq2.offer(200);
        System.out.println(pq2.peek()); // 200

        // pop in O(logn)
        System.out.println(pq1.size()); // 3
        Integer num = pq1.poll();
        System.out.println(num); // 50
        System.out.println(pq1.size()); // 2
        System.out.println(pq1.peek()); // 100
    }
}
```

# stack and queue
```Java
// ArrayDeque

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // init
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        // push in O(1) (in left)
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack); // [3, 2, 1]

        // pop in O(1) (in left)
        Integer num1 = stack.pop();
        System.out.println(num1); // 3
        System.out.println(stack); // [2, 1]

        // peek in O(1) (in left)
        Integer num2 = stack.peek();
        System.out.println(num2); // 2
        System.out.println(stack); // [2, 1]

        // size in O(1)
        System.out.println(stack.size()); // 2
    }
}

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // init
        ArrayDeque<Integer> queue = new ArrayDeque<>();

        // push in O(1) (in right)
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        System.out.println(queue); // [1, 2, 3]

        // pop in O(1) (in left)
        Integer num1 = queue.poll();
        System.out.println(num1); // 1
        System.out.println(queue); // [2, 3]

        // peek (in left) and peekLast (in right) in O(1)
        Integer num2 = queue.peek();
        System.out.println(num2); // 2
        System.out.println(queue); // [2, 3]
        Integer num3 = queue.peekLast();
        System.out.println(num3); // 3
        System.out.println(queue); // [2, 3]

        // size in O(1)
        System.out.println(queue.size()); // 2
    }
}
```

# number
```Java
// number

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // min and max
        int max1 = Integer.MAX_VALUE;
        int min1 = Integer.MIN_VALUE;
        System.out.println(max1); // 2147483647
        System.out.println(min1); // -2147483648
        long max2 = Long.MAX_VALUE;
        long min2 = Long.MIN_VALUE;
        System.out.println(max2); // 9223372036854775807
        System.out.println(min2); // -9223372036854775808

        // division
        int num1 = 80;
        int num2 = 7;
        System.out.println(num1 / num2); // 11
        System.out.println(num1 % num2); // 3
        int num3 = 10;
        int num4 = - 7;
        int num5 = - 17;
        System.out.println(num3 / num4); // - 1, truncate toward zero
        System.out.println(num3 / num5); // 0, truncate toward zero

        // random
        // [a, b]
        int max3 = 5;
        int min3 = 2;
        Random random = new Random();
        int randomInt = random.nextInt((max3 - min3) + 1) + min3;
        System.out.println(randomInt); // 5

    }
}
```

# string
```Java
// String and StringBuilder and StringBuffer

// String: Immutable, safe for use in multi-threaded environments, but may be inefficient in scenarios requiring extensive modifications due to constant creation of new objects
// StringBuilder: Mutable, not thread-safe, efficient for single-threaded scenarios where lots of modifications are required
// StringBuffer: Mutable, thread-safe, suitable for multi-threaded scenarios but slower than StringBuilder due to synchronization

import java.util.*;

public class Main {

    public static void main(String[] args) {

        String s = "Apple";

        // size in O(1)
        System.out.println(s.length()); // 5
        
        // get char in O(1)
        System.out.println(s.charAt(4)); // e

        // get substring in O(n), [a, b)
        System.out.println(s.substring(0, 2)); // Ap

        // look in O(n)
        boolean bool1 = s.contains("pp");
        boolean bool2 = s.contains("zq");
        System.out.println(bool1); // true
        System.out.println(bool2); // false
        boolean bool3 = s.startsWith("Axp");
        boolean bool4 = s.endsWith("pple");
        System.out.println(bool3); // false
        System.out.println(bool4); // true

        // look idx in O(n)
        System.out.println(s.indexOf("pl")); // 2
        System.out.println(s.indexOf("z")); // - 1

        // get char array in O(n)
        char[] arr = s.toCharArray();
        System.out.println(arr); // Apple
        System.out.println(arr[4]); // e

        // split in O(n)
        String sentence = "apple,banana,mango";
        String[] words = sentence.split(",");
        System.out.println(Arrays.toString(words)); // [apple, banana, mango]

        // compare in O(n)
        String s1 = "apple";
        String s2 = "apple";
        String s3 = "banana";
        System.out.println(s1.equals(s2)); // true
        System.out.println(s1.compareTo(s2)); // 0
        System.out.println(s1.compareTo(s3)); // - 1

        // change case in O(n)
        String upperS = s.toUpperCase();
        String lowerS = s.toLowerCase();
        System.out.println(upperS); // APPLE
        System.out.println(lowerS); // apple

        // trim in O(n)
        String beforeTrim = "   Polo. ";
        String afterTrim = beforeTrim.trim();
        System.out.println(afterTrim); // Polo.

        // replace in O(n)
        String beforeReplace = "Yolo";
        String afterReplace = beforeReplace.replace("o", "a");
        System.out.println(afterReplace); // Yala

        // concat in O(n)
        String s1 = "a" + "b" + "c";
        System.out.println(s1); // abc
        String s2 = "Hello".concat(" World").concat("!!"); 
        System.out.println(s2); // Hello World!!

        // char related methods
        char c1 = 'a';
        char c2 = 'A';
        char c3 = '5';
        System.out.println(Character.isLetter(c1)); // true
        System.out.println(Character.isDigit(c3)); // true
        System.out.println(Character.isLetterOrDigit(c3)); // true
        System.out.println(Character.isUpperCase(c2)); // true
        System.out.println(Character.isLowerCase(c1)); // true

        // StringBuilder
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder(s);
        sb1.append("f");
        sb2.append("f");
        System.out.println(sb1.toString()); // f
        System.out.println(sb2.reverse().toString()); // felppA

        // StringBuffer
        StringBuffer sbf = new StringBuffer("Hello");
        sbf.append(" World");
        System.out.println(sbf.toString()); // Hello World
        StringBuffer sb = new StringBuffer("Hello");
        sb.insert(5, " World"); // Hello World
        StringBuffer sb = new StringBuffer("HelloWorld");
        sb.delete(5, 10); // Hello
        StringBuffer sb = new StringBuffer("HelloWorld");
        sb.replace(5, 10, " Friend"); // Hello Friend
        StringBuffer sb = new StringBuffer("Hello");
        sb.reverse(); // olleH
    }
}
```

# linked list
```Java
// linked list

class ListNode<T> {
    T val;
    ListNode<T> next;
    public ListNode(T val) {
        this.val = val;
    }
}

public class Main {

    public static void main(String[] args) {

        ListNode<Integer> node1 = new ListNode<>(1);
        ListNode<Integer> node2 = new ListNode<>(2);
        ListNode<Integer> node3 = new ListNode<>(3);
        node1.next = node2;
        node2.next = node3;
        System.out.println(node1.next.next.val); // 3
    }
}
```

# tree
```Java
// tree

class Node<T> {
    T val;
    Node<T> left;
    Node<T> right;
    public Node(T val) {
        this.val = val;
    }
}

public class Main {

    public static void main(String[] args) {

        Node<Integer> node1 = new Node<>(1);
        Node<Integer> node2 = new Node<>(2);
        Node<Integer> node3 = new Node<>(3);
        node1.left = node2;
        node2.left = node3;
        System.out.println(node1.left.left.val); // 3
        System.out.println(node1.left.right); // null
    }
}
```

# sort
```Java
// comparable interface and comparator interface
// nested classes (static nested class, inner class, local class, anonymous class)
// lambda expression
// method references

import java.util.*;

class Person implements Comparable<Person> {
    private String name;
    private int age;

    // Constructor chaining
    public Person() {
        this("Default", 100);
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }

    public int getAge() { return age; }

    @Override
    public String toString() { return this.name + " - " + this.age; }

    // Implementing the Comparable Interface and compareTo method - sort by age (asc)
    @Override
    public int compareTo(Person other) {
        return this.age - other.age; 
    }

    // Static nested class - Implementing the Comparator Interface and compare method - sort by name (asc)
    static class PersonNameComparator implements Comparator<Person> {
        @Override
        public int compare(Person p1, Person p2) {
            return p1.name.compareTo(p2.name);
        }
    }

    // Inner class - Implementing the Comparator Interface and compare method - sort by name length (asc)
    class PersonNameLengthComparator implements Comparator<Person> {
        @Override
        public int compare(Person p1, Person p2) {
            return Integer.compare(p1.name.length(), p2.name.length());
        }
    }

    // Local class in the method - Implementing the Comparator Interface and compare method - sort by the last char of the name (asc)
    public static void sortByNameLastChar(List<Person> people) {
        class PersonLastNameCharacterComparator implements Comparator<Person> {
            @Override
            public int compare(Person p1, Person p2) {
                return Character.compare(p1.name.charAt(p1.name.length() - 1), p2.name.charAt(p2.name.length() - 1));
            }
        }
        Collections.sort(people, new PersonLastNameCharacterComparator());
    }

    // Anonymous class in the method - Implementing the Comparator Interface and compare method - sort by age (asc)
    public static void sortByAgeAscI(List<Person> people) {
        Collections.sort(people, new Comparator<Person>() {
            @Override
            public int compare(Person p1, Person p2) {
                return p1.age - p2.age;
            }
        });
    }

    // Lambda expression in the method - sort by age (desc)
    public static void sortByAgeDesc(List<Person> people) {
        Collections.sort(people, (p1, p2) -> p2.age - p1.age);
    }

    // Lambda expression in the method - sort by age (asc)
    public static void sortByAgeAscII(List<Person> people) {
        Collections.sort(people, Comparator.comparing(p -> p.age));
    }

    // Method references in the method - sort by age (asc) then name (asc)
    public static void sortByAgeThenName(List<Person> people) {
        Collections.sort(people, Comparator.comparing(Person::getAge).thenComparing(Person::getName));
    }

}

public class Main {
    public static void main(String[] args) {
        ArrayList<Person> people = new ArrayList<>();
        people.add(new Person("Appkz", 30));
        people.add(new Person("Zeeeec", 25));
        people.add(new Person("Cata", 20));
        people.add(new Person("Pay", 50));
        people.add(new Person("Ye", 50));

        // Sorting - element's Class must implement the Comparable Interface and compareTo method - sort by age (asc)
        Collections.sort(people);

        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Cata - 20
        Zeeeec - 25
        Appkz - 30
        Pay - 50
        Ye - 50
        */

        // Sorting with the Comparator - Comparator comes from a static nested class - sort by name (asc)
        Collections.sort(people, new Person.PersonNameComparator());

        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Appkz - 30
        Cata - 20
        Pay - 50
        Ye - 50
        Zeeeec - 25
        */

        // Sorting with the Comparator and revsersed method - Comparator comes from a static nested class - sort by name (desc)
        Collections.sort(people, new Person.PersonNameComparator().reversed());

        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Zeeeec - 25
        Ye - 50
        Pay - 50
        Cata - 20
        Appkz - 30
        */

        // Sorting with the Comparator - Comparator comes from a inner class - sort by name length (asc)
        Collections.sort(people, new Person().new PersonNameLengthComparator());
        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Ye - 50
        Pay - 50
        Cata - 20
        Appkz - 30
        Zeeeec - 25
        */

        // Sorting with static method (local class in that method) - sort by the last char of the name (asc)
        Person.sortByNameLastChar(people);
        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Cata - 20
        Zeeeec - 25
        Ye - 50
        Pay - 50
        Appkz - 30
        */

        // Sorting with static method (anonymous class in that method) - sort by age (asc)
        Person.sortByAgeAscI(people);
        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Cata - 20
        Zeeeec - 25
        Appkz - 30
        Ye - 50
        Pay - 50
        */

        // Sorting with static method (lambda expression in that method) - sort by age (desc)
        Person.sortByAgeDesc(people);
        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Ye - 50
        Pay - 50
        Appkz - 30
        Zeeeec - 25
        Cata - 20
        */

        // Sorting with static method (lambda expression in that method) - sort by age (asc)
        Person.sortByAgeAscII(people);
        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Cata - 20
        Zeeeec - 25
        Appkz - 30
        Ye - 50
        Pay - 50
        */

        // Sorting with static method (method references in that method) - sort by age (asc) then name (asc)
        Person.sortByAgeThenName(people);
        for (Person p : people) {
            System.out.println(p);
        }
        System.out.println("---");
        /*
        Cata - 20
        Zeeeec - 25
        Appkz - 30
        Pay - 50
        Ye - 50
        */
    }
}

```

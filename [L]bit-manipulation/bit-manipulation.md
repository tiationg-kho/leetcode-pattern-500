# bit manipulation

## intro

```python
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

# exclusive or
5 ^ 5 # 0
5 ^ 5 ^ 3 # 3

# not (~)

# turn int number to 4-byte string (length = 4)
# 256 == 8 bits == 1 byte
bin(0xff) # '0b11111111'
def int_to_string(val):
    byte_array = [(val >> (i * 8)) & 0xFF for i in range(4)][::- 1]
    char_array = [chr(byte) for byte in byte_array]
    string = ''.join(char_array)
    return string

# turn 4-byte string to int number
def string_to_int(string):
    val = 0
    for i, c in enumerate(string):
        val += ord(c) << (8 * (4 - 1 - i)) # use |= here is applicable too
    return val

num = 12345
s = int_to_string(num)
res = string_to_int(s)
print(res) # 12345
```

## pattern


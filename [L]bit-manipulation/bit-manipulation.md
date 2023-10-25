# bit manipulation

## intro

```python
# bitmasking
# start from: mask = 0
# check: mask & 1<<k == 0, if equals 0 means not mask 1<<k yet
# masking: mask = mask | 1<<k
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

# exclusive or
5 ^ 5 # 0
5 ^ 5 ^ 3 # 3

# not (~)

```

## pattern


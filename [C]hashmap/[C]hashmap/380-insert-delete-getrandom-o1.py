import random
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.num_idx:
            return False
        else:
            self.nums.append(val)
            self.num_idx[val] = len(self.nums) - 1 
            return True

    def remove(self, val: int) -> bool:
        if val in self.num_idx:
            old_val = val
            old_idx = self.num_idx[old_val]
            last_val = self.nums[- 1]
            last_idx = len(self.nums) - 1
            self.nums[old_idx] = last_val
            self.nums[last_idx] = old_val
            self.nums.pop()
            self.num_idx[last_val] = old_idx
            self.num_idx[old_val] = last_idx
            self.num_idx.pop(old_val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# time O(1)
# space O(n), due to hashmap and list
# using hashmap and store val and list
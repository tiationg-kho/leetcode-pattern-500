from collections import defaultdict
import random
class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.num_indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        if val in self.num_indices:
            self.nums.append(val)
            self.num_indices[val].add(len(self.nums) - 1)
            return False
        else:
            self.nums.append(val)
            self.num_indices[val].add(len(self.nums) - 1)
            return True

    def remove(self, val: int) -> bool:
        if val in self.num_indices:
            old_val = val
            old_idx = self.num_indices[old_val].pop()
            self.num_indices[old_val].add(old_idx)
            last_val = self.nums[- 1]
            last_idx = len(self.nums) - 1

            self.nums[old_idx] = last_val
            self.nums[last_idx] = old_val
            self.nums.pop()
            
            if old_val != last_val:
                self.num_indices[last_val].remove(last_idx)
                self.num_indices[last_val].add(old_idx)
                self.num_indices[old_val].remove(old_idx)
            else:
                self.num_indices[last_val].remove(last_idx)

            if not self.num_indices[old_val]:
                self.num_indices.pop(old_val)
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# time O(1)
# space O(n), due to hashmap and list
# using hashmap and store val and list and hashset
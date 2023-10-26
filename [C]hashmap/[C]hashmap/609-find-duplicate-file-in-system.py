from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path = defaultdict(list)
        
        for p in paths:
            files = p.split(' ')
            root_path = files[0]
            for i in range(1, len(files)):
                data = files[i].split('(')
                file_path = data[0]
                content = data[1][: - 1]
                content_path[content].append(root_path + "/" + file_path)

        return [v for v in content_path.values() if len(v) > 1]

# time O(nL)
# space O(nL)
# using hashmap and store val and string
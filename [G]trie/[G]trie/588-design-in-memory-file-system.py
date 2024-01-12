class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ''

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        node = self.get_node(path)
        if node.content:
            return [path.split('/')[- 1]]
        return sorted(list(node.children.keys()))

    def mkdir(self, path: str) -> None:
        self.get_node(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.get_node(filePath)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.get_node(filePath)
        return node.content

    def get_node(self, path):
        if path == '/':
            return self.root
        path = path.split('/')[1:]
        node = self.root
        for p in path:
            if p not in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        return node

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# time O(L), most operation is O(L), and ls() can be O(L + klogk), k is the number of files
# space O(nL), n is the number of paths and files, L is the path's length
# using trie and custom trie node
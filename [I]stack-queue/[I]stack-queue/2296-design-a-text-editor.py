class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        res = 0
        while self.left and k:
            self.left.pop()
            k -= 1
            res += 1
        return res

    def cursorLeft(self, k: int) -> str:
        while self.left and k:
            self.right.append(self.left.pop())
            k -= 1
        res = ''
        for i in range(len(self.left) - 1, - 1, - 1):
            res = self.left[i] + res
            if len(res) == 10:
                break
        return res

    def cursorRight(self, k: int) -> str:
        while self.right and k:
            self.left.append(self.right.pop())
            k -= 1
        res = ''
        for i in range(len(self.left) - 1, - 1, - 1):
            res = self.left[i] + res
            if len(res) == 10:
                break
        return res

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
                       
# time O(s) for add, O(1) for init, others are O(k)
# space O(n)
# using stack and queue and stack to simulate and two stacks
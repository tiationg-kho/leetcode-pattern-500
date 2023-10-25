# tree

## intro

**tree properties**

- tree is a special graph with properties that
    - connected
    - acyclic
    - non-direction edges
    - one path/edge between any two vertices/node
- important tree concepts
    - types of node
        - root
        - leaf
        - parent
        - child
        - sibling
        - left boundary
        - right boundary
        - lowest common ancestor (LCA) of two nodes
    - depth/height of tree
    - node’s degree
    - subtree
    - traversal
    - types of tree
        - binary tree
            - every node has at most two children (left and right)
        - binary search tree (BST)
            - for each node
                - nodes in left subtree have smaller keys
                - nodes in right subtree have larger keys
            - inorder traversal res is an ascending sorted list
        - height-balanced binary tree
            - depth of the two subtrees of every node never differs by more than one
        - perfect binary tree
            - all leaf nodes at the same depth
            - every node has degree 2
        - complete binary tree
            - every level is completely filled besides last level
            - nodes in last level align left
        - full/strictly binary tree
            - every non-leaf node has degree 2

**how to define tree node**

```python
# definition for a binary tree node
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# definition for a n-nary tree node
class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = []
```

**if you need to do tree traversal, then try**

1. BFS (levelorder)
    1. level 0 → level 1 → level2
    2. time `O(n)`, due to visiting all nodes
    3. space `O(n)`, due to perfect tree or complete tree, otherwise `O(diameter(count of nodes in same level))`
    4. use bfs when the operation related to level
    
    ```python
    from collections import deque
    
    def bfs(root):
        queue = deque([root]) 
        while queue: 
            node = queue.popleft()
            if SOME_CONDITION:
                return FOUND
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        return NOTFOUND
    ```
    
2. DFS preorder
    1. node → left → right
    2. time `O(n)`, due to visiting all nodes
    3. space `O(n)`, due to skewed tree, otherwise `O(height)`
    4. use preorder when the operation has a top-down flow
    
    ```python
    # recursive
    preorder = []

    def preorder_helper(root):
        if not root:
            return
        preorder.append(root.val)    
        preorder_helper(root.left)
        preorder_helper(root.right)
        return

    preorder_helper(root)
    return preorder
    
    # iterative I
    preorder = []
    if not root:
        return preorder
    stack = [root]
    while stack:
        node = stack.pop()
        preorder.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return preorder
    
    # iterative II
    preorder = []
    if not root:
        return preorder
    stack = [(root, False)]
    while stack:
        node, children_visited = stack.pop()
        if children_visited:
            preorder.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
            stack.append((node, True))
    return preorder
    ```
    
3. DFS inorder
    1. left → node → right
    2. time `O(n)`, due to visiting all nodes
    3. space `O(n)`, due to skewed tree, otherwise `O(height)`
    4. use inorder when the operation consider the ascending val order (when using BST)
    
    ```python
    # recursive
    inorder = []

    def inorder_helper(root):
        if not root:
            return
        inorder_helper(root.left)
        inorder.append(root.val)   
        inorder_helper(root.right)
        return

    inorder_helper(root)
    return inorder
    
    # iterative I
    inorder = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
    return inorder
    
    # iterative II
    inorder = []
    if not root:
        return inorder
    stack = [(root, False)]
    while stack:
        node, children_visited = stack.pop()
        if children_visited:
            inorder.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
    return inorder
    ```
    
4. DFS postorder
    1. left → right → node
    2. time `O(n)`, due to visiting all nodes
    3. space `O(n)`, due to skewed tree, otherwise `O(height)`
    4. use postorder when the operation has a bottom-up flow
    
    ```python
    # recursive
    postorder = []

    def postorder_helper(root):
        if not root:
            return
        postorder_helper(root.left)
        postorder_helper(root.right)
        postorder.append(root.val)
        return

    postorder_helper(root)
    return postorder
    
    # iterative I
    rev_postorder = []
    if not root:
        return rev_postorder
    stack = [root]
    while stack:
        node = stack.pop()
        rev_postorder.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return rev_postorder[::-1]
    
    # iterative II
    postorder = []
    if not root:
        return postorder
    stack = [(root, False)]
    while stack:
        node, children_visited = stack.pop()
        if children_visited:
            postorder.append(node.val)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    return postorder
    ```
    
5. Morris inorder traversal
    1. in normal inorder traversal, we store cur node in stack then got to left, but morris traversal store cur node by link it from its predecessor
    2. link the predecessor and successor
        1. only the node with left subtree will need its predecessor to link to itself (successor)
        2. the predecessor node is the right-most node in left subtree
        3. due to linking, will modify the tree data temporary
    3. time `O(n)`, due to visiting all nodes
        1. each edge is traversed for 3 times at most
            1. traverse through
            2. find predecessor (and build link)
            3. find predecessor (and found link already existed)
        2. why finding predecessor would not increase time complexity
            1. intuitive way to think about it is that more right branch nodes will make link route longer, but more right branch nodes will not cause the need of more link route for themself
            2. only more left branch nodes will need more link route for themself, but more left branch nodes only need the short link route for themself
    4. space `O(1)`, due to no cost for stack, queue or recursion stack (not counting output list’s cost)
    
    ```python
    inorder = []
    cur = root
    while cur:
        # if cannot find prev/predecessor of cur, then add cur to list and go to cur.right
        if not cur.left:
            inorder.append(cur.val)
            cur = cur.right

        else:
            # find the prev/predecessor of cur (the right-most node in cur.left)
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right

            # make cur as right child of its prev (link the predecessor and successor) and go to cur.left
            if not prev.right:
                prev.right = cur
                cur = cur.left

            # if find the linked predecessor, add cur to list and unlink predecessor, then go to cur.right
            # means just come here from the prev node, the prev has alreardy recorded
            else:
                inorder.append(cur.val)
                prev.right = None
                cur = cur.right
    return inorder
    ```
    
6. Divide and Conquer
    1. use tree’s properties
        1. range (l and r)
            1. the idx from preorder, inorder, postorder array
                1. BST inorder’s val has ascending order
            2. the idx of the ascending order linked list
        2. parent and node’s relation
        3. direction from the parent
        4. validate the value interval (BST)

## pattern

- divide and conquer
    - two branch top-down
        - operation can
            - start from both side’s children (left subtree and right subtree)
            - start from two diff trees
    - re-build tree (top-down)
        - use divide and conquer
            - notice: val in tree should be unique
            - preorder’s first is root
            - postorder’s last is root
            - inorder’s middle is root (idx not sure yet)
                - inorder: left subtree + root + right subtree
                - we already have the root’s val (from preorder or postorder)
                - now use hashmap to quickly find the val’s idx in inorder array
            - parameters we need to pass down: left_idx, right_idx, node_count
            - when using preorder and postorder to re-build
                - notice: val in tree should be unique
                - can not confirm the re-built tree is the only possible tree
                - only if we know every non-leaf node in tree has degree 2 (full binary tree), then we can try to re-build the full binary tree version as only possible tree
                    - in other words, if we can guarantee we always have left subtree, then we can re-built the only possible tree
                - notice: when node_count is 1, just return that node. no need for building left and right subtrees
    - re-build BST
        - top-down approach
            - with preorder
                - in preorder: first node is root of tree/subtree
                - BST properties: use the lower and upper bound of val to check node is valid or not
            - with inorder
                - use the left and right ptr
                - array is already ascending order (BST's inorder res)
                - just use middle as root
                - notice: res tree will be height-balanced
        - inorder approach
            - build left subtree first
            - then root
            - right subtree last
            - notice: res tree will be height-balanced
    - use BST attributes
        - left subtree nodes’ val is less than the node’s val
        - right subtree nodes’ val is larger than the node’s val
        - left or right subtree is also BST
        - BST inorder traversal is ascending order
        - predecessor and successor
        - delete node in BST
            - use the delete node's left child as substitute
            - we do not modify node's left child's left child and right child directly
            - we link the delete node's right child to delete node's predecessor’s right side
                - notice: predecessor in the right-most node in left subtree
            - how to understand this method
              - treat delete node as old tree
              - we replace this old tree with its left subtree
              - we need to find the largest node in its left subtree (which is delete node's pred)
              - link delete node's right subtree to this pred node's right side
            ```python
            def delete_helper(node):
                if not node:
                    return None
                if node.val == key:
                    if not node.left:
                        node = node.right
                    else:
                        pred = node.left
                        while pred.right:
                            pred = pred.right
                        pred.right = node.right
                        node = node.left
                elif node.val > key:
                    node.left = delete_helper(node.left)
                else:
                    node.right = delete_helper(node.right)
                return node
            ```
    - find LCA
        - LCA in BST
            1. p and q node are inside LCA’s left and right subtree
            2. p is the root/LCA, and q is inside p's left or right subtree
        - find LCA without root and each node has stored parent info
            - use two pointers
            - [ p->LCA + LCA->root + q->LCA ] is same as [ q->LCA + LCA->root + p->LCA ]
    - populate next ptr
        - perfect binary tree
            - two nodes between the link (next ptr)
                - belong to same parent
                - belong to parents next to each other
            - when at level 0, need to build next ptrs at level 1 and so on
            - maintain
              - upper level's start ptr
              - upper level's cur ptr
        - regular binary tree
            - maintain
                - upper level’s start ptr
                - upper level's cur ptr
                - lower level’s start ptr
                - lower level’s cur_end ptr
    - unique BST
        - concept of Catalan Number
        - determine the root first
        - then we can know the choices of left subtree and right subtree
- preorder
    - use preorder when the operation has a top-down flow
      - eg. invert
    - turn tree to string
        ```python
        # dfs preorder
        def build(node):
            if not node:
                return '#null'
            cur = '#' + str(node.val)
            left = build(node.left)
            right = build(node.right)
            return cur + left + right
        ```
    - record leaves
        ```python
        # dfs preorder
        leaves = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node != root and not node.left and not node.right:
                leaves.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    stack.append(child)
        ```
- inorder
    - use inorder when the operation consider the ascending val order (when using BST)
- postorder
    - use postorder when the operation has a bottom-up flow
    - we will utilize the return value
- bfs
    - level related
    - notice the length of the queue means the count of cur level's nodes (we can process all nodes in same level in a for loop)
    - build a child_parent hashmap
        ```python
        # bfs
        node_parent = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
                    node_parent[child] = node
        ```
    - assign idx
        - using bfs
        - next level’s left is cur * 2
        - next level’s right is cur * 2 + 1
        - eg. root is 1, left child is 2, right child is 3
        - notice: we can turn this idx to binary to see we choose to go left or go right (eg. idx 5 is 101 means we go left then go right)
    - assign coordinates
        - using bfs
        - treat root node as (0, 0), then let row and col to define (x, y)
        - often use hashmap to record as assistance
            - key can be row or col, value is list
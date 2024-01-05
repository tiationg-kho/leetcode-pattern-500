# math

## intro

- Catalan Number
    - Cn = C(2n, n) / (n+1) or (2n)! / (n+1)!n!
        - C0 is the base case, equal to 1
        - Cn is calculated by summing the product of Catalan numbers Ci and Cn-i-1 for all i from 0 to n-1
            - C0 = 1
            - C1 = C0 * C0 = 1
            - C2 = C0 * C1 + C1 * C0 = 2
            - C3 = C0 * C2 + C1 * C1 + C2 * C0 = 5
            - C4 = C0 * C3 + C1 * C2 + C2 * C1 + C3 * C0 = 14
            - C5 = C0 * C4 + C1 * C3 + C2 * C2 + C3 * C1 + C4 * C0 = 42
        - C0 = 1, C(n+1) = Cn * ((4n + 2) / (n + 2))
    - related problem
        - unique BST / unique full binary tree
            - think about choose root node first then decide the left and right child
            - each number 1 through n can be the root, and the number of unique trees is the product of the number of unique trees in the left and right subtrees, which are themselves Catalan Numbers
            - eg. when n = 3 (node 1, 2 ,3)
                - node 1 as root, so 0 node at left, 2 nodes at right
                - node 2 as root, so 1 node at left, 1 node at right
                - node 3 as root, so 2 nodes at left, 0 node at right
        - balanced parentheses
            - think about we got single fixed pair of parentheses
            - we can put x pairs inside it, and y pairs after (at right side of) this fixed pair
            - eg. when n = 3
                - 2 pairs inside, 0 pair right side
                - 1 pairs inside, 1 pair right side
                - 0 pairs inside, 2 pair right side
        - valid stack orderings
            - we can convert this problem into balanced parentheses

## pattern

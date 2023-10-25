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
    - related problem
        - unique BST / unique full binary tree
            - think about choose root node first then decide the left and right child
            - eg. when n = 3 (node 1, 2 ,3)
                - node 1 as root, so 0 node at left, 2 nodes at right
                - node 2 as root, so 1 node at left, 1 node at right
                - node 3 as root, so 2 nodes at left, 0 node at right
        - balanced parentheses
            - think about we got a fixed pair of parentheses
            - we can put x pairs inside and y pairs after (at right side of) this fixed pair
            - eg. when n = 3
                - 2 pairs inside, 0 pair right side
                - 1 pairs inside, 1 pair right side
                - 0 pairs inside, 2 pair right side
        - valid stack orderings
            - we can convert this problem into balanced parentheses

## pattern

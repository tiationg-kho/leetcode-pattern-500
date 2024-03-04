/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        HashMap<Node, Node> oldToNew = new HashMap<>();
        if (node == null) {
            return node;
        }
        oldToNew.put(node, new Node(node.val));
        ArrayDeque<Node> queue = new ArrayDeque<>();
        queue.offer(node);
        while (!queue.isEmpty()) {
            Node oldNode = queue.poll();
            Node newNode = oldToNew.get(oldNode);
            for (Node neighbor: oldNode.neighbors) {
                if (!oldToNew.containsKey(neighbor)) {
                    oldToNew.put(neighbor, new Node(neighbor.val));
                    queue.offer(neighbor);
                }
                Node newNeighbor = oldToNew.get(neighbor);
                newNode.neighbors.add(newNeighbor);
            }
        }
        return oldToNew.get(node);
    }
}

// time O(n)
// space O(n)
// using graph and bfs with single source and hashmap
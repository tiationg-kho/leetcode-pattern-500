class Node {
    int key;
    int val;
    Node prev;
    Node next;
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class Dll {
    Node head;
    Node tail;
    public Dll() {
        head = new Node(- 1, - 1);
        tail = new Node(- 1, - 1);
        head.next = tail;
        tail.prev = head;
    }

    public void append(Node node) {
        Node prevNode = tail.prev;
        Node nextNode = tail;
        prevNode.next = node;
        node.prev = prevNode;
        node.next = nextNode;
        nextNode.prev = node;
        return;
    }

    public void update(Node node) {
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        this.append(node);
        return;
    }

    public Node popleft() {
        Node prevNode = head;
        Node node = prevNode.next;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        return node;
    }
}

class LRUCache {
    int capacity;
    Dll dll;
    HashMap<Integer, Node> keyToNode;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        dll = new Dll();
        keyToNode = new HashMap<>();
    }
    
    public int get(int key) {
        if (!keyToNode.containsKey(key)) {
            return - 1;
        }
        Node node = keyToNode.get(key);
        dll.update(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (keyToNode.containsKey(key)) {
            Node node = keyToNode.get(key);
            node.val = value;
            dll.update(node);
            return;
        }
        if (keyToNode.size() == capacity) {
            Node removeNode = dll.popleft();
            keyToNode.remove(removeNode.key);
        }
        Node node = new Node(key, value);
        keyToNode.put(key, node);
        dll.append(node);
        return;
    }
}

/**
* Your LRUCache object will be instantiated and called as such:
* LRUCache obj = new LRUCache(capacity);
* int param_1 = obj.get(key);
* obj.put(key,value);
*/

// time O(1)
// space O(capacity)
// using linked list and dll and hashmap
/*
1. maintain key_node hashmap
2. maintain dll
3. maintain capacity
4. if get() or put(), dll update the recent used node to the dll's tail or just append node to tail
5. if exceed capacity, dll popleft the least recent used node and pop it from hashmap
*/
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return new ArrayList<>(Arrays.asList(0));
        }
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        HashMap<Integer, Integer> indegrees = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
            indegrees.put(i, 0);
        }
        for (int[] pq: edges) {
            int p = pq[0];
            int q = pq[1];
            graph.get(p).add(q);
            graph.get(q).add(p);
            indegrees.put(p, indegrees.get(p) + 1);
            indegrees.put(q, indegrees.get(q) + 1);
        }

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (Integer p: indegrees.keySet()) {
            if (Objects.equals(indegrees.get(p), 1)) {
                queue.offer(p);
            }
        }
        List<Integer> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            int levelCount = queue.size();
            res = new ArrayList<>();
            for (int i = 0; i < levelCount; i++) {
                Integer node = queue.poll();
                res.add(node);
                for (Integer neighbor: graph.get(node)) {
                    indegrees.put(neighbor, indegrees.get(neighbor) - 1);
                    if (Objects.equals(indegrees.get(neighbor), 1)) {
                        queue.offer(neighbor);
                    }
                }
            }
        }
        return res;
    }
}

// time O(V+E)
// space O(V+E), due to building graph
// using graph and kahn and topological sort
/*
1. we want the root node as center as possible
2. so start from removing all cur leaf nodes in each round
*/
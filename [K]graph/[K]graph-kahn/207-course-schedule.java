class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        HashMap<Integer, Integer> indegrees = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
            indegrees.put(i, 0);
        }
        for (int[] prereq: prerequisites) {
            int q = prereq[0];
            int p = prereq[1];
            graph.get(p).add(q);
            indegrees.put(q, indegrees.get(q) + 1);
        }

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (Integer node: indegrees.keySet()) {
            if (Objects.equals(indegrees.get(node), 0)) {
                queue.offer(node);
            }
        }
        ArrayList<Integer> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            Integer node = queue.poll();
            res.add(node);
            for (Integer neighbor: graph.get(node)) {
                indegrees.put(neighbor, indegrees.get(neighbor) - 1);
                if (Objects.equals(indegrees.get(neighbor), 0)) {
                    queue.offer(neighbor);
                }
            }
        }
        return res.size() == numCourses;
    }
}

// time O(V+E)
// space O(V+E), due to building graph
// using graph and kahn and topological sort
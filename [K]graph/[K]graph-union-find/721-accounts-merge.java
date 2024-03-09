class UnionFind {
    int[] parents;
    int[] rank;

    public UnionFind(Integer n) {
        parents = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
            rank[i] = 0;
        }
    }

    public Integer find(Integer p) {
        while (p != parents[p]) {
            parents[p] = parents[parents[p]];
            p = parents[p];
        }
        return p;
    }

    public void union(Integer p, Integer q) {
        Integer rootP = find(p);
        Integer rootQ = find(q);
        if (rootP == rootQ) {
            return;
        }
        if (rank[rootP] > rank[rootQ]) {
            parents[rootQ] = rootP;
        } else if (rank[rootP] < rank[rootQ]) {
            parents[rootP] = rootQ;
        } else {
            parents[rootP] = rootQ;
            rank[rootQ] += 1;
        }
    }
}

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        UnionFind uf = new UnionFind(accounts.size());
        HashMap<String, Integer> emailToId = new HashMap<>();
        for (int i = 0; i < accounts.size(); i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String mail = accounts.get(i).get(j);
                if (emailToId.containsKey(mail)) {
                    uf.union(emailToId.get(mail), i);
                } else {
                    emailToId.put(mail, i);
                }
            }
        }

        HashMap<Integer, Set<String>> idToEmails = new HashMap<>();
        for (int i = 0; i < accounts.size(); i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String mail = accounts.get(i).get(j);
                Integer id = uf.find(i);
                idToEmails.computeIfAbsent(id, k -> new HashSet<>()).add(mail);
            }
        }

        List<List<String>> res = new ArrayList<>();
        for (Map.Entry<Integer, Set<String>> entry: idToEmails.entrySet()) {
            Integer id = entry.getKey();
            Set<String> mails = entry.getValue();
            ArrayList<String> info = new ArrayList<>();
            info.addAll(mails);
            Collections.sort(info);
            info.add(0, accounts.get(id).get(0));
            res.add(info);
        }
        return res;
    }
}

// time O(mlogm + n + m), due to sort
// space O(m+n), due to hashmap, m is the number of mails, n is the number of accounts
// using graph and union find and sort
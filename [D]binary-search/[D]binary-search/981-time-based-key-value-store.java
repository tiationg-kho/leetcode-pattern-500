class TimeMap {
    HashMap<String, ArrayList<Pair>> map;

    record Pair(String value, int timestamp) { }

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new Pair(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }
        ArrayList<Pair> list = map.get(key);
        int left = 0;
        int right = list.size() - 1;
        int boundary = - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            if (list.get(m).timestamp <= timestamp) {
                boundary = m;
                left = m + 1;
            } else {
                right = m - 1;
            }
        }
        if (boundary == - 1) {
            return "";
        }
        return list.get(boundary).value;
    }
}

/**
* Your TimeMap object will be instantiated and called as such:
* TimeMap obj = new TimeMap();
* obj.set(key,value,timestamp);
* String param_2 = obj.get(key,timestamp);
*/

// time O(logn) for get()
// space O(n), due to hashmap, n is the number of calling set()
// using binary search and search in a sorted array for most close val and hashmap
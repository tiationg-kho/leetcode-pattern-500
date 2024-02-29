class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> closeOpen = new HashMap<>();
        closeOpen.put(')', '(');
        closeOpen.put('}', '{');
        closeOpen.put(']', '[');
        ArrayDeque<Character> stack = new ArrayDeque<>();
        for (Character c: s.toCharArray()) {
            if (closeOpen.containsKey(c)) {
                if (!closeOpen.get(c).equals(stack.peek())) {
                    return false;
                }
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}

// time O(n)
// space O(n)
// using stack and queue and use stack to store the last states and hashmap
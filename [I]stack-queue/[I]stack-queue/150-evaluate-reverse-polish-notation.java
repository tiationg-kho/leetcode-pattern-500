class Solution {
    public int evalRPN(String[] tokens) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (String token: tokens) {
            if ("+-*/".contains(token)) {
                Integer second = stack.pop();
                Integer first = stack.pop();
                if (Objects.equals(token, "+")){
                    stack.push(first + second);
                } else if (Objects.equals(token, "-")) {
                    stack.push(first - second);
                } else if (Objects.equals(token, "*")) {
                    stack.push(first * second);
                } else {
                    stack.push(first / second);
                }
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.peek();
    }
}

// time O(n), due to traverse
// space O(n), due to stack
// using stack and queue and use stack to store the last states
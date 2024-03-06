class MinStack {
    ArrayDeque<Long> stack;
    long min;

    public MinStack() {
        stack = new ArrayDeque<>();
        min = 0;
    }
    
    public void push(int val) {
        if (stack.isEmpty()) {
            min = val;
            stack.push(0L);
        } else {
            long diff = val - min;
            if (diff < 0) {
                min = val;
                stack.push(diff);
            } else {
                stack.push(diff);
            }
        }
    }
    
    public void pop() {
        Long diff = stack.peek();
        if (diff < 0) {
            min += Math.abs(diff);
            stack.pop();
        } else {
            stack.pop();
        }
        if (stack.isEmpty()) {
            min = 0;
        }
    }
    
    public int top() {
        Long diff = stack.peek();
        if (diff < 0) {
            return (int) min;
        }
        return (int) (min + diff);
    }
    
    public int getMin() {
        return (int) min;
    }
}

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(val);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
*/

// time O(1)
// space O(n)
// using stack and queue and implement stack/queue and one stack
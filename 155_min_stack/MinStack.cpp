class MinStack {
    public:
        std::stack<int> stack;
        std::stack<int> min_stack;
        int min;
    
        MinStack() { min = INT_MAX; }
    
        void push(int val) {
            if (val <= min) {
                min_stack.push(min);
                min = val;
            }
    
            stack.push(val);
        }
    
        void pop() {
            int prev = stack.top();
    
            if (prev == min) {
                min = min_stack.top();
                min_stack.pop();
            }
    
            stack.pop();
        }
    
        int top() { return stack.top(); }
    
        int getMin() { return min; }
    };
    
    /**
     * Your MinStack object will be instantiated and called as such:
     * MinStack* obj = new MinStack();
     * obj->push(val);
     * obj->pop();
     * int param_3 = obj->top();
     * int param_4 = obj->getMin();
     */
class MinStack {
public:
    /**
     * Time Complexity: O(1) for each operation
     * Space Complexity: O(n) for n elements in stack
     */
    stack<int> main_stack;
    stack<int> min_stack;
    MinStack() {

    }
    
    void push(int val) {
        if(min_stack.empty() || min_stack.top() >= val){
            min_stack.push(val);
        }
        main_stack.push(val);
    }
    
    void pop() {
        if(main_stack.empty()) return;
        if(main_stack.top() == min_stack.top()){
            min_stack.pop();
        }
        main_stack.pop();
    }
    
    int top() {
        return main_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
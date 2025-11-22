#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> p_stack;
        for(char ch : s){
            if(!p_stack.empty()){
                if(p_stack.top() == '(' && ch == ')'){
                    p_stack.pop();
                } else if(p_stack.top() == '{' && ch == '}'){
                    p_stack.pop();
                } else if(p_stack.top() == '[' && ch == ']'){
                    p_stack.pop();
                } else {
                    p_stack.push(ch);
                }
            } else {
                p_stack.push(ch);
            }
        }
        return p_stack.empty();
    }
};
class Solution {
    public:
        int evalRPN(vector<string>& tokens) {
            stack<int> stack;
            set<string> operations = {"+", "-", "*", "/"};
    
            for (auto token : tokens) {
                if (operations.find(token) != operations.end()) {
                    int b = stack.top();
                    stack.pop();
                    int a = stack.top();
                    stack.pop();
                    int c = calculate(a, b, token);
                    stack.push(c);
                } else {
                    stack.push(stoi(token));
                }
            }
    
            return stack.top();
        }
    
    private:
        int calculate(int a, int b, string op) {
            if (op == "+") return a + b;
            if (op == "-") return a - b;
            if (op == "*") return a * b;
            if (op == "/") return a / b;
    
            return 0;
        }
    };
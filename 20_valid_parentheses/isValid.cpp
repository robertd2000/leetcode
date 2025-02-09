class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> map;
        map[')'] = '(';
        map['}'] = '{';
        map[']'] = '[';

        for (auto i : s) {
            if (map.find(i) != map.end()) {
                if (!stack.empty() && stack.top() == map[i]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(i);
            }
        }

        if (!stack.empty())
            return false;

        return true;
    }
};
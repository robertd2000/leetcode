class Solution {
    public:
        int longestPalindrome(string s) {
            int res = 0;
    
            set<char> visited;
    
            for (char c : s) {
                if (visited.find(c) != visited.end()) {
                    res += 2;
                    visited.erase(c);
                } else {
                    visited.insert(c);
                }
            }
    
            if (!visited.empty()) res++;
    
            return res;
        }
    };
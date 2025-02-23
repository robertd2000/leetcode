class Solution {
    public:
        string longestPalindrome(string s) {
            string res = "";
            int maxLen = 0;
            int n = s.length();
    
            for (int i = 0; i < n; i++) {
                int l = i;
                int r = i;
    
                while (l >= 0 && r < n && s[l] == s[r]) {
                    int diff = r - l + 1;
                    if (diff > maxLen) {
                        maxLen = diff;
                        res = s.substr(l, diff);
                    }
                    l--;
                    r++;
                }
    
                l = i;
                r = i + 1;
    
                while (l >= 0 && r < n && s[l] == s[r]) {
                    int diff = r - l + 1;
                    if (diff > maxLen) {
                        maxLen = diff;
                        res = s.substr(l, diff);
                    }
                    l--;
                    r++;
                }
            }
    
            return res;
        }
    };
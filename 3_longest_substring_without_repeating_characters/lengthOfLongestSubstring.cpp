class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            int n = s.length();
    
            if (n == 0)
                return 0;
    
            int longest = 0;
            unordered_map<char, int> map;
    
            int j = 0;
    
            for (int i = 0; i < n; i++) {
                if (map.contains(s[i])) {
                    j = max(j, map[s[i]] + 1);
                }
                map[s[i]] = i;
                longest = max(longest, i - j + 1);
            }
    
            return longest;
        }
    };
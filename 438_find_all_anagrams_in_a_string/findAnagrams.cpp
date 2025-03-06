class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            vector<int> res;
    
            int n = s.length();
            int m = p.length();
    
            int freqS[26] = {0};
            int freqP[26] = {0};
    
            if (n < m) {
                return res;
            }
    
            for (int i = 0; i < m; i++) {
                freqS[(int)s[i] - 97]++;
                freqP[(int)p[i] - 97]++;
            }
    
            int start = 0;
            int end = m;
    
            if (std::equal(std::begin(freqS), std::end(freqS), std::begin(freqP))) {
                res.push_back(start);
            }
    
            while (end < n) {
                freqS[(int)s[start] - 97]--;
                freqS[(int)s[end] - 97]++;
    
                if (std::equal(std::begin(freqS), std::end(freqS),
                               std::begin(freqP))) {
                    res.push_back(start + 1);
                }
    
                start++;
                end++;
            }
    
            return res;
        }
    };
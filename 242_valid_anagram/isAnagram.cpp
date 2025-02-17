class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.length();
        int m = t.length();

        if (n != m) return false;

        unordered_map<char, int> hash;

        for (char ch: s) {
            hash[ch]++;
        }

        for (char ch: t) {
            hash[ch]--;

            if (hash[ch] < 0) return false;
        }

        return true;
    }
};
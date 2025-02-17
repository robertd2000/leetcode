class Solution {
public:
    bool isAlphanumeric(char ch) {
        return std::isalnum(ch);
    }
    bool isPalindrome(string s) {
        int n = s.length();

        int l = 0;
        int r = n - 1;

        while (l < r) {
            if (!isAlphanumeric(s[l])) {
                l++;
                continue;
            }
            if (!isAlphanumeric(s[r])) {
                r--;
                continue;
            }

            if (isAlphanumeric(s[l]) && isAlphanumeric(s[r])) {
                if (std::tolower(s[l]) != std::tolower(s[r])) {
                    return false;
                }

                l++;
                r--;
            }
        }

        return true;
    }
};
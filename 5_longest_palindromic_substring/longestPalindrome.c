char* longestPalindrome(char* s) {
    int maxLen = 0;
    int n = strlen(s);

    char* res;

    for (int i = 0; i < n; i++) {
        int l = i;
        int r = i;

        while (l >= 0 && r < n && s[l] == s[r]) {
            int diff = r - l + 1;
            if (diff > maxLen) {
                maxLen = diff;
                res = malloc(maxLen + 1);
                memcpy(res, &s[l], maxLen);
                res[maxLen] = '\0';
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
                res = malloc(maxLen + 1);
                memcpy(res, &s[l], maxLen);
                res[maxLen] = '\0';
            }
            l--;
            r++;
        }
    }

    return res;
}
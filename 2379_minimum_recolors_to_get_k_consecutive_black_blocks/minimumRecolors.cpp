class Solution {
    public:
        int minimumRecolors(string blocks, int k) {
            int n = blocks.length();
    
            int min_changes = n;
            int black_count = 0;
    
            for (int i = 0; i < n; i++) {
                if (i - k >= 0 && blocks[i - k] == 'B') black_count--;
                if (blocks[i] == 'B') black_count++;
                min_changes = min(min_changes, k - black_count);
            }
    
            return min_changes;
        }
    };
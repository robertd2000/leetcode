class Solution {
public:
    int maxArea(vector<int>& height) {
        int maximum = 0;

        int l = 0;
        int r = height.size() - 1;

        while (l < r) {
            int lHeight = height[l];
            int rHeight = height[r];

            int square = min(lHeight, rHeight) * (r - l);

            if (square > maximum) {
                maximum = square;
            }

            if (lHeight < rHeight) {
                l++;
            } else {
                r--;
            }
        }

        return maximum;
    }
};
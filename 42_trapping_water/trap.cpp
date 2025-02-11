class Solution {
public:
    int trap(vector<int>& height) {
        int total = 0;
        int n = height.size();
        int left = 1;
        int right = n - 2;
        int maxLeft = height[0];
        int maxRight = height[n - 1];

        while (left <= right) {
            if (maxLeft < maxRight) {
                maxLeft = max(maxLeft, height[left]);
                total += maxLeft - height[left];
                left++;
            } else {
                maxRight = max(maxRight, height[right]);
                total += maxRight - height[right];
                right--;
            }
        }

        return total;
    }
};
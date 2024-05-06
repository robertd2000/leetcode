class Solution {
    public int trap(int[] height) {
        int result = 0;

        int n = height.length;
        int left = 0;
        int right = n - 1;

        int leftMax = height[0];
        int rightMax = height[n - 1];

        while (left <= right) {
            leftMax = Math.max(height[left], leftMax);
            rightMax = Math.max(height[right], rightMax);

            if (rightMax >= leftMax) {
                result += leftMax - height[left];
                left++;
            } else {
                result += rightMax - height[right];
                right--;
            }
        }

        return result;
    }
}
int trap(int* height, int heightSize) {
    int left = 1;
    int right = heightSize - 2;

    int leftMax = height[0];
    int rightMax = height[heightSize - 1];

    int result = 0;

    while (left <= right) {
        if (leftMax < rightMax) {
            if (height[left] > leftMax) {
                leftMax = height[left];
            }
            result += leftMax - height[left];
            left++;
        } else {
            if (height[right] > rightMax) {
                rightMax = height[right];
            }
            result += rightMax - height[right];
            right--;
        }
    }

    return result;
}
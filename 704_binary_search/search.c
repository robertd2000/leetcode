int search(int* nums, int numsSize, int target) {
    int low = 0;
        int hight = numsSize - 1;

        while (low <= hight) {
            int mid = (hight + low) / 2;

            if (nums[mid] == target) return mid;
            if (nums[mid] < target) {
                low = mid + 1;
            }
            if (nums[mid] > target) {
                hight = mid - 1;
            }
        }
        return -1;
}
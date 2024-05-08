/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));

    if (result == NULL) {
        *returnSize = 0;
        return NULL;
    }

    int l = 0;
    int r = numbersSize - 1;

    while (l < r) {
        if (numbers[l] + numbers[r] == target) {
            result[0] = l + 1;
            result[1] = r + 1;

            *returnSize = 2;
            return result;
        }

        if (numbers[l] + numbers[r] > target) {
            r--;
        }

        if (numbers[l] + numbers[r] < target) {
            l++;
        }
    }
    *returnSize = 0;
    free(result);
    return NULL;
}
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume
 * caller calls free().
 */
int comp(const void* a, const void* b) {
    return (*(int**)a)[0] - (*(int**)b)[0];
}

int** merge(int** intervals, int intervalsSize, int* intervalsColSize,
            int* returnSize, int** returnColumnSizes) {
    qsort(intervals, intervalsSize, sizeof(int*), comp);

    int** stack = (int**)malloc(sizeof(int*) * intervalsSize);
    stack[0] = intervals[0];
    int top = 1;
    for (int i = 1; i < intervalsSize; i++) {
        if (intervals[i][0] <= stack[top - 1][1]) {
            stack[top - 1][1] = intervals[i][1] > stack[top - 1][1]
                                    ? intervals[i][1]
                                    : stack[top - 1][1];
        } else {
            stack[top++] = intervals[i];
        }
    }

    *returnSize = top;
    *returnColumnSizes = (int*)malloc(sizeof(int) * (*returnSize));
    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = 2;
    }
    return stack;
}
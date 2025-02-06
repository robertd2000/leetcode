int **insert(int **intervals, int intervalsSize, int *intervalsColSize, int *newInterval, int newIntervalSize, int *returnSize, int **returnColumnSizes) {
    int **result = (int **)malloc((intervalsSize + 1) * sizeof(int *));
    *returnSize = 0;
    *returnColumnSizes = (int *)malloc((intervalsSize + 1) * sizeof(int));
    
    int i = 0;
    while (i < intervalsSize && intervals[i][1] < newInterval[0]) {
        result[*returnSize] = (int *)malloc(2 * sizeof(int));
        result[*returnSize][0] = intervals[i][0];
        result[*returnSize][1] = intervals[i][1];
        (*returnColumnSizes)[*returnSize] = 2;
        (*returnSize)++;
        i++;
    }
    
    while (i < intervalsSize && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = (newInterval[0] < intervals[i][0]) ? newInterval[0] : intervals[i][0];
        newInterval[1] = (newInterval[1] > intervals[i][1]) ? newInterval[1] : intervals[i][1];
        i++;
    }
    
    result[*returnSize] = (int *)malloc(2 * sizeof(int));
    result[*returnSize][0] = newInterval[0];
    result[*returnSize][1] = newInterval[1];
    (*returnColumnSizes)[*returnSize] = 2;
    (*returnSize)++;
    
    while (i < intervalsSize) {
        result[*returnSize] = (int *)malloc(2 * sizeof(int));
        result[*returnSize][0] = intervals[i][0];
        result[*returnSize][1] = intervals[i][1];
        (*returnColumnSizes)[*returnSize] = 2;
        (*returnSize)++;
        i++;
    }
    
    return result;
}
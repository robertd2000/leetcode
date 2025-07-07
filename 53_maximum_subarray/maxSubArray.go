func maxSubArray(nums []int) int {
    maxSum := nums[0]
    sum := 0

    for _, num := range nums {
        if sum < 0 {
            sum = 0
        }

        sum += num
        maxSum = max(maxSum, sum)
    }

    return maxSum
}
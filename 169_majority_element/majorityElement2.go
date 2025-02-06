func majorityElement(nums []int) int {
    count := 1
    major := nums[0]

    for _, num := range nums[1:] {
        if count == 0 {
            count = 1
            major = num
        } else if num == major {
            count++
        } else {
            count--
        }
    }

    return major
}
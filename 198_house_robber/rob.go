func rob(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    p1, p2 := 0, 0

    for _, num := range nums {
        p1, p2 = max(p1, p2 + num), p1        
    }

    return p1
}
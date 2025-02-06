func containsDuplicate(nums []int) bool {
    count := make(map[int]int)

    for _, i := range nums {
        if _, ok := count[i]; ok {
            return true
        }

        count[i] = 1
    }
    
    return false
}
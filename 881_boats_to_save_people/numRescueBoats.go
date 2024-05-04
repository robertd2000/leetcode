func numRescueBoats(people []int, limit int) int {
    sort.Ints(people)
    left, right, count := 0, len(people) -1, 0

    for left <= right {
        if people[left] + people[right] <= limit {
            left++
            right--
        } else {
            right--
        }

        count++
    }

    return count
}
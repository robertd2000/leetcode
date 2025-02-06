func insert(intervals [][]int, newInterval []int) [][]int {
    var res [][]int

    for idx, interval := range intervals {
        if interval[0] > newInterval[1] {
            res = append(res, newInterval)
            res = append(res, intervals[idx:]...)
            return res
        } else if interval[1] < newInterval[0] {
            res = append(res, interval)
        } else {
            start := min(interval[0], newInterval[0])
            end := max(interval[1], newInterval[1])
            newInterval = []int {start, end}
        }
    }
    
    res = append(res, newInterval)

    return res
}

func max(a int, b int) int {
    if a > b {
        return a
    }

    return b
}

func min(a int, b int) int {
    if a < b {
        return a
    }

    return b
}
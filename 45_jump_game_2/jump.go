func jump(nums []int) int {
    c, r, j, n := 0, 0, 0, len(nums)

    for i, val := range nums[:n - 1] {
        r = findMax(r, val + i)

        if i == j {
            j = r
            c++
        }
    }

    return c
}

func findMax(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
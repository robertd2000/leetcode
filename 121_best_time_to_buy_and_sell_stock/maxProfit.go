func maxProfit(prices []int) int {
    l, r, max := 0, 1, 0

    for r < len(prices) {
        candidate := prices[r] - prices[l]
        if prices[r] > prices[l] {
            max = findMax(candidate, max)
        } else {
            l = r
        }

        r++
    }


    return max
}

func findMax(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
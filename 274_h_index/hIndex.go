func hIndex(citations []int) int {
    h, n := 0, len(citations)
    
    sort.Ints(citations)

    for i, val := range citations {
        m := n - findIndexOfElement(citations, val, i)
        h = findMax(findMin(m, val), h)
    }

    return h
}

func findIndexOfElement(arr []int, el int, start int) int {
    for i := start; i < len(arr); i++ {
        if arr[i] == el {
            return i
        }
        
    }
    return -1
}

func findMax(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

func findMin(a int, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}
func findAnagrams(s string, p string) []int {
    n := len(s)
    m := len(p)

    res := make([]int, 0)

    if n < m {
        return res
    }

    freqS := [26]int{}
    freqP := [26]int{}

    for i := 0; i < m; i++ {
        freqS[s[i] - 'a']++
        freqP[p[i] - 'a']++
    }

    start := 0
    end := m

    if freqS == freqP {
        res = append(res, start)
    }

    for end < n {
        freqS[s[start] - 'a']--
        freqS[s[end] - 'a']++

        if freqS == freqP {
            res = append(res, start + 1)
        }

        start++
        end++
    }

    return res
}
func reversePrefix(word string, ch byte) string {
    chIndex := findIndexInString(word, ch)
    prefix := reverse(word[0:chIndex + 1])
    postfix := word[chIndex + 1:]

    return prefix + postfix
}

func reverse(word string) string {
   n := len(word)
    res := make([]byte, n)

    for i, j := 0, n-1; i < n; i, j = i+1, j-1 {
        res[i] = word[j]
    }

    return string(res)
}

func findIndexInString(word string, ch byte) int {
    for i := range word {
        if word[i] == byte(ch) {
            return i
        }
    }

    return -1
}
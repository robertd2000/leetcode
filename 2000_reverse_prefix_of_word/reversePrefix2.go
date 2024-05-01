func reversePrefix(word string, ch byte) string {
    chIndex := findIndexInString(word, ch)
    prefix := reverse(word[0:chIndex + 1])
    postfix := word[chIndex + 1:]

    return prefix + postfix
}

func reverse(word string) string {
   var res strings.Builder
    n := len(word)

    for i := n - 1; i >= 0; i-- {
        res.WriteByte(word[i])
    }

    return res.String()
}

func findIndexInString(word string, ch byte) int {
    for i := range word {
        if word[i] == byte(ch) {
            return i
        }
    }

    return -1
}
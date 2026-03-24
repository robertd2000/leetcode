impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
    let h_len = haystack.len();
    let n_len = needle.len();

    if h_len < n_len {
        return -1;
    }

    for front in 0..=(h_len - n_len) {
        if haystack[front..front+n_len] == needle {
            return front as i32;
        }
    }

    -1
    }
}
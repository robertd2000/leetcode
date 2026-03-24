impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let n = haystack.len();
        let m = needle.len();

        if m == 0 {
            return 0;
        }

        if n < m {
            return -1;
        }

        for i in 0..n-m + 1 {
            let mut j = 0;

            while j < m && haystack.chars().nth(i + j).unwrap() == needle.chars().nth(j).unwrap() {
                j+=1;
            }

            if j == m {
                return i as i32;
            }
        }

        -1
    }
}
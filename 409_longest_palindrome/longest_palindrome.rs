use std::collections::HashSet;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut res = 0;

        let mut visited = HashSet::new();

        for c in s.chars() {
            if visited.contains(&c) {
                res += 2;
                visited.remove(&c);
            } else {
                visited.insert(c);
            }
        }

        if !visited.is_empty() {
            res += 1;
        }

        return res;
    }
}
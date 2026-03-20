use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut h_map = HashMap::new();

        for c in s.chars() {
            *h_map.entry(c).or_insert(0) += 1;
        }

        for c in t.chars() {
            let e = h_map.entry(c).or_insert(0);
            *e -= 1;
            if *e < 0 {
                return false;
            }
        }

        true
    }
}
use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut h_map = HashMap::new();

        for c in s.chars() {
            let e = h_map.entry(c).or_insert(0);
            *e += 1;
        }

        for (i, c) in s.chars().enumerate() {
            if *h_map.get(&c).unwrap() == 1 {
                return i as i32;
            }
        }

        -1
    }
}
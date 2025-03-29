use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut res = 0;
        let n = s.len();

        if n == 0 {
            return res;
        }

        let mut h_map: HashMap<char, i32> = HashMap::new();

        let mut j = 0;

        for c in 0..n {
            let i = c as i32;
            let key = s.chars().nth(c).unwrap();

            if h_map.contains_key(&key) {
                j = cmp::max(j, h_map.get(&key).map(|&x| x + 1).unwrap()) as i32;
            }
            res = cmp::max(res, (i - j + 1) as i32);
            h_map.insert(key, i);
        }

        return res;
    }
}
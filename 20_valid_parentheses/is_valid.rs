use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();

        let mut p = HashMap::new();
        p.insert(')', '(');
        p.insert(']', '[');
        p.insert('}', '{');

        for c in s.chars() {
            if p.contains_key(&c) {
                if !stack.is_empty() && stack.last() == p.get(&c) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        if !stack.is_empty() {
            return false;
        }

        return true;
    }
}
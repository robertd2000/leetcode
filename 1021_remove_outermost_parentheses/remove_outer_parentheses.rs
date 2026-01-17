impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut res = String::new();
        let mut level = 0;

        for c in s.chars() {
            if c == '(' {
                if level > 0 {
                    res.push(c);
                }

                level += 1;
            } else {
                if level > 1 {
                    res.push(c);
                }

                level -= 1;
            }
        }
        
        res
    }
}
struct MinStack {
    min: i32,
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        MinStack {
            min: i32::MAX,
            stack: Vec::new(),
            min_stack: Vec::new(), 
        }
    }
    
    fn push(&mut self, val: i32) {
        self.stack.push(val);
        if val <= self.min {
            self.min_stack.push(self.min);
            self.min = val;
        }
    }
    
    fn pop(&mut self) {
        let val = self.stack.pop().unwrap();
        if val == self.min {
            self.min = self.min_stack.pop().unwrap();
        }
    }
    
    fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }
    
    fn get_min(&self) -> i32 {
        self.min
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
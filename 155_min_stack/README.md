[155. Min Stack](https://leetcode.com/problems/min-stack/)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

**Input**
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

**Output**
[null,null,null,null,-3,null,0,-2]

**Explanation**
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top(); // return 0
minStack.getMin(); // return -2

**Constraints:**

- `-231 <= val <= 231 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 104` calls will be made to `push`, `pop`, `top`, and `getMin`.

[155. Min Stack](https://leetcode.com/problems/min-stack/)

Спроектируйте стек, который поддерживает push, pop, top и извлечение минимального элемента за постоянное время.

Реализуйте класс `MinStack`:

- `MinStack()` инициализирует объект стека.
- `void push(int val)` помещает элемент `val` в стек.
- `void pop()` удаляет элемент на вершине стека.
- `int top()` получает верхний элемент стека.
- `int getMin()` извлекает минимальный элемент в стеке.

Необходимо реализовать решение со сложностью `O(1)` для каждой функции.

**Пример 1:**

**Вход**
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

**Выход**
[null,null,null,null,-3,null,0,-2]

**Объяснение**
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // вернуть -3
minStack.pop();
minStack.top(); // вернуть 0
minStack.getMin(); // return -2

**Ограничения:**

- `-231 <= val <= 231 - 1`
- Методы `pop`, `top` и `getMin` операции всегда будут вызываться на **непустых** стеках.
- Максимум `3 * 104` вызовов `push`, `pop`, `top` и `getMin`.

Для решения нужно использовать 2 стека:

- в первом хранить значения - stack
- во втором предыдущие минимумы - minStack

Также нужно хранить текущий минимум currentMin
При добавлении нового элемента val в стек проверяем, он меньше текущего минимума minStack и если да, то

- добавить текущий минимум minStack в стек с минимумами minStack
- обновить текущий минимум minStack значением val
  После этого нужно добавить val в стек stack

При удалении элемента из стека, нужно проверить, равен ли он текущему минимуму. Если да, то значит нужно обновить текущий минимум, так как мы удаляем его значение. Для этого обновляем текущий минимум currentMin последним значением из стека minStack, так как там будет хранится последний минимум, тот который был там до добавления текущего минимума (то есть элементы в minStack будут по сути отсортированы). После этого удалим последний элемент из minStack и из stack.

Итоговый код:

```typescript
class MinStack {
  stack: number[];
  minStack: number[];
  currentMin: number;

  constructor() {
    this.stack = [];
    this.minStack = [];
    this.currentMin = Infinity;
  }

  push(val: number): void {
    this.stack.push(val);

    if (val <= this.currentMin) {
      this.minStack.push(this.currentMin);
      this.currentMin = val;
    }
  }

  pop(): void {
    const value = this.stack.pop();

    if (value === this.currentMin) {
      this.currentMin = this.minStack[this.minStack.length - 1];
      this.minStack.pop();
    }
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.currentMin;
  }
}
```

Можно обойтись и одним стеком - хранить в нем объекты со значением и текущим минимумом.

```js
var MinStack = function () {
  this.stack = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
  this.stack.push({
    value: val,
    min: this.stack.length === 0 ? val : Math.min(val, this.getMin()),
  });
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  return this.stack.at(-1).value;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  return this.stack.at(-1).min;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.minStack.append(self.min)
            self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            self.min = self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

```go

type MinStack struct {
    Stack []int
    Min int
    MinStack []int
}


func Constructor() MinStack {
    stack := MinStack{
        Stack: []int{},
        MinStack: []int{},
        Min: 1<<63-1,
    }
    return stack
}


func (this *MinStack) Push(val int)  {
  this.Stack = append(this.Stack, val)

  if val <= this.Min {
      this.MinStack = append(this.MinStack, this.Min)
      this.Min = val
  }
}


func (this *MinStack) Pop()  {
    if this.Stack[len(this.Stack) - 1] == this.Min {
        this.Min = this.MinStack[len(this.MinStack) - 1]
        this.MinStack = this.MinStack[0: len(this.MinStack) - 1]
    }
    this.Stack = this.Stack[0: len(this.Stack) - 1]
}


func (this *MinStack) Top() int {
    return this.Stack[len(this.Stack) - 1]
}


func (this *MinStack) GetMin() int {
    return this.Min
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

```

```java

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    private int min;

    public MinStack() {
        this.stack = new Stack<>();
        this.minStack = new Stack<>();
        this.min = Integer.MAX_VALUE;
    }

    public void push(int val) {
        this.stack.push(val);

        if (val <= this.min) {
            this.minStack.push(this.min);
            this.min = val;
        }
    }

    public void pop() {
        int prev = this.stack.pop();

        if (prev == this.min) {
            this.min = this.minStack.pop();
        }
    }

    public int top() {
        return this.stack.peek();
    }

    public int getMin() {
        return this.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

```

```cpp

class MinStack {
public:
    std::stack<int> stack;
    std::stack<int> min_stack;
    int min;

    MinStack() { min = INT_MAX; }

    void push(int val) {
        if (val <= min) {
            min_stack.push(min);
            min = val;
        }

        stack.push(val);
    }

    void pop() {
        int prev = stack.top();

        if (prev == min) {
            min = min_stack.top();
            min_stack.pop();
        }

        stack.pop();
    }

    int top() { return stack.top(); }

    int getMin() { return min; }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

```

```rs

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

```

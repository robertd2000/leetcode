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
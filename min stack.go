type MinStack struct {

    stack []int
    minStack []int
    
}


func Constructor() MinStack {
    return MinStack{
        stack: []int{},      
        minStack: []int{},   
    }
}


func (this *MinStack) Push(val int)  {
    
    if len(this.stack) > 0 {
        if val <= this.minStack[len(this.minStack) - 1] {
            this.minStack = append(this.minStack, val)
        } 
            
        
    } else {
        this.minStack = append(this.minStack, val)
    }

    this.stack = append(this.stack, val)

    
}


func (this *MinStack) Pop()  {
    
    if this.Top() == this.GetMin()  {
        this.minStack = this.minStack[:len(this.minStack) - 1]
    }
   
    this.stack = this.stack[:len(this.stack) - 1]
     
    
}


func (this *MinStack) Top() int {

    return this.stack[len(this.stack) - 1]
    
}


func (this *MinStack) GetMin() int {

    if len(this.minStack) < 1 {
        return 0
    }
    return this.minStack[len(this.minStack) - 1]


}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
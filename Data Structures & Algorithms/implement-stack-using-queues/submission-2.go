type MyStack struct {
	queue []int
}

func Constructor() MyStack {
	return MyStack{}
}

func (this *MyStack) Push(x int) {
	this.queue = append(this.queue, x)
}

func (this *MyStack) Pop() int {
	if len(this.queue) == 1{
		num := this.queue[0]
		this.queue = this.queue[:0]
		return num
	}

	temp_q := reverse(this.queue)

	val := temp_q[0]
	temp_q = temp_q[1:]

	this.queue = temp_q
	return val
}

func (this *MyStack) Top() int {
	temp := reverse(this.queue)
	return temp[0]
}

func (this *MyStack) Empty() bool {
	if len(this.queue) == 0{
		return true
	}

	return false
}

func reverse(queue []int) []int{
	copied := make([]int, len(queue))
	copy(copied, queue)

	for range len(copied) - 1{
		copied = append(copied[1:], copied[0])
	}
	return copied
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param2 := obj.Pop();
 * param3 := obj.Top();
 * param4 := obj.Empty();
 */
